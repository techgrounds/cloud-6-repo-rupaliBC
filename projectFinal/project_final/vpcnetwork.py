from aws_cdk import (
    # Duration,
    Stack,
    
    Duration,
    RemovalPolicy,
    Stack,
    CfnOutput,
    NestedStack,
     
    aws_ec2 as ec2,
    aws_ssm as ssm,
    aws_kms as kms,
    aws_backup as backup,
    aws_events as events,
    aws_iam as iam,
    aws_cloudformation as cfn,
    
    # aws_sqs as sqs,
)
from constructs import Construct
import aws_cdk as cdk

class vpcnetwork(cdk.NestedStack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
         #####     Parameters    ##########
        myenvironment=self.node.try_get_context("myenvironment")

         ###     VPC parameters    ########
        vpcenv=myenvironment.get("vpc_s")
        vpc1_id=vpcenv.get("vpc1_id")
        vpc1_max_az= vpcenv.get("vpc1_max_az")
        vpc1_subnet_name= vpcenv.get("vpc1_subnet_name")
        vpc1_cidr_range=vpcenv.get("vpc1_cidr_range")
        vpc2_id=vpcenv.get("vpc2_id")
        vpc2_max_az=vpcenv.get("vpc2_max_az")
        vpc2_subnet_name= vpcenv.get("vpc2_subnet_name")
        vpc2_cidr_range=vpcenv.get("vpc2_cidr_range")

        ### VPC #####
        self.vpc = ec2.Vpc(self,vpc1_id,
                           max_azs=vpc1_max_az,
                           cidr=vpc1_cidr_range,
                           subnet_configuration=[
                            ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PUBLIC,
                               cidr_mask=27,
                               name=vpc1_subnet_name,
                            ),
                            ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT,
                               name="Private Subnet"),
                            ],
                           nat_gateway_subnets=ec2.SubnetSelection(
                                     subnet_group_name=vpc1_subnet_name,
                                   ),
                             )
            
        CfnOutput(self, "Output",
                       value=self.vpc.vpc_id)

         #### VPC 2 settings for management server  ####

        self.vpc2 = ec2.Vpc(self, vpc2_id,
                           max_azs=vpc2_max_az,
                           cidr=vpc2_cidr_range,
                            subnet_configuration=[
                                ec2.SubnetConfiguration(
                                  subnet_type=ec2.SubnetType.PUBLIC,
                                  name=vpc2_subnet_name
                                  )
                            ],
                            )
        CfnOutput(self, "Output1",
                       value=self.vpc2.vpc_id)
         
