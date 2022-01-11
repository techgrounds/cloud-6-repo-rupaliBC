# DynamoDB
Amazon DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. DynamoDB lets you offload the administrative burdens of operating and scaling a distributed database so that you don't have to worry about hardware provisioning, setup and configuration, replication, software patching, or cluster scaling. DynamoDB also offers encryption at rest, which eliminates the operational burden and complexity involved in protecting sensitive data. 

With DynamoDB, you can create database tables that can store and retrieve any amount of data and serve any level of request traffic. You can scale up or scale down your tables' throughput capacity without downtime or performance degradation.
DynamoDB is a good fit for mobile gaming, ad-tech, IoT and many other applications.


## Key-terms
- Items - A row of data in a table
- Attributes - A column of data in a table.
- Partition key – A simple primary key, composed of one attribute known as the partition key. DynamoDB uses the partition key's value as input to an internal hash function. 
- Composite key - In database design, a composite key is a candidate key that consists of two or more attributes (table columns) that together uniquely identify an entity occurrence (table row)
- Read Capacity Unit (RCU): A read capacity unit represents one strongly consistent read per second, or two eventually consistent reads per second, for an item up to 4 KB in size.
- Write Capacity Unit (WCU) : In case of write capacity the number is 1 KB. That is each write that is 1KB or less will use 1 write capacity and writes that are more than 1 KB in size will be rounded off to the next 1 KB. 

## Opdracht


Create a NoSQL table Sales Information. It should contain Order Nr ( Partition Key) , Product Nr, Product Name and Price ( in $ )
- Choose Provisioned Capacity Mode
- Auto Scaling off 
- Read Capacity Unit = 5 , Write Capacity Unit = 5
- The partition key should be set.
- You should be able to sort by Order Number
- Add at least five items to the table.
- Scan the table to search for all the Products with Price > 100 .
- A query to find one specific Order Number in the table.

### Gebruikte bronnen

- https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html
- https://www.youtube.com/watch?v=dOTUl2mZNVQ
- https://play.whizlabs.com/site/task_details?lab_type=1&task_id=13&quest_id=37
- https://www.dynamodbguide.com/inserting-retrieving-items
### Ervaren problemen

### Resultaat
Create Table with 5 items with attributes Order Nr., Product Nr, Product Name and Price ( in $ ) :

 ![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/dynamo1.png)

 Scan the table with with Attribute Price > 200 
 
 ![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/dynamo2.png)

 Result of the above scan:
 
 ![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/dynamo3.png)
 
 Query the table with Order Nr 1002 :

 ![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/dynamo6.png)
 
 Result of the abov query :

 ![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/dynamo5.png)
 
