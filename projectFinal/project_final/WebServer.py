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
    aws_iam as iam,
   
    Tags,
    aws_elasticloadbalancingv2 as elb,
    aws_elasticloadbalancingv2_targets as targets,
    aws_autoscaling as autoscaling,
    aws_certificatemanager as acm
   
    # aws_sqs as sqs,
)
from constructs import Construct
from aws_cdk import NestedStack
import aws_cdk as cdk
from cdk_ec2_key_pair import KeyPair
from aws_cdk.aws_s3_assets import Asset
from aws_cdk.aws_elasticloadbalancingv2 import SslPolicy
import importcert as cert
  
   
class webserver(cdk.NestedStack):

    def __init__(self, scope: Construct, construct_id: str,vpc:ec2.Vpc,MgmtSG:ec2.SecurityGroup, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
         #####     Parameters    ##########
        myenvironment=self.node.try_get_context("myenvironment")

        SecurityGp=myenvironment.get("SecurityGp")
        elbsg_id=SecurityGp.get("websg_id")
        elbsg_name=SecurityGp.get("websg_name")
        autoscale=myenvironment.get("autoscale")
        target_utilization_percent=autoscale.get("target_utilization_percent")
        desired_capacity=autoscale.get("desired_capacity")
        min_capacity=autoscale.get("min_capacity")
        max_capacity=autoscale.get("max_capacity")
        certificate_arn=myenvironment.get("certificate_arn")
        arn=certificate_arn.get("arn")

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
          ##### Security Group for ELB  ###########
        
        ELBSG=ec2.SecurityGroup(self,"elbsg_id",vpc= vpc,
                                  description="ELBSecurityGp",
                                 allow_all_outbound=True,
                                    security_group_name=elbsg_name)
        ELBSG.add_ingress_rule(ec2.Peer.any_ipv4(),
                                 ec2.Port.tcp(80),
                                    "http traffic")
        ELBSG.add_ingress_rule(ec2.Peer.any_ipv4(),
                                 ec2.Port.tcp(443),
                                    "https traffic")
     
         ##### Security Group for ASG  ###########
        ASGSG=ec2.SecurityGroup(self,"ASGSG",vpc= vpc,
                                  description="ASGSecurityGp",
                                 allow_all_outbound=True,
                                    security_group_name="ASGSG")
        ASGSG.add_ingress_rule(ec2.Peer.security_group_id(MgmtSG.security_group_id),
                               ec2.Port.tcp(22),"ssh")
        ASGSG.add_ingress_rule(ec2.Peer.security_group_id(ELBSG.security_group_id),
                              ec2.Port.tcp(80),"HTTP")
      #  ASGSG.add_ingress_rule(ec2.Peer.security_group_id(ELBSG.security_group_id),
       #                       ec2.Port.tcp(443),"HTTPS")
        ASGSG.add_ingress_rule(ec2.Peer.any_ipv4(),ec2.Port.tcp(80),"http traffic")
        ASGSG.add_ingress_rule(ec2.Peer.any_ipv4(),ec2.Port.tcp(443),"https traffic")                

       
        
       # Create AutoScaling Group with 2 EC2 Instances.
        self.web_server_asg = autoscaling.AutoScalingGroup(self,
                                                       "webServerAsgId",
                                                       vpc=vpc,
                                                       instance_type=ec2.InstanceType("t3.nano"),
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
                                                         volume_size=8,
                                                         volume_type=ec2.EbsDeviceVolumeType.GP2,
                                                        encrypted=True,
                                                         delete_on_termination=True,
                                                         )
                                                       )
                                                       ],
                                                       #security_group=ASGSG,
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
        
        certificate=elb.ListenerCertificate.from_arn(cert.generatecertificate())
       
        # Add Listerner to ALB
        listener = alb.add_listener("listernerId",
                                    port=443,
                                    certificates=[certificate],
                                    ssl_policy=elb.SslPolicy.TLS12_EXT,
                                    open=True
                                   )
        # listener connection
        #listener.connections.allow_default_port_from_any_ipv4("allow")

        # Allows ASG Security Group receive traffic from ALB
       
        #self.web_server_asg.connections.allow_from(alb, ec2.Port.tcp(80),
         #                                     description="Allows ASG Security Group receive traffic from ALB")
        health_check=elb.HealthCheck()
        # Add ASG Instances to ALB Target Group
        listener.add_targets("targetId", port=80, targets=[self.web_server_asg],health_check=health_check)
        ### HTTP => HTTPS redirect
        alb.add_redirect(source_port=80, target_port=443)

        ### Health Check ####
        
      #  self.web_server_asg._alb_target_group.configure_health_check(interval=Duration.seconds(60), timeout=Duration.seconds(40))
        
        
       ### Autoscaling Action
        self.web_server_asg.scale_on_cpu_utilization("CPUUtilization",cooldown=Duration.seconds(100),
                            target_utilization_percent=target_utilization_percent,
                             disable_scale_in=False)
        
        ## server Tags ###
        Tags.of(self.web_server_asg).add(key="webs",value="webbackup")
        