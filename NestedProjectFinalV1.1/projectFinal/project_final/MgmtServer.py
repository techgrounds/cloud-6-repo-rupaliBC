from aws_cdk import (
    Stack,
    aws_ec2 as ec2,
    aws_iam as iam
   
)
from constructs import Construct
from aws_cdk import NestedStack
import aws_cdk as cdk
from cdk_ec2_key_pair import KeyPair
   
class mgmtserver(cdk.NestedStack):

    def __init__(self, scope: Construct, construct_id: str,vpc2:ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
         #####     Parameters    ##########
        myenvironment=self.node.try_get_context("myenvironment")
        SecurityGp=myenvironment.get("SecurityGp")
        mgsg_id=SecurityGp.get("mgsg_id")
        mgsg_name=SecurityGp.get("mgsg_name")
        mgsg_peer= SecurityGp.get("mgsg_peer")
        servers=myenvironment.get("servers")
        mgmt_instance_type=servers.get("mgmt_instance_type")
        mgmt_volume_size=servers.get("mgmt_volume_size")
            ### AMI ####
        amzn_windows = ec2.MachineImage.latest_windows(
            ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE
                           )
         ### Role ####
        role1= iam.Role(self,"keyrole1",
                              assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
                           )
        role1.add_managed_policy(
                                 iam.ManagedPolicy.from_aws_managed_policy_name
                                 ("AmazonSSMManagedInstanceCore")
                                 )
           ###add this role AmazonS3ReadOnlyAccess
        self.MgmtSG=ec2.SecurityGroup(self,mgsg_id,
                                 vpc= vpc2,
                                 description="MgmtSecurityGp",
                                 allow_all_outbound=True,
                                 security_group_name=mgsg_name)
        self.MgmtSG.add_ingress_rule(ec2.Peer.ipv4(mgsg_peer),
                                    ec2.Port.tcp(22),
                                    "SSH Connecton")
        self.MgmtSG.add_ingress_rule(ec2.Peer.ipv4(mgsg_peer),
                                    ec2.Port.tcp(3389),
                                    "SSH Connecton")
        self.MgmtSG.add_ingress_rule(ec2.Peer.ipv4(mgsg_peer),
                                    ec2.Port.tcp(80),
                                    "HTTP")
        self.MgmtSG.add_ingress_rule(ec2.Peer.ipv4(mgsg_peer),
                                    ec2.Port.tcp(443),
                                    "HTTPS")

      ### Key Pair for mgmt server ####

        key1 = KeyPair(self,"KeyPair2",
                        name="MgmtServerKey",
                        store_public_key=True,
                        resource_prefix="K"
                     )
        
        key1.grant_read_on_private_key(role1)
        key1.grant_read_on_public_key(role1)

         ######## Launch Management server( EC2 Instance )   ########
        
        self.instance2 = ec2.Instance(self, "mgmtServer",
                    instance_type=ec2.InstanceType(mgmt_instance_type),
                    machine_image=amzn_windows,
                    vpc = vpc2,
                    block_devices= [ec2.BlockDevice(
                                device_name="/dev/sda1", 
                                volume=ec2.BlockDeviceVolume.ebs(
                                 volume_size= mgmt_volume_size,
                               # volume_type=ec2.EbsDeviceVolumeType.GP2,
                                encrypted=True
                    ),
                     )],
                    role=role1,
                    security_group = self.MgmtSG,
                    key_name=key1.key_pair_name
                     )
