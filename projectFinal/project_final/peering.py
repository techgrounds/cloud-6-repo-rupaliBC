
from aws_cdk import (
    # Duration,
    Stack,
      
    Duration,
    RemovalPolicy,
    Stack,
    CfnOutput,
    aws_cloudformation as cfn,
    aws_ec2 as ec2,
    aws_ssm as ssm,
    aws_kms as kms,
    aws_backup as backup,
    aws_events as events,
    aws_iam as iam
    
    # aws_sqs as sqs,
)
from constructs import Construct
from aws_cdk import NestedStack
import aws_cdk as cdk

class peering(cdk.NestedStack):

    def __init__(self, scope: Construct, construct_id: str,vpc:ec2.Vpc,vpc2:ec2.Vpc, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
         #####     Parameters    ##########
        myenvironment=self.node.try_get_context("myenvironment")
         ###     VPC peering parameters    ########
        peerings=myenvironment.get("peering")
        peering_id= peerings.get("peering_id")
        peering_region= peerings.get("peering_region")
        vpc1_route_id = peerings.get("vpc1_route_id")
        vpc2_route_id = peerings.get("vpc2_route_id")
        #### VPC Peering ######

        self.VPCPeering = ec2.CfnVPCPeeringConnection(
            self,
            peering_id,
            peer_vpc_id=vpc.vpc_id,
            vpc_id=vpc2.vpc_id,
            peer_region= peering_region
            )

    #### VPC subnet route table entry ######   
        for i in range(0,2):                          
                           self.cfn_Route = ec2.CfnRoute(self, vpc1_route_id+str(i),
                           route_table_id=vpc.public_subnets[i].route_table.route_table_id,
                           destination_cidr_block=vpc2.vpc_cidr_block,
                           vpc_peering_connection_id=self.VPCPeering.ref)
                           i=i+1
        for j in range(0,2):              
                           self.cfn_Route = ec2.CfnRoute(self, vpc2_route_id+str(j),
                           route_table_id=vpc2.public_subnets[j].route_table.route_table_id,
                           destination_cidr_block=vpc.vpc_cidr_block,
                           vpc_peering_connection_id=self.VPCPeering.ref)    
                           j=j+1
        for k in range(0,2):
                           self.cfn_Route = ec2.CfnRoute(self, "route_table_id"+str(k),
                           route_table_id=vpc.private_subnets[k].route_table.route_table_id,
                           destination_cidr_block=vpc2.vpc_cidr_block,
                           vpc_peering_connection_id=self.VPCPeering.ref)
                           k=k+1                           

