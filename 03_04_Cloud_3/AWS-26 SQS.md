# Simple Queue Service
Amazon Simple Queue Service (Amazon SQS) offers a secure, durable, and available hosted queue that lets you integrate and decouple distributed software systems and components.
## Key-terms
- Short Polling : With short polling, the ReceiveMessage request queries only a subset of the servers (based on a weighted random distribution) to find messages that are available to include in the response. Amazon SQS sends the response right away, even if the query found no messages.
- Long Polling: 
With long polling, the ReceiveMessage request queries all of the servers for messages. Amazon SQS sends a response after it collects at least one available message, up to the maximum number of messages specified in the request. Amazon SQS sends an empty response only if the polling wait time expires.
- Dead-letter queue : A dead-letter queue is a queue that one or more source queues can use for messages that are not consumed successfully. 
- visibility TimeOut : To prevent other consumers from processing the message again, Amazon SQS sets a visibility timeout, a period of time during which Amazon SQS prevents other consumers from receiving and processing the message. The default visibility timeout for a message is 30 seconds. The minimum is 0 seconds. The maximum is 12 hours.  
- InFlight messages : A message is considered to be in flight after it is received from a queue by a consumer, but not yet deleted from the queue

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