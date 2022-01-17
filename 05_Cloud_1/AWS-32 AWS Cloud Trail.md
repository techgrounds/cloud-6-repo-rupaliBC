# AWS Cloud Trail
AWS CloudTrail is an AWS service that helps you enable governance, compliance, and operational and risk auditing of your AWS account. Actions taken by a user, role, or an AWS service are recorded as events in CloudTrail.

CloudTrail is enabled by default for your AWS account. You can use Event history in the CloudTrail console to view, search, download, archive, analyze, and respond to account activity across your AWS infrastructure. 

 A trail enables CloudTrail to deliver log files to an Amazon S3 bucket. By default, when you create a trail in the console, the trail applies to all AWS Regions. The trail logs events from all Regions in the AWS partition and delivers the log files to the Amazon S3 bucket that you specify. Additionally, you can configure other AWS services to further analyze and act upon the event data collected in CloudTrail logs.

## Key-terms
- Trails: 
A trail is a configuration that enables delivery of CloudTrail events to an Amazon S3 bucket, CloudWatch Logs, and CloudWatch Events.
- Organization trails : 
An organization trail is a configuration that enables delivery of CloudTrail events in the management account and all member accounts in an AWS Organizations organization to the same Amazon S3 bucket, CloudWatch Logs, and CloudWatch Events.
- Management events :
Management events provide information about management operations that are performed on resources in your AWS account.
- CloudTrail events :
An event in CloudTrail is the record of an activity in an AWS account. This activity can be an action taken by a user, role, or service that is monitorable by CloudTrail. CloudTrail events provide a history of both API and non-API account activity made through the AWS Management Console, AWS SDKs, command line tools, and other AWS services.
- Data events : 
Data events provide information about the resource operations performed on or in a resource.
-  Insights events : 
CloudTrail Insights events capture unusual API call rate or error rate activity in your AWS account. If you have Insights events enabled, and CloudTrail detects unusual activity, Insights events are logged to a different folder or prefix in the destination S3 bucket for your trail.
## Opdracht
Bestudeer:

- AWS Cloud Trail

### Gebruikte bronnen
- https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html
- https://www.youtube.com/watch?v=LZgIRNED7N4
### Ervaren problemen

### Resultaat
