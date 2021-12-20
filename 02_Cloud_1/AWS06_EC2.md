# AWS EC2
- Amazon Elastic Compute Cloud (Amazon EC2) is a web service that provides resizable compute capacity in the cloud. It is designed to make web-scale cloud computing easier for developers.
Amazon EC2's simple web service interface allows you to obtain and configure capacity with minimal friction. It provides you with complete control of your computing resources and lets you run on Amazon's proven computing environment. Amazon EC2 reduces the time required to obtain and boot new server instances to minutes, allowing you to quickly scale capacity, both up and down, as your computing requirements change.

- The service with which you can run Virtual Machines in AWS is called EC2. These VMs can be used for anything a regular server is used for. Since they’re located at a remote location, connecting to the machine has to be done via the internet. For a connection to Linux machines, you use the Secure Shell (ssh) protocol. For a connection to Windows machines, you use the Remote Desktop Protocol (RDP).
When creating an EC2 instance, you first need to select an Amazon Machine Image (AMI). An AMI is a blueprint for your machine. It contains a template for the OS among other things.
EC2 can have different sizes, called instance types. Every instance type has a different amount of (virtual)CPUs, memory, and network performance.
For the root volume, an instance can use Elastic Block Store (EBS) or Instance store depending on its type. Instance store is known as ephemeral storage, while EBS is known as persistent storage.

- The price of an EC2 instance depends on the instance type, the AMI, the region it’s in, the number of seconds it’s running, and the type of purchase you make.
    - On demand instances are the most expensive option, but they’re also the most flexible.
    - Reserved instances provide a greater discount depending on how much you pay up front. You can reserve instances only for 1 or 3 years.
    - Spot instances are generally considered the cheapest, but their availability depends on the demand, so they’re not always reliable.

## Key-terms
 - Amazon Machine Image: 
 - 

## Opdracht
### Exercise 1
  - Start your sandbox lab and open the AWS console.
  - Navigate to the EC2 menu.
  - Launch an EC2 instance with the following requirements:
    - AMI: Amazon Linux 2 AMI (HVM), SSD Volume Type
    - Instance type: t2.micro
    - Default network, no preference for subnet
    - Termination protection: enabled
    - User data: <br>
         #!/bin/bash <br> yum -y install httpd <br> systemctl enable httpd <br> systemctl start httpd <br>
         echo '<html><h1>Hello From Your Web Server!</h1></html>' > /var/www/html/index.html
         
    - Root volume: general purpose SSD, Size: 8 GiB
    - New Security Group:
    - Name: Web server SG
    - Rules: Allow SSH, HTTP and HTTPS from anywhere
    - Key Pair: vockey (this can be downloaded from the sandbox lab environment
### Exercise 2
    - Wait for the Status Checks to get out of the initialization stage. When you click the Status Checks tab, you should see that the System reachability and the Instance reachability checks have passed.
    - Find the EC2 system logs. Verify that the HTTP package was installed.

### Exercise 3 
    - Stop your EC2 instance (don’t terminate it).
    - Change the instance type to a t2.small.
    - Change the EBS volume size to 10 GiB.
    - Start your EC2 instance.
    
### Exercise 4
    - Terminate your EC2 instance.



### Gebruikte bronnen


### Ervaren problemen
.

### Resultaat
### Exercise 1
- Status Check tab
  ![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/ec262.png)
- EC2 System logs 
  ![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/ec261.png)
### Exercise 2
![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/ec263.png)


