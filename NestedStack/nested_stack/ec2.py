from constructs import Construct
from aws_cdk import (
    Duration,
    RemovalPolicy,
    NestedStack,
    aws_cloudformation as cfn,
     CfnOutput,
    aws_ec2 as ec2,
    aws_ssm as ssm,
    aws_kms as kms,
    aws_events as events,
    aws_iam as iam,
)
from cdk_ec2_key_pair import KeyPair
class WebServer(NestedStack):

    def __init__(self, scope: Construct, construct_id: str,**kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
        
        amzn_linux = ec2.MachineImage.latest_amazon_linux(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
                                 edition=ec2.AmazonLinuxEdition.STANDARD,
                                 virtualization=ec2.AmazonLinuxVirt.HVM,
                                 storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
                                    )
        ### AMI Windows
        amzn_windows = ec2.MachineImage.latest_windows(
            ec2.WindowsVersion.WINDOWS_SERVER_2019_ENGLISH_FULL_BASE
                           )
         ### Role ####
        role1= iam.Role(self,"keyrole1",
                              assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
                           )
        role1.add_managed_policy(
                                 iam.ManagedPolicy.from_aws_managed_policy_name
                                 ("AmazonSSMFullAccess")
                                 )
        ### Key Pair
        key = KeyPair(self,"KeyPair",
                        name="WebServerKey",
                        store_public_key=True
                     )
        
        key.grant_read_on_private_key(role1)
        key.grant_read_on_public_key(role1)
        ##### User Data for web server launch ######
        with open("./Bucket/userdata.sh") as f:
                    user_data = f.read()

        
        ##### Security Group for web server ###########
        
        webSG=ec2.SecurityGroup(self,"websg",vpc= self.vpc,
                                  description="WebSecurityGp",
                                 allow_all_outbound=True,
                                    security_group_name="websg")
        webSG.add_ingress_rule(ec2.Peer.any_ipv4(),
                                 ec2.Port.tcp(80),
                                    "http traffic")
        webSG.add_ingress_rule(ec2.Peer.any_ipv4(),
                                 ec2.Port.tcp(443),
                                    "https traffic")
        
        instance1 = ec2.Instance(self, "webserver",
                                    instance_type=ec2.InstanceType("t2.micro"),
                                    machine_image=amzn_linux,
                                    vpc = self.vpc,
                                     block_devices= [ec2.BlockDevice(
                                    device_name="/dev/xvda",
                                     volume=ec2.BlockDeviceVolume.ebs(
                                                                     volume_size= 8,
                                                                     volume_type=ec2.EbsDeviceVolumeType.GP2,
                                                                     encrypted=True
                                                                      ),
                                     mapping_enabled= True
                                       )
                                                ],
                                 user_data=ec2.UserData.custom(user_data),
                                 
                                  security_group = webSG,
                                  key_name=key.key_pair_name
        )
        instance1.connections.allow_from_any_ipv4(port_range=ec2.Port.tcp(80)
                                                  , description="Allow Web Traffic")



        CfnOutput(self,"ip", value=str(instance1.instance_private_ip))