from constructs import Construct
from aws_cdk import (
    
    Stack,
     CfnOutput, 
    aws_ec2 as ec2,
    aws_ssm as ssm,
    
    
)
from cdk_ec2_key_pair import KeyPair


     

class NewProjectStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        ####### VPC ( for web server )###############
       
        self.vpc = ec2.Vpc(self, "VPC",
                           max_azs=2,
                           cidr="10.10.10.0/24",
                            subnet_configuration=[ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PUBLIC,
                               name="Public",
                                  )
                            ]
                             )
            
        CfnOutput(self, "Output",
                       value=self.vpc.vpc_id)

       ######### AMI linux    ############         
                       
        amzn_linux = ec2.AmazonLinuxImage(generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
                                 edition=ec2.AmazonLinuxEdition.STANDARD,
                                 virtualization=ec2.AmazonLinuxVirt.HVM,
                                 storage=ec2.AmazonLinuxStorage.GENERAL_PURPOSE
                                    )

        ### Key Pair
        key = KeyPair(self,"KeyPair",
                        name="WebServerKey",
                        store_public_key=True
                     )
       
        ##### User Data for web server launch ######
        with open("./userdata.sh") as f:
                    user_data = f.read()
        ##### Security Group for web server ###########
        
        webSG=ec2.SecurityGroup(self,"webSG",vpc= self.vpc,
                                 allow_all_outbound=True,
                                    security_group_name="WebserverSG")
        webSG.add_ingress_rule(ec2.Peer.any_ipv4(),
                                 ec2.Port.tcp(80),
                                    "http traffic")
        webSG.add_ingress_rule(ec2.Peer.any_ipv4(),
                                 ec2.Port.tcp(443),
                                    "https traffic")
        webSG.add_ingress_rule(ec2.Peer.any_ipv4(),
                                    ec2.Port.tcp(22),
                                       "ssh")

        ######## Lanuch web server( EC2 Instance )   ########
        instance1 = ec2.Instance(self, "Instance",
        instance_type=ec2.InstanceType("t2.micro"),
        machine_image=amzn_linux,
        vpc = self.vpc,
        block_devices= [ec2.BlockDevice(
                        device_name="/dev/xvda", 
                        volume=ec2.BlockDeviceVolume.ebs(
                        volume_size=8,
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
        
    
        
        

'''
        self.vpc2 = ec2.Vpc(self, "VPC2",
                           max_azs=2,
                           cidr="10.10.20.0/24",
                            subnet_configuration=[ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PUBLIC,
                               name="Public",
                                  )
                            ]
                            )
            
                           
        CfnOutput(self, "Output2",
                       value=self.vpc2.vpc_id)

                       ### Key Pair####

        key1 = KeyPair(self,"KeyPair2",
                        name="MgmtServerKey",
                        store_public_key=True
                     )
       
        
        ##### Security Group for Management Server  ###########

        MgmtSG=ec2.SecurityGroup(self,"MgmtSG",
                                 vpc= self.vpc2,
                                 allow_all_outbound=True,
                                 security_group_name="MgmtServerSG")
        MgmtSG.add_ingress_rule(ec2.Peer.ipv4(),
                                    ec2.Port.tcp(22),
                                    "SSH Connecton")
        
         
   
    ######## Lanuch Management server( EC2 Instance )   ########

        instance2 = ec2.Instance(self, "Instance2",
                    instance_type=ec2.InstanceType("t2.micro"),
                    machine_image=amzn_linux,
                    vpc = self.vpc2,
                    block_devices= [ec2.BlockDevice(
                                device_name="/dev/xvda", 
                                volume=ec2.BlockDeviceVolume.ebs(
                                 volume_size=8,
                                volume_type=ec2.EbsDeviceVolumeType.GP2,
                                encrypted=True
                    ),
                    mapping_enabled= True
                     )],
        
        security_group = MgmtSG,
        key_name=key1.key_pair_name
        )
       
        
    
        
        

                           
        

        
        
        
   
        )
     
'''
    