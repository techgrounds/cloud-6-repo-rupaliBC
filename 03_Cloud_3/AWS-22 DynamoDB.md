# DynamoDB
DynamoDB is a fast and flexible NoSQL database designed for applications that need consistent, single-digit millisecond latency at any scale.it is a fully managed database It has a very flexible data model. This means that you don't need to define your database schema upfront. It also has reliable performance.

DynamoDB is a good fit for mobile gaming, ad-tech, IoT and many other applications.

DynamoDB Tables
DynamoDB tables consist of 
- Items (Think of a row of data in a table).
- Attributes ((Think of a column of data in a table).

Supports key-value and document data structures.
Key= the name of the data.  Value= the data itself.

DynamoDB- Primary Keys

DynamoDB stores and retrieves data based on a Primary key
DynamoDB also uses Partition keys to determine the physical location data is stored.

If you are using a partition key as your Primary key, then no items will have the same Partition key.
Composite Keys (Partition Key + Sort Key) can be used in Combination.

Two items may have the same partition key, but must have a different sort key.

All items with the same partition key are stored together and then sorted according to the sort key value.

DynamoDB allows you to store multiple items with the same partition keys.
## Key-terms

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

### Ervaren problemen

### Resultaat
Create Table with 5 items with attributes Order Nr., Product Nr, Product Name and Price ( in $ )

 ![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/dynamo1.png)

 Scan the table with with Attribute Price > 100 
 
 ![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/dynamo2.png)

 Result of the above scan:
 
 ![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/dynamo3.png)
 
 Query the table with Order Nr 1002

 ![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/dynamo6.png)
 
 Result of the abov query :

 ![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/dynamo5.png)
 
