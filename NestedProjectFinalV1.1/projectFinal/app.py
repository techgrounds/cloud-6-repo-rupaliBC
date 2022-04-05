#!/usr/bin/env python3
import os

import aws_cdk as cdk


from project_final.vpcnetwork import vpcnetwork
from project_final.peering import peering
from project_final.MgmtServer import mgmtserver
from project_final.SecurityGrp import securitygrp
from project_final.WebServer import webserver
from project_final.LoadBalancer import loadbalancer
from project_final.Bucket import bucketboot
from project_final.Backup import backupserver

app = cdk.App()
main_stack=cdk.Stack(app,"mainstack")

vpc_app=vpcnetwork(main_stack, "vpcnet")
vpc_peering=peering(main_stack, "peering",vpc=vpc_app.vpc,vpc2=vpc_app.vpc2)
mgmt_app=mgmtserver(main_stack, "mgmtServer",vpc2=vpc_app.vpc2)
security_grp=securitygrp(main_stack, "securitygrp",vpc=vpc_app.vpc,MgmtSG=mgmt_app.MgmtSG)
bucket_bootstrap=bucketboot(main_stack, "bucket")
web_app=webserver(main_stack, "webServer",vpc=vpc_app.vpc,MgmtSG=mgmt_app.MgmtSG,ASGSG=security_grp.ASGSG)
load_balance=loadbalancer(main_stack, "loadbalancer",vpc=vpc_app.vpc,ELBSG=security_grp.ELBSG,web_server_asg=web_app.web_server_asg)
backup_server=backupserver(main_stack, "backupServer",web_server_asg=web_app.web_server_asg,
                                instance2=mgmt_app.instance2)


app.synth()
