from aws_cdk import (
    Duration,
    aws_ec2 as ec2,
    aws_elasticloadbalancingv2 as elb,
    aws_autoscaling as autoscaling,
    aws_certificatemanager as acm
   
)
from cdk_iam_floyd import Ec2
from constructs import Construct
from aws_cdk import NestedStack
import aws_cdk as cdk
from aws_cdk.aws_elasticloadbalancingv2 import SslPolicy
  
   
class loadbalancer(cdk.NestedStack):

    def __init__(self, scope: Construct, construct_id: str,vpc:ec2.Vpc,ELBSG:ec2.SecurityGroup,web_server_asg:autoscaling.AutoScalingGroup,**kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
         #####     Parameters    ##########
        myenvironment=self.node.try_get_context("myenvironment")
        autoscale=myenvironment.get("autoscale")
        target_utilization_percent=autoscale.get("target_utilization_percent")
        certificate_arn=myenvironment.get("certificate_arn")
        arn=certificate_arn.get("arn")

         #####  Application Load balancer #######

        alb = elb.ApplicationLoadBalancer(
            self,
            "myAlbId",
            vpc=vpc,
            internet_facing=True,
            security_group=ELBSG,
            load_balancer_name="WebServerAlb",
            )
        ## Self Signed certificate ######
        
        certificate=elb.ListenerCertificate.from_arn(arn)
       
        # Add Listerner to ALB
        listener = alb.add_listener("listernerId",
                                    port=443,
                                    certificates=[certificate],
                                    ssl_policy=elb.SslPolicy.TLS12_EXT,
                                    open=True
                                   )
         ### Health Check ####
        health_check=elb.HealthCheck()
        # Add ASG Instances to ALB Target Group
        listener.add_targets("targetId", port=80, targets=[web_server_asg],health_check=health_check)
        ### HTTP => HTTPS redirect
        alb.add_redirect(source_port=80, target_port=443)
         ### Autoscaling Action
        web_server_asg.scale_on_cpu_utilization("CPUUtilization",cooldown=Duration.seconds(100),
                            target_utilization_percent=target_utilization_percent,
                             disable_scale_in=False)
       
        
'''
        self.web_server_asg._alb_target_group.configure_health_check(interval=Duration.seconds(60), timeout=Duration.seconds(40))
        
        
      
        
       # listener connection
        #listener.connections.allow_default_port_from_any_ipv4("allow")

        # Allows ASG Security Group receive traffic from ALB
       
        #self.web_server_asg.connections.allow_from(alb, ec2.Port.tcp(80),
         #                                     description="Allows ASG Security Group receive traffic from ALB")

'''