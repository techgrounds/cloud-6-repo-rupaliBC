# EFS
Amazon Elastic File System (Amazon EFS) is a simple, serverless, set-and-forget, elastic file system. There is no minimum fee or setup charge. You pay only for the storage you use, for read and write access to data stored in Infrequent Access storage classes, and for any provisioned throughput.

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