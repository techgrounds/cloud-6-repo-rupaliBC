from itertools import count
from msilib.schema import Environment
from multiprocessing import Event
from multiprocessing.pool import TERMINATE
from operator import countOf
from cdk_iam_floyd import ElasticloadbalancingV2, Events, Health, Iam
from constructs import Construct
import boto3
import socket
from aws_cdk import (
    
    Duration,
    RemovalPolicy,
    Stack,
    CfnOutput,
    
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
   
       
)
from cdk_ec2_key_pair import KeyPair
from aws_cdk.aws_s3_assets import Asset
from aws_cdk.aws_elasticloadbalancingv2 import SslPolicy
  
class NewProjectStack(Stack):

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
        ## Peering #####
        peering_id= vpcenv.get("peering_id")
        peering_region= vpcenv.get("peering_region")
        vpc1_route_id = vpcenv.get("vpc1_route_id")
        vpc2_route_id = vpcenv.get("vpc2_route_id")
         ##### server security grp parameters ###
        SecurityGp=myenvironment.get("SecurityGp")
        mgsg_id=SecurityGp.get("mgsg_id")
        mgsg_name=SecurityGp.get("mgsg_name")
        mgsg_peer= SecurityGp.get("mgsg_peer")
        elbsg_id=SecurityGp.get("websg_id")
        elbsg_name=SecurityGp.get("websg_name")
        
        #######  Backup jobs #######
        BackupServers=myenvironment.get("BackupServers")    
        hour1=BackupServers.get("hour1")  
        minute1=BackupServers.get("minute1")
        day1=BackupServers.get("day1")
        month1=BackupServers.get("month1")
        year1=BackupServers.get("year1")
        duration1=BackupServers.get("duration1")  
        hour2=BackupServers.get("hour2")  
        minute2=BackupServers.get("minute2")
        day2=BackupServers.get("day2")
        month2=BackupServers.get("month2")
        year2=BackupServers.get("year2")
        duration2=BackupServers.get("duration2")  
        ####### VPC ( for web server )###############
       
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
         

      #### VPC Peering ######

        self.VPCPeering = ec2.CfnVPCPeeringConnection(
            self,
            peering_id,
            peer_vpc_id=self.vpc.vpc_id,
            vpc_id=self.vpc2.vpc_id,
            peer_region= peering_region
            )

    #### VPC subnet route table entry ######   
        for i in range(0,2):                          
                           self.cfn_Route = ec2.CfnRoute(self, vpc1_route_id+str(i),
                           route_table_id=self.vpc.public_subnets[i].route_table.route_table_id,
                           destination_cidr_block=self.vpc2.vpc_cidr_block,
                           vpc_peering_connection_id=self.VPCPeering.ref)
                           i=i+1
        for j in range(0,2):              
                           self.cfn_Route = ec2.CfnRoute(self, vpc2_route_id+str(j),
                           route_table_id=self.vpc2.public_subnets[j].route_table.route_table_id,
                           destination_cidr_block=self.vpc.vpc_cidr_block,
                           vpc_peering_connection_id=self.VPCPeering.ref)    
                           j=j+1
        for k in range(0,2):
                           self.cfn_Route = ec2.CfnRoute(self, "route_table_id"+str(k),
                           route_table_id=self.vpc.private_subnets[k].route_table.route_table_id,
                           destination_cidr_block=self.vpc2.vpc_cidr_block,
                           vpc_peering_connection_id=self.VPCPeering.ref)
                           k=k+1                           

        

       ######### AMI linux    ############         
                     
        amzn_linux = ec2.MachineImage.latest_amazon_linux(
                                 generation=ec2.AmazonLinuxGeneration.AMAZON_LINUX_2,
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
                                 ("AmazonSSMManagedInstanceCore")
                                 )
           ###add this role AmazonS3ReadOnlyAccess
        ### Key Pair
        key = KeyPair(self,"KeyPair",
                        name="WebServerKey",
                        store_public_key=True
                     )
        
        key.grant_read_on_private_key(role1)
        key.grant_read_on_public_key(role1)
        ##### User Data for web server launch ######
        with open("./Bucket/userdata1.sh") as f:
                    user_data = f.read()

        ##### Security Group for Management Server  ###########

        MgmtSG=ec2.SecurityGroup(self,mgsg_id,
                                 vpc= self.vpc2,
                                 description="MgmtSecurityGp",
                                 allow_all_outbound=True,
                                 security_group_name=mgsg_name)
        MgmtSG.add_ingress_rule(ec2.Peer.ipv4(mgsg_peer),
                                    ec2.Port.tcp(22),
                                    "SSH Connecton")
        MgmtSG.add_ingress_rule(ec2.Peer.ipv4(mgsg_peer),
                                    ec2.Port.tcp(3389),
                                    "SSH Connecton")
        MgmtSG.add_ingress_rule(ec2.Peer.ipv4(mgsg_peer),
                                    ec2.Port.tcp(80),
                                    "HTTP")
        MgmtSG.add_ingress_rule(ec2.Peer.ipv4(mgsg_peer),
                                    ec2.Port.tcp(443),
                                    "HTTPS")

      ### Key Pair for mgmt server ####

        key1 = KeyPair(self,"KeyPair2",
                        name="MgmtServerKey",
                        store_public_key=True
                     )
        
        key1.grant_read_on_private_key(role1)
        key1.grant_read_on_public_key(role1)
      ######## Launch Management server( EC2 Instance )   ########
        
        instance2 = ec2.Instance(self, "mgmtServer",
                    instance_type=ec2.InstanceType("t2.micro"),
                    machine_image=amzn_windows,
                    vpc = self.vpc2,
                    block_devices= [ec2.BlockDevice(
                                device_name="/dev/xvda", 
                                volume=ec2.BlockDeviceVolume.ebs(
                                 volume_size= 8,
                                volume_type=ec2.EbsDeviceVolumeType.GP2,
                                encrypted=True
                    ),
                    mapping_enabled= True
                     )],
       
                        role=role1,
                        security_group = MgmtSG,
                        key_name=key1.key_pair_name
                     )


        ##### Security Group for ELB  ###########
        
        ELBSG=ec2.SecurityGroup(self,"elbsg_id",vpc= self.vpc,
                                  description="ELBSecurityGp",
                                 allow_all_outbound=True,
                                    security_group_name=elbsg_name)
        ELBSG.add_ingress_rule(ec2.Peer.any_ipv4(),
                                 ec2.Port.tcp(80),
                                    "http traffic")
        ELBSG.add_ingress_rule(ec2.Peer.any_ipv4(),
                                 ec2.Port.tcp(443),
                                    "https traffic")
      #  ELBSG.add_ingress_rule(ec2.Peer.security_group_id(MgmtSG.security_group_id), ec2.Port.tcp(22),  "ssh")
                                    
         ##### Security Group for ASG  ###########
        ASGSG=ec2.SecurityGroup(self,"ASGSG",vpc= self.vpc,
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

        # Create Application Load Balancer
        
        
       # Create AutoScaling Group with 2 EC2 Instances.
        web_server_asg = autoscaling.AutoScalingGroup(self,
                                                       "webServerAsgId",
                                                       vpc=self.vpc,
                                                       instance_type=ec2.InstanceType("t3.nano"),
                                                       machine_image=amzn_linux,
                                                       role=role1,
                                                       security_group=ASGSG,
                                                       #associate_public_ip_address=False,
                                                       desired_capacity=1,
                                                       min_capacity=1,
                                                       max_capacity=3,
                                                    
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
        
        path = web_server_asg.user_data.add_s3_download_command(
                     bucket=assets.bucket,
                     bucket_key=assets.s3_object_key,
                     region="eu-central-1"
        )

        web_server_asg.user_data.add_execute_file_command(
            file_path=path
        )

        assets.grant_read(web_server_asg.role)

        #####  Application Load balancer #######

        alb = elb.ApplicationLoadBalancer(
            self,
            "myAlbId",
            vpc=self.vpc,
            internet_facing=True,
            security_group=ELBSG,
            load_balancer_name="WebServerAlb",
            )
        ## Self Signed certificate ######
        
        certificate=elb.ListenerCertificate.from_arn("arn:aws:acm:eu-central-1:638251832878:certificate/a70c031f-9145-4f99-9a0f-4ed69ba2d023")
       
        # Add Listerner to ALB
        listener = alb.add_listener("listernerId",
                                    port=443,
                                    certificates=[certificate],
                                    ssl_policy=elb.SslPolicy.TLS12_EXT,
                                    open=True
                                   )
        # listener connection
        listener.connections.allow_default_port_from_any_ipv4("allow")
         # Allow ALB to receive internet traffic
       # alb.connections.allow_from_any_ipv4(
        #    ec2.Port.tcp(80),
         #   description="Allow Internet access on ALB Port 80"
        #)

        # Allows ASG Security Group receive traffic from ALB
       
        web_server_asg.connections.allow_from(alb, ec2.Port.tcp(80),
                                              description="Allows ASG Security Group receive traffic from ALB")

        # Add ASG Instances to ALB Target Group
        listener.add_targets("targetId", port=80, targets=[web_server_asg])
        ### HTTP => HTTPS redirect
        alb.add_redirect(source_port=80, target_port=443)
        
        ### Health Check ####
        
        web_server_asg._alb_target_group.configure_health_check(interval=Duration.seconds(60), timeout=Duration.seconds(40))
        
        
       ### Autoscaling Action
        web_server_asg.scale_on_cpu_utilization("CPUUtilization",cooldown=Duration.seconds(100),
                            target_utilization_percent=50,
                             disable_scale_in=False)
        
        ## server Tags ###
        Tags.of(web_server_asg).add(key="webs",value="webbackup")
        Tags.of(instance2).add(key="mgmt",value="mgmtbackup")

        #### Back up Web Server ####
        WebBackupkey = kms.Key(
            self,
            "BackupkeyWebServer",
            removal_policy=RemovalPolicy.DESTROY
            )
        vault1= backup.BackupVault(self,"WebServerVault",
                                    backup_vault_name="WebServerVault",
                                    encryption_key=WebBackupkey,
                                    removal_policy=RemovalPolicy.DESTROY
                                    )
        backup_plan1 = backup.BackupPlan(self,"Backup1",
                                          backup_plan_name="webserverBackup"
                                          )
        backup_plan1.add_selection("ec2web",resources=[
                                    backup.BackupResource.from_tag(key="webs",value="webbackup")
                                             ]
                                                            )

        backup_plan1.add_rule(backup.BackupPlanRule(
                              backup_vault=vault1,
                              rule_name="WebRule",
                              schedule_expression=events.Schedule.cron
                                 (hour=hour1 ,minute=minute1,day=day1, month=month1,year=year1),
                              delete_after=Duration.days(duration1),
                              completion_window=Duration.hours(2),
                              start_window=Duration.hours(1)
                               ))           
                              
        #### Back up Management Server ####
        Mgmtbackupkey = kms.Key(
            self,
            "BackupkeyMgmtServer",
            removal_policy=RemovalPolicy.DESTROY
            )
        vault2= backup.BackupVault(self,"MgmtServerVault",
                                  backup_vault_name="MgmtServerVault",
                                  encryption_key=Mgmtbackupkey,
                                 removal_policy=RemovalPolicy.DESTROY)
        backup_plan2 = backup.BackupPlan(self,"Backup2",backup_plan_name="MgmtserverBackup")
        backup_plan2.add_selection("ec2mgmt",resources=[
                                          backup.BackupResource.from_tag(key="mgmt",value="mgmtbackup")
                                          ]
                                                            )

        backup_plan2.add_rule(backup.BackupPlanRule(
                              backup_vault=vault2,
                              rule_name="mgmtRule",
                              schedule_expression=events.Schedule.cron(
                                    hour=hour2 ,minute=minute2,day=day2, month=month2,year=year2
                                                ),
                              delete_after=Duration.days(duration2),
                              completion_window=Duration.hours(2),
                              start_window=Duration.hours(1)
                               ))                       
       
    
       

'''
        

       target_tracking_scaling_policy = autoscaling.TargetTrackingScalingPolicy(self, "MyTargetTrackingScalingPolicy",
                                        auto_scaling_group=web_server_asg,
                                            target_value=70,

                                # the properties below are optional
                                        #cooldown=Duration.seconds(60),
    
                                disable_scale_in=False,
                                #estimated_instance_warmup=Duration.minutes(30),
                            predefined_metric=autoscaling.PredefinedMetric.ASG_AVERAGE_CPU_UTILIZATION
                           

        
       
    
       
        ## server Tags ###
        Tags.of(instance1).add(key="webs",value="webbackup")
        Tags.of(instance2).add(key="mgmt",value="mgmtbackup")

        #### Back up Web Server ####
        WebBackupkey = kms.Key(
            self,
            "BackupkeyWebServer",
            removal_policy=RemovalPolicy.DESTROY
            )
        vault1= backup.BackupVault(self,"WebServerVault",
                                    backup_vault_name="WebServerVault",
                                    encryption_key=WebBackupkey,
                                    removal_policy=RemovalPolicy.DESTROY
                                    )
        backup_plan1 = backup.BackupPlan(self,"Backup1",
                                          backup_plan_name="webserverBackup"
                                          )
        backup_plan1.add_selection("ec2web",resources=[
                                    backup.BackupResource.from_tag(key="webs",value="webbackup")
                                             ]
                                                            )

        backup_plan1.add_rule(backup.BackupPlanRule(
                              backup_vault=vault1,
                              rule_name="WebRule",
                              schedule_expression=events.Schedule.cron
                                 (hour=hour1 ,minute=minute1,day=day1, month=month1,year=year1),
                              delete_after=Duration.days(duration1),
                              completion_window=Duration.hours(2),
                              start_window=Duration.hours(1)
                               ))           
                              
        #### Back up Management Server ####
        Mgmtbackupkey = kms.Key(
            self,
            "BackupkeyMgmtServer",
            removal_policy=RemovalPolicy.DESTROY
            )
        vault2= backup.BackupVault(self,"MgmtServerVault",
                                  backup_vault_name="MgmtServerVault",
                                  encryption_key=Mgmtbackupkey,
                                 removal_policy=RemovalPolicy.DESTROY)
        backup_plan2 = backup.BackupPlan(self,"Backup2",backup_plan_name="MgmtserverBackup")
        backup_plan2.add_selection("ec2mgmt",resources=[
                                          backup.BackupResource.from_tag(key="mgmt",value="mgmtbackup")
                                          ]
                                                            )

        backup_plan2.add_rule(backup.BackupPlanRule(
                              backup_vault=vault2,
                              rule_name="mgmtRule",
                              schedule_expression=events.Schedule.cron(
                                    hour=hour2 ,minute=minute2,day=day2, month=month2,year=year2
                                                ),
                              delete_after=Duration.days(duration2),
                              completion_window=Duration.hours(2),
                              start_window=Duration.hours(1)
                               ))                       
       
    
       
       
       
    
'''      
        

                           
        

       
        
        
   
        
     
    