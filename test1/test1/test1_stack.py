from aws_cdk import (
    # Duration,
    Stack,
    aws_ec2 as ec2,
    CfnOutput
    # aws_sqs as sqs,
)
from constructs import Construct

class Test1Stack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        self.vpc = ec2.Vpc(self,"test1",
                           max_azs=2,
                           cidr="10.10.10.0/24",
                           
                            nat_gateways=1,
                            subnet_configuration=[ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PUBLIC,
                               cidr_mask=27,
                               name="public",
                                  ),
                                  ec2.SubnetConfiguration(subnet_type=ec2.SubnetType.PRIVATE_WITH_NAT,
                                  cidr_mask=27,
                                  name="Private Subnet",),
                            
                            ],
                            nat_gateway_subnets=ec2.SubnetSelection(
                                     subnet_group_name="public",
                                     #subnets=ec2.SubnetType.PUBLIC
                                     ),
                             )
            
        CfnOutput(self, "Output",
                       value=self.vpc.vpc_id)

         #### VPC 2 settings for management server  ####

        self.vpc2 = ec2.Vpc(self, "test2",
                           max_azs=2,
                           cidr="10.20.20.0/24",
                            subnet_configuration=[ec2.SubnetConfiguration(
                               subnet_type=ec2.SubnetType.PUBLIC,
                               name="public"
                                  )
                            ],
                            )
        CfnOutput(self, "Output1",
                       value=self.vpc2.vpc_id)
         

      #### VPC Peering ######

        self.VPCPeering = ec2.CfnVPCPeeringConnection(
            self,
            "peer",
            peer_vpc_id=self.vpc.vpc_id,
            vpc_id=self.vpc2.vpc_id,
            peer_region="eu-central-1"
            )
         
         
   
        for i in range(0,2):
                          
                           self.cfn_Route = ec2.CfnRoute(self, "route_table_id"+str(i),
                           route_table_id=self.vpc.public_subnets[i].route_table.route_table_id,
                           destination_cidr_block=self.vpc2.vpc_cidr_block,
                           vpc_peering_connection_id=self.VPCPeering.ref)
                           i=i+1
        for j in range(0,2):
                          
                           self.cfn_Route = ec2.CfnRoute(self, "route_table1_id"+str(j),
                           route_table_id=self.vpc.private_subnets[j].route_table.route_table_id,
                           destination_cidr_block=self.vpc2.vpc_cidr_block,
                           vpc_peering_connection_id=self.VPCPeering.ref)
                           j=j+1
        for k in range(0,2):              
                           self.cfn_Route = ec2.CfnRoute(self,"route_table2_id"+str(k),
                           route_table_id=self.vpc2.public_subnets[k].route_table.route_table_id,
                           destination_cidr_block=self.vpc.vpc_cidr_block,
                           vpc_peering_connection_id=self.VPCPeering.ref)   
                           k=k+1                            

        
