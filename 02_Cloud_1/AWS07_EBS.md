# AWS EBS
EBS can be seen as virtual hard drives in the cloud. They can be either root volumes (like an internal hard disk), or seperate volumes (like an external hard disk). One instance of an EBS is called a volume. One volume can be attached to only one EC2 instance at a time, although for every non-root volume, you can detach it and attach it to a different EC2 instance.
You can create snapshots of a volume to create backups or new identical volumes. These snapshots will be stored in S3.For security, EBS volumes can be encrypted. Volumes can be scaled up, but not down.
- Types of EBS Volumes
  Amazon EBS volume types are broken into two main categories: 
- SSD-backed volumes are optimized for IOPS, which are best for workloads involving frequent read/write operations with small I/O size.
- HDD-backed volumes are optimized for throughput (measured in MiB/s) for large streaming workloads. Cannot include boot volumes.
  Within each of those groups are two options. The default type is General Purpose SSD (gp2), and there are 3 others available:
    - General Purpose SSD (gp2) – general purpose, balances price and performance.
      Use cases: Most workloads such as virtual desktops, dev and test environments, and low-latency interactive apps.
    - Provisioned IOPS SSD (io1) – highest-performance SSD volume for mission-critical low-latency or high-throughput workloads that require sustained IOPS performance, or more than 16,000 IOPS or 250 MiB/s of throughout per volume.
       Use cases: Mission-critical applications, large database workloads such as MongoDB, Microsoft SQL Server, Cassandra, Oracle, MySQL, and PostgreSQL
    - Throughput Optimized HDD (st1) – low-cost HDD volume for frequently accessed workloads with high throughput.
      Use cases: Streaming workloads, big data, data warehouses, log processing.
    - Cold HDD (sc1) – lowest cost HDD volume for less-frequently accessed workloads
      Use cases: Throughput-oriented storage for large volumes of data that is infrequently accessed


## Key-terms
- IOPS 
- Throughput
- Persistent storage
- Resiliency
- High reliability

## Opdracht
### Exercise 1:
   - Start your sandbox lab and open the AWS console.
   - Navigate to the EC2 menu.
   - Create a t2.micro Amazon Linux 2 machine with all the default settings (the key can be downloaded from the sandbox lab)
   - Create a new EBS volume with the following requirements:
      Volume type: General Purpose SSD (gp2)
      Size: 1 GiB
      Availability Zone: same as your EC2
      Wait for its state to be available.

### Exercise 2:
   - Attach your new EBS volume to your EC2 instance.
   - Connect to your EC2 instance using SSH.
   - Mount the EBS volume on your instance.
   - Create a text file and write it to the mounted EBS volume.

### Exercise 3:
  - Create a snapshot of your EBS volume.
  - Remove the text file from your original EBS volume.
  - Create a new volume using your snapshot.
  - Detach your original EBS volume.
  - Attach the new volume to your EC2 and mount it.
  - Find your text file on the new EBS volume.

### Gebruikte bronnen
- https://www.parkmycloud.com/blog/ebs-volume-types/
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html
- https://aws.amazon.com/ebs/
- https://www.youtube.com/watch?v=N9t2RzmHta8&amp;t=171s
- https://www.youtube.com/watch?v=6h13JGeiE2Y
### Ervaren problemen
After launching EC2 instance, I could not connect to EC2 instance so then I have to create Internet Gateway and allow traffic. For that I have to create Route Table 

### Resultaat

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/s3cat.png)

