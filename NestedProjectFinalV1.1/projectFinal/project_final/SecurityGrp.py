from aws_cdk import (
    aws_ec2 as ec2,
    
)
from constructs import Construct
from aws_cdk import NestedStack
import aws_cdk as cdk

class securitygrp(cdk.NestedStack):

    def __init__(self, scope: Construct, construct_id: str,vpc:ec2.Vpc,MgmtSG:ec2.SecurityGroup, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
         #####     Parameters    ##########
        myenvironment=self.node.try_get_context("myenvironment")

        SecurityGp=myenvironment.get("SecurityGp")
        elbsg_id=SecurityGp.get("elbsg_id")
        elbsg_name=SecurityGp.get("elbsg_name")
        asgsg_id=SecurityGp.get("asgsg_id")
        asgsg_name=SecurityGp.get("asgsg_name")

  
  ##### Security Group for ELB  ###########
        
        self.ELBSG=ec2.SecurityGroup(self,elbsg_id,vpc= vpc,
                                  description="ELBSecurityGp",
                                 allow_all_outbound=True,
                                    security_group_name=elbsg_name)
        self.ELBSG.add_ingress_rule(ec2.Peer.any_ipv4(),
                                 ec2.Port.tcp(80),
                                    "http traffic")
        self.ELBSG.add_ingress_rule(ec2.Peer.any_ipv4(),
                                 ec2.Port.tcp(443),
                                    "https traffic")
     
         ##### Security Group for ASG  ###########
        self.ASGSG=ec2.SecurityGroup(self,asgsg_id,vpc= vpc,
                                  description="ASGSecurityGp",
                                 allow_all_outbound=True,
                                    security_group_name=asgsg_name)
        self.ASGSG.add_ingress_rule(ec2.Peer.security_group_id(MgmtSG.security_group_id),
                               ec2.Port.tcp(22),"ssh")
        self.ASGSG.add_ingress_rule(ec2.Peer.security_group_id(self.ELBSG.security_group_id),
                              ec2.Port.tcp(80),"HTTP")
      #  ASGSG.add_ingress_rule(ec2.Peer.security_group_id(ELBSG.security_group_id),
       #                       ec2.Port.tcp(443),"HTTPS")
        self.ASGSG.add_ingress_rule(ec2.Peer.any_ipv4(),ec2.Port.tcp(80),"http traffic")
        self.ASGSG.add_ingress_rule(ec2.Peer.any_ipv4(),ec2.Port.tcp(443),"https traffic")                

       