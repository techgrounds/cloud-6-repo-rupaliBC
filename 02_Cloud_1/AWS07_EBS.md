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


## Opdracht
### Exercise 1:

### Exercise 2:

### Gebruikte bronnen
- https://www.parkmycloud.com/blog/ebs-volume-types/
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volume-types.html

### Ervaren problemen
.

### Resultaat
