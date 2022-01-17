# EFS
Amazon Elastic File System (Amazon EFS) is a simple, serverless, set-and-forget, elastic file system. There is no minimum fee or setup charge. You pay only for the storage you use, for read and write access to data stored in Infrequent Access storage classes, and for any provisioned throughput.

- Features:

- Fully managed

Amazon EFS is a fully managed service providing NFS shared file system storage for Linux workloads. EFS makes it simple to create and configure file systems.

- Highly available and durable

Amazon EFS is designed to be highly available and is designed for 99.999999999% (11 nines) durability. By default, every EFS file system object (such as directory, file, and link) is redundantly stored across multiple Availability Zones (AZs) for file systems using Standard storage classes.

- Scalable performance

Amazon EFS is designed to provide the throughput, IOPS, and low latency needed for a broad range of workloads. Throughput and IOPS scale as a file system grows and can burst to higher throughput levels for short periods of time to support the unpredictable performance needs of file workloads. 

- Elastic and scalable

With Amazon EFS, storage capacity is elastic, growing and shrinking automatically as you add and remove files, dynamically providing the storage capacity to applications as they need it. Since capacity is elastic, no provisioning is necessary, and you’ll be billed only for what you use. Amazon EFS is designed to be highly scalable both in storage capacity and in throughput performance. It can grow to petabyte scale and allows massively parallel access from Amazon EC2 instances to your data. 
## Key-terms


## Opdracht
- Launch an EC2 instance - Amazon Linux 2, t2.micro EC2 instance 
- Create an EFS filesystem.
- Mount the filesystem to your EC2 instance.
- Create 3 text files in this filesystem.
- Launch a second EC2 instance with the same specifications as the first.
- Mount the same EFS filesystem to the second EC2 instance.
- Locate all 3 files you created on your second instance.
### Gebruikte bronnen
- https://aws.amazon.com/efs/
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AmazonEFS.html#quick-create
### Ervaren problemen

### Resultaat
#### File System Created :
![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/EFS5.png)

##### Mounting FileSystem on to EC2 instructons:

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/EFS6.png)

#### Mounting File System on first EC2 instance and then creating files

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/EFS3.png)
#### Mounting File System on second EC2 instance and then locating files created from first EC2 instance: 
![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/EFS2.png)