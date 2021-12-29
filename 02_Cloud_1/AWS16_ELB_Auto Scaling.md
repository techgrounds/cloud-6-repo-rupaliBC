# AWS ELB Auto Scaling
Elastic Load Balancing automatically distributes incoming application traffic across multiple Amazon EC2 instances. It enables you to achieve greater levels of fault tolerance in your applications, seamlessly providing the required amount of load balancing capacity needed to distribute application traffic. Elastic Load Balancing detects unhealthy instances and automatically reroutes traffic to healthy instances until the unhealthy instances have been restored.
- Application Load Balancer -
Application Load Balancer is best suited for load balancing of HTTP and HTTPS traffic and provides advanced request routing targeted at the delivery of modern application architectures
- Network Load Balancer - 
Network Load Balancer is best suited for load balancing of Transmission Control Protocol (TCP), User Datagram Protocol (UDP), and Transport Layer Security (TLS) traffic where extreme performance is required. 

## Key-terms
- AMI -An Amazon Machine Image (AMI) provides the information required to launch an instance. You must specify an AMI when you launch an instance. You can launch multiple instances from a single AMI when you need multiple instances with the same configuration. You can use different AMIs to launch instances when you need instances with different configurations.
- Auto Scaling - Amazon EC2 Auto Scaling helps you ensure that you have the correct number of Amazon EC2 instances available to handle the load for your application.

## Opdracht
### Exercise 1
- Launch an EC2 instance with the following requirements:
- Region: Frankfurt (eu-central-1)
- AMI: Amazon Linux 2
- Type: t3.micro
- User data:
- #!/bin/bash
-# Install Apache Web Server and PHP
- yum install -y httpd mysql php
-# Download Lab files
- wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/80-lab-vpc-web-server/lab-app.zip
- unzip lab-app.zip -d /var/www/html/
-# Turn on web server
- chkconfig httpd on
- service httpd start
- Security Group: Allow HTTP
- Wait for the status checks to pass.
- Create an AMI from your instance with the following requirements:
- Image name: Web server AMI

### Exercise 2

- Create an application load balancer with the following requirements:
- Name: LabELB
- Listener: HTTP on port 80
- AZs: eu-central-1a and eu-central-1b
- Subnets: must be public
- Security Group: 
- Name: ELB SG
- Rules: allow HTTP access
- Target Group:
- Name: LabTargetGroup
- Targets: to be registered by Auto Scaling

### Exercise 3
- Create a launch configuration for the Auto Scaling group. It has to be identical to the server that is currently running.
- Create an auto scaling group with the following requirements:
- Name: Lab ASG
- Launch Configuration: Web server launch configuration
- Subnets: must be in eu-central-1a and eu-central-1b
- Load Balancer: LabELB
- Group metrics collection in CloudWatch must be enabled
- Group Size:
- Desired Capacity: 2
- Minimum Capacity: 2
- Maximum Capacity: 4
- Scaling policy: Target tracking with a target of 60% average CPU utilisation
### Exercise 4:
- Verify that the EC2 instances are online and that they are part of the target group for the load balancer.
- Access the server via the ELB by using the DNS name of the ELB.
- Perform a load test on your server(s) using the website on your server to activate auto scaling. There might be a delay on the creation of new servers in your fleet, depending on the settings on your Auto Scaling Group.

### Gebruikte bronnen
https://aws.amazon.com/elasticloadbalancing/

https://www.amazonaws.cn/en/elasticloadbalancing/

https://www.youtube.com/watch?v=qpHLRc4Qt1E

### Ervaren problemen


### Resultaat

## Launcing an EC2 instance:

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/ELB1.png)

## Creating AMI

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/ELB3.png)

## Load Balancer 
- 
![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/ELB4.png)

## Auto Scaling

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/ELB2.png)


![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/ELB5.png)

## Load Test
![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/ELB6.png)
