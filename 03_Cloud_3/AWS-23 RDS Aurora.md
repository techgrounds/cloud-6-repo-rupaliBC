# Relational Database Service (Aurora)
Amazon Relational Database Service (Amazon RDS) makes it easy to set up, operate, and scale a relational database in the cloud. It provides cost-efficient and resizable capacity while automating time-consuming administration tasks, such as hardware provisioning, database setup, patching, and backups
Amazon Aurora is a MySQL and PostgreSQL-compatible relational database built for the cloud that combines the performance and availability of traditional enterprise databases with the simplicity and cost-effectiveness of open source databases.

Amazon Aurora is up to five times faster than standard MySQL databases and three times faster than standard PostgreSQL databases. It provides the security, availability, and reliability of commercial databases at 1/10th the cost. Amazon Aurora is fully managed by Amazon Relational Database Service (RDS), which automates time-consuming administration tasks like hardware provisioning, database setup, patching, and backups.

Amazon Aurora features a distributed, fault-tolerant, self-healing storage system that auto-scales up to 128TB per database instance. It delivers high performance and availability with up to 15 low-latency read replicas, point-in-time recovery, continuous backup to Amazon S3, and replication across three Availability Zones.
## Key-terms

## Opdracht
- Create the DB cluster
- Retrieve the DB cluster endpoints
- Assign an IAM role to the DB cluster
- Create a replica auto scaling policy
- Create an AWS Secrets Manager secret
- Configure your Cloud9 desktop
- Verify DB cluster
- Connect to the DB Cluster
### Gebruikte bronnen
https://awsauroralabsmy.com/provisioned/create/

### Ervaren problemen

### Resultaat
#### There are two endpoints created by default. The Cluster Endpoint will always point to the writer DB instance of the cluster, and should be used for both writes and reads. The Reader Endpoint will always resolve to one of the reader DB instances and should be used to offload read operations to read replicas. In the RDS console, go to the DB cluster detail view by clicking on the cluster DB identifier.

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/aurora11.png)

#### The Endpoints section in the Connectivity and security tab of the details page displays the endpoints:

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/aurora2.png)

#### Assign an IAM role to the DB cluster, in order to allow the cluster access to Amazon S3 for importing and exporting data:
![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/aurora3.png)

#### Create an AWS Secrets Manager secret:

#### Configure your cloud9 desktop: 
run the command below, replacing the [secretArn] placeholder with the ARN of the secret created :: 

CREDS=`aws secretsmanager get-secret-value --secret-id [secretArn] | jq -r '.SecretString'`
export DBUSER="`echo $CREDS | jq -r '.username'`"
export DBPASS="`echo $CREDS | jq -r '.password'`"
echo "export DBPASS=\"$DBPASS\"" >> /home/ec2-user/.bashrc
echo "export DBUSER=$DBUSER" >> /home/ec2-user/.bashrc
#### Verify your DB cluster
echo $DBUSER
###### Connect to the DB Cluster
- mysql -h[clusterEndpoint] -u$DBUSER -p"$DBPASS" mylab

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/aurora4.png)