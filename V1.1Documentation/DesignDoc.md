# Project by Sentia


## Infrastructure as code app to build cloud infrastructure


### Introduction

Help a company transition to the cloud. The company had its infrastructure analyzed by a previous team. A diagram has been made based on the current situation.

You will build the Infrastructure as Code app to bring this design to the cloud. You are supposed to use AWS CDK ( Cloud Development Kit) .


### Requirements

The following requirements are indicated as necessary:

1. All VM disks must be encrypted.
2. The web server must be backed up daily. The backups must be kept for 7 days.
3. The web server must be installed in an automated manner.
4. The admin/management server must be reachable with a public IP.
5. The admin/management server should only be reachable from trusted locations (office/admin's home)
6. The following IP ranges are used: 10.10.10.0/24 & 10.20.20.0/24
7. All subnets must be protected by a firewall at the subnet level.
8. SSH or RDP connections to the web server may only be established from the admin server.
9. The web server should no longer be accessible on the Internet. Ideally, the customer would like to see a load balancer placed in between.
10. The server should no longer have a public IP address.
11. In case a user connects to the load balancer via HTTP, this connection should automatically be upgraded to HTTPS.
12. The connection should be secured with TLS 1.2 or higher.
13. The web server must undergo a health check at regular intervals.
14. If the web server fails this health check the server should be restored automatically.
15. If the web server is subjected to a sustained load, a temporary extra server should be started. The customer thinks that no more than 3 servers in total will ever be needed given the user numbers in the past.


# Architecture 
 ![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/V1.1new.png)


# 
## Services Used: 

- VPC ( Virtual Private Network)
- EC2 ( Elastic Compute Cloud)
- VPC Peering
- KMS (Key Management Services)
- IAM ( Identity and Access Management)
- S3 Storage
- EBS ( Elastic Block Storage)
- AWS Backup Service
- Secret Manager
- Autoscaling Group
- Load Balancer
- Certificate Manager
- lambda


![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/archi33.png)


## Assumptions:


1. **There will be 2 VPC’s**
    - Production VPC will have 2 public subnets and 2 private subnets.
    - Management VPC will have 2 public subnets.
    - Multi-VPC architecture will allow you to isolate different parts of your infrastructure.
    - Furthermore to achieve high availability, it is good practice to deploy service to at least two AZ’s. If one AZ goes down there will always be another to take over.
2. **VPC Peering Connection**-
    - With peering, the servers in different VPC’s can talk to each other via private IP
3. **Auto Scaling Group - Web Server**
    - Autoscaling group will be used to launch webservers.
    - Web servers will be kept in private subnet as it should no longer be accessible on internet or have a public ip.
    - The Load Balancer will be kept in between Autoscaling group and the internet.
    - Nat Gateway will be kept in publuc subnet (The instances in the public subnet can send outbound traffic directly to the internet, whereas the instances in the private subnet can’t. The instances in the private subnet can access the internet by using a network address translation (NAT) gateway that resides in the public subnet)
    - Desired Capacity / Min Capacity =  1
    - max capacity = 3
    - Web server will get installed automatically by providing User Data. 
    - The root volume (EBS) will be encrypted and the key will be stored in AWS KMS.
    - The web server will need Security Group rules that allow inbound HTTP traffic from Load Balancer.
    - For SSH connection, Management server’s source ip will be used.
    - AWS Backup will allow you to take backups daily and to maintain it for a required number of days.
    - Key Pair will be created and will be stored in the Secrets manager.  
4. **Management Server**
    - The management server will have port 22 open for SSH connection from trusted locations.
    - The root volume (EBS) will be encrypted and the key will be stored in AWS KMS.
    - The IAM Role will be created which will then be attached to the EC2 instance. This will ensure limited user access to the management server.
    - Key Pair will be created and will be stored in the Secrets manager.
5. **S3 storage**
    - Bootstrap Scripts will be kept in S3 bucket.
    - The bucket will be encrypted with a key stored in KMS.  
  

  ## Design and Specification:


#   
| Services                       | Requirement                                                                                                                                       | Configuration                                                                                                                                                            | Comments/Questions                                                                                                                                                                                        |
| ------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| VPC                            |  2 VPC’s1. mgmt-prd-vpc 2. app-prd-vpc                                                                                                            | Launch 2 VPC’s ‘mgmt-prd-vpc’ and ‘app-prd-vpc’ with 2 public subnets in different AZ’s. CIDR:- 10.10.10.0/24 and 10.20.20.0/24, Nr of AZ’s=2                                      |                                                                                                                                                                                                           |
| VPC Peering Connection         | 1. VPC peering connection between 2 VPC’s so that the Management server and Web server can talk to each other via private ip’s                    | Provide Region, Requester/ Accepter name ( VPC names), CIDR blocks                                                                                                       |                                                                                                                                                                                                           |
| AMI ( Amazon Machine Image )   | 1. Amazon machine image configuration is needed for launching EC2 instances.                                                                      | Generation = Amazon Linux 2; Edition = Standard; Virtualization =HVM; Storage = General Purpose                                                                                |                                                                                                                                                                                                           |
| EC2Web Server                  | 1. Web server must be installed in an automated manner in app-prd-vpc.2. Storage should be encrypted.                                             | 1. Provide Encrypted Storage;  2.  Allow all inbound traffic for port 443, 80;  Allow inbound traffic from mgmt_server for port 22.   User Data for web server launch    | User Data script in S3? \#!/bin/bash  yum -y install httpd systemctl enable httpd systemctl start httpd echo '&lt;html>&lt;h1>Hello From Your Web Server!&lt;/h1>&lt;/html>' > /var/www/html/index.html          |
| EC2Management Server           | 1. The admin/management server must be reachable with a public IP. 2. The admin/management server should only be reachable from trusted locations | Provide Encrypted Storage; Security group-: Allow inbound traffic from mgmt_server for port 22 from Trusted IP’s.                                                            |                                                                                                                                                                                                           |
| Secret Manager                 | 1. EC2 instance key pairs will be stored in Secret Manager                                                                                        | Both public and Private keys will be stored . By default only Private keys get stored. Set Store_Public_Key = True                                                       |                                                                                                                                                                                                           |
| KMS ( Key Management Service ) | 1. Encrypted storage (EBS, S3) keys are stored in KMS.                                                                                            |                                                                                                                                                                          |                                                                                                                                                                                                           |
| AWS Backup Service             | 1. The web server must be backed up daily. 2. The backups must be kept for 7 days.                                                                |                                                                                                                                                                          | Uses S3 for backups?                                                                                                                                                                                      |
| S3 storage                     | 1. For post deployment scripts.                                                                                                                   | Encrypted storage                                                                                                                                                        |                                                                                                                                                                                                           |
| IAM                            | 1. Create Role for EC2 instance                                                                                                                   |    With Managed policy "AWSSSMFull Access"                                                                                                                                                                      |                                                                                                                                                                                                           |






### **Security Group (Web Server AutoScaling Group )**



| Type  | Protocol | Port Range | Source                         | Description        |
| ----- | -------- | ---------- | ------------------------------ | ------------------ |
| SSH   | TCP      | 22         | Management Server Security Grp | Admin Access       |
| HTTP  | TCP      | 80         |ELB Security Grp                      | Web Traffic        |
|  |       |         |                     |   |

### **Security Group Load Balancer**



| Type  | Protocol | Port Range | Source                         | Description        |
| ----- | -------- | ---------- | ------------------------------ | ------------------ |
| HTTPS   | TCP      | 443       |0.0.0.0/0      | Web Traffic
| HTTP  | TCP      | 80         |0.0.0.0/0                     | Web Traffic        |
|  |       |         |                     |   |



### **Security Group Management Server**

  


| Type | Protocol | Port Range | Source | Description  |
| ---- | -------- | ---------- | ------ | ------------ |
| SSH  | TCP      | 22         | myIp   | Admin Access |



### **VPC Route Table Entry:**
****app-prd-vpc****  
| Destination   | Target                        |
| ------------- | ----------------------------- |
| 10.10.10.0/24 | Local                         |
| 10.20.20.0/24 | VPC peering Id ( pcx- \*\*\*) |



****prd-prd-vpc****  
| Destination   | Target                        |
| ------------- | ----------------------------- |
| 10.20.20.0/24 | Local                         |
| 10.10.10.0/24 | VPC peering Id ( pcx- \*\*\*) |




     
### **AWS Backup Plan:**

     


   |                          | Backup Plan 1 ( Web server)                                                                  | Backup Plan 2 (Management Server )                                                           |
   | ------------------------ | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- |
   | Vault                    | Web_Vault                                                                                    | Mgmt_Vault                                                                                   |
   | Resource Selection       | EC2 instance                                                                                 | EC2 instance                                                                                 |
   | Rule                     | cron(hour="11" ,minute="35",day="\*",month="\*",year="\*"),delete_after=Duration.days(7),    | cron(hour="11" ,minute="35",day="\*",month="\*",year="\*"),delete_after=Duration.days(7),    |
   | Start /Completion window | completion_window=Duration.hours(2),start_window=Duration.hours(1)                           | completion_window=Duration.hours(2),start_window=Duration.hours(1)                           |  
