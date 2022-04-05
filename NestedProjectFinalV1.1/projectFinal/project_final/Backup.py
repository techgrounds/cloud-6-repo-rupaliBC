from aws_cdk import (
    Duration,
    RemovalPolicy,
    Stack,
    aws_ec2 as ec2,
    aws_kms as kms,
    aws_backup as backup,
    aws_events as events,
    Tags,
    aws_autoscaling as autoscaling
   
)
from cdk_iam_floyd import Ec2
from constructs import Construct
from aws_cdk import NestedStack
import aws_cdk as cdk
   
class backupserver(cdk.NestedStack):

    def __init__(self, scope: Construct, construct_id: str,web_server_asg:Ec2,instance2:autoscaling.AutoScalingGroup, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)
         #####     Parameters    ##########
        myenvironment=self.node.try_get_context("myenvironment")
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
       
    
       
