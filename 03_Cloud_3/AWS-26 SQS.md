# Simple Queue Service
Amazon Simple Queue Service (Amazon SQS) offers a secure, durable, and available hosted queue that lets you integrate and decouple distributed software systems and components.
## Key-terms

## Opdracht

- AWS SQS LAB WITH LAMBDA FUNCTION.
AWS SQS Triggers on lambda

### Gebruikte bronnen
- https://aws.amazon.com/sqs/
- https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html
### Ervaren problemen

### Resultaat
#### Created Standard TestQueue and added 2 messages in the queue:

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/sqs1.png)

#### - Create lambda function using BluePrint- SQS-Poller and link to your SQS queue

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/sqs2.png)


#### - Queue Enabled :
![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/sqs3.png)

#### - Lambda funtion used for Trigger:

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/sqs4.png)

#### - Receievd Messages: 

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/sqs6.png)

#### - Messages got removed from the queue after lambda trigger:

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/sqs5.png)