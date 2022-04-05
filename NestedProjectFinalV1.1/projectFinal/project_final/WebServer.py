from aws_cdk import (
    aws_ec2 as ec2,
    aws_iam as iam,
    aws_autoscaling as autoscaling,
    aws_certificatemanager as acm
   
)
from cdk_iam_floyd import Ec2
from constructs import Construct
from aws_cdk import NestedStack
import aws_cdk as cdk
from cdk_ec2_key_pair import KeyPair
from aws_cdk.aws_s3_assets import Asset
from aws_cdk.aws_elasticloadbalancingv2 import SslPolicy
  
   
class webserver(cdk.NestedStack):

    def __init__(self, scope: Construct, construct_id: str,vpc:ec2.Vpc,MgmtSG:ec2.SecurityGroup,ASGSG:ec2.SecurityGroup, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
         #####     Parameters    ##########
        myenvironment=self.node.try_get_context("myenvironment")
        servers=myenvironment.get("servers")
        web_instance_type=servers.get("web_instance_type")
        web_volume_size=servers.get("web_volume_size")
        autoscale=myenvironment.get("autoscale")
        desired_capacity=autoscale.get("desired_capacity")
        min_capacity=autoscale.get("min_capacity")
        max_capacity=autoscale.get("max_capacity")
     
         ######### AMI linux    ############         
                     
        amzn_linux = ec2.MachineImage.latest_amazon_linux(
                                 generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
                                 edition=ec2.AmazonLinuxEdition.STANDARD,
                                 virtualization=ec2.AmazonLinuxVirt.HVM,
                                 storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
                                    )
        role1= iam.Role(self,"keyrole1",
                              assumed_by=iam.ServicePrincipal("ec2.amazonaws.com"),
                           )
        role1.add_managed_policy(
                                 iam.ManagedPolicy.from_aws_managed_policy_name
                                 ("AmazonSSMManagedInstanceCore")
                                 )
  
        ### Key Pair
        key = KeyPair(self,"KeyPair",
                        name="WebServerKey",
                        store_public_key=True,
                        resource_prefix="k1"
                     )
        
        key.grant_read_on_private_key(role1)
        key.grant_read_on_public_key(role1)
        
       # Create AutoScaling Group with 2 EC2 Instances.
        self.web_server_asg = autoscaling.AutoScalingGroup(self,
                                                       "webServerAsgId",
                                                       vpc=vpc,
                                                       instance_type=ec2.InstanceType(web_instance_type),
                                                       machine_image=amzn_linux,
                                                       role=role1,
                                                       security_group=ASGSG,
                                                       #associate_public_ip_address=False,
                                                       desired_capacity=desired_capacity,
                                                       min_capacity=min_capacity,
                                                       max_capacity=max_capacity,
                                                    
                                                       block_devices=[
                                                      autoscaling.BlockDevice(
                                                          device_name="/dev/xvda",
                                                         volume=autoscaling.BlockDeviceVolume.ebs(
                                                         volume_size=web_volume_size,
                                                         volume_type=ec2.EbsDeviceVolumeType.GP2,
                                                        encrypted=True,
                                                         delete_on_termination=True,
                                                         )
                                                       )
                                                       ],
                                                       key_name=key.key_pair_name,
                                                       vpc_subnets=ec2.SubnetSelection(
                                                           subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT
                                                        ),
                                                    
                                                     termination_policies=[autoscaling.TerminationPolicy.OLDEST_INSTANCE,autoscaling.TerminationPolicy.DEFAULT],
                                                       new_instances_protected_from_scale_in=False
                                                    )
                                                      
         ### Assigning UserData to Autoscaling group #####                                            
        assets = Asset(
                  self,
                  "Assets",
                  path="./Bucket/userdata1.sh"
                     )
        
        path = self.web_server_asg.user_data.add_s3_download_command(
                     bucket=assets.bucket,
                     bucket_key=assets.s3_object_key,
                     region="eu-central-1"
        )

        self.web_server_asg.user_data.add_execute_file_command(
            file_path=path
        )

        assets.grant_read(self.web_server_asg.role)

      
