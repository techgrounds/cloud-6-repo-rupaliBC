# AWS VPC
Amazon VPC is typically described as a virtual private data center in the cloud. It is a virtual network that is logically isolated from other VPCs.
With a VPC you have full control over the design of the network. You can create subnets, internet gateways (igw), NAT gateways, VPN connections, and more.

There is always a default VPC when you create a new AWS account, but you can add up to 5 non-default VPCs per region per account. This is a soft limit. That is, you can request the limit to be raised.
Many services, like EC2, RDS and ECS require a VPC to be placed into.
When you create a VPC, you must assign a CIDR block. Choose your CIDR block and subnet mask carefully, as they have to allow for enough subnets and hosts and cannot be changed after creation.

Subnets can be either public or private. The only difference is that private subnets do not have an entry for the internet gateway (igw) in their route table, where public subnets do. In other words, private subnets cannot access the internet without a NAT gateway or a NAT instance.
VPCs operate at the regional level, while subnets can only be placed into a single Availability Zone.
Elastic IPs are also available from the VPC menu. EIPs are public IP addresses that can be dynamically allocated to resources like EC2 instances or NAT gateways.

## Key-terms
- NAT gateways - A NAT gateway is a Network Address Translation (NAT) service. You can use a NAT gateway so that instances in a private subnet can connect to services outside your VPC but external services cannot initiate a connection with those instances.
- Elastic IP - An Elastic IP address is a reserved public IP address that you can assign to any EC2 instance in a particular region, until you choose to release it. 
- Internet gateway - An internet gateway is a horizontally scaled, redundant, and highly available VPC component that allows communication between your VPC and the internet.
- Private Subnet - The instances in the private subnet can't. Instead, the instances in the private subnet can access the internet by using a network address translation (NAT) gateway that resides in the public subnet.
- Public Subnet - The instances in the public subnet can send outbound traffic directly to the internet.


## Opdracht
### Exercise 1
Navigate to the VPC menu in your sandbox environment.<br>
Allocate an Elastic IP address to your account.<br>
Use the Launch VPC Wizard option to create a new VPC with the following requirements:<br>
Region: Frankfurt (eu-central-1)<br>
VPC with a public and a private subnet<br>
Name: Lab VPC<br>
CIDR: 10.0.0.0/16<br>
Requirements for the public subnet:<br>
Name: Public subnet 1<br>
CIDR: 10.0.0.0/24 <br>
AZ: eu-central-1a <br>
Requirements for the private subnet: <br>
Name: Private subnet 1 <br>
CIDR: 10.0.1.0/24 <br>
AZ: eu-central-1a <br>

### Exercise 2
Create an additional public subnet with the following requirements: <br>
VPC: Lab VPC <br>
Name: Public Subnet 2 <br>
AZ: eu-central-1b <br>
CIDR: 10.0.2.0/24 <br>
Create an additional private subnet with the following requirements: <br>
VPC: Lab VPC <br>
Name: Private Subnet 2 <br>
AZ: eu-central-1b <br>
CIDR: 10.0.3.0/24 <br>
View the main route table for Lab VPC. It should have an entry for the NAT gateway. Rename this route table to Private Route Table. <br>
Explicitly associate the private route table with your two private subnets. <br>
View the other route table for Lab VPC. It should have an entry for the internet gateway. Rename this route table to Public Route Table. <br>
Explicitly associate the public route table to your two public subnets. <br>

### Exercise 3 <br>
Create a Security Group with the following requirements: <br>
Name: Web SG <br>
Description: Enable HTTP Access <br>
VPC: Lab VPC <br>
Inbound rule: allow HTTP access from anywhere <br>
Outbound rule: Allow all traffic <br>

### Exercise 4
Launch an EC2 instance with the following requirements: <br>
AMI: Amazon Linux 2 <br>
Type: t3.micro <br>
Subnet: Public subnet 2 <br>
Auto-assign Public IP: Enable <br>
User data: <br>
```
#!/bin/bash
# Install Apache Web Server and PHP
yum install -y httpd mysql php
# Download Lab files
wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/80-lab-vpc-web-server/lab-app.zip
unzip lab-app.zip -d /var/www/html/
# Turn on web server
chkconfig httpd on
service httpd start
```
Tag:
Key: Name <br>
Value: Web server <br>
Security Group: Web SG <br>
Key pair: no key pair <br>
Connect to your server using the public IPv4 DNS name.


### Gebruikte bronnen

https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario2.html

https://www.youtube.com/watch?v=g2JOHLHh4rI

https://www.cloudflare.com/learning/cloud/what-is-a-virtual-private-cloud/

https://www.youtube.com/watch?v=b1b6JTYnbjU


### Ervaren problemen


### Resultaat

#### VPC with public and private subnet

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/vpc3.png)

#### Private route table

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/vpc4.png)

#### Launching an EC2 instance

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/vpc1.png)

#### Connecting to server using the IPv4 DNS name

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/vpc2.png)


![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/VPC.png)
