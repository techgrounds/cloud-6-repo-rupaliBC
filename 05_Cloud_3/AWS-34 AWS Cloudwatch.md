# AWS Cloudwatch
Amazon CloudWatch monitors your Amazon Web Services (AWS) resources and the applications you run on AWS in real time. You can use CloudWatch to collect and track metrics, which are variables you can measure for your resources and applications.

The CloudWatch home page automatically displays metrics about every AWS service you use. You can additionally create custom dashboards to display metrics about your custom applications, and display custom collections of metrics that you choose.
## Key-terms
- Metrics: 
Metrics are the fundamental concept in CloudWatch. A metric represents a time-ordered set of data points that are published to CloudWatch. Think of a metric as a variable to monitor, and the data points as representing the values of that variable over time. For example, the CPU usage of a particular EC2 instance is one metric provided by Amazon EC2. 
- Dimensions
A dimension is a name/value pair that is part of the identity of a metric. You can assign up to 10 dimensions to a metric.
Every metric has specific characteristics that describe it, and you can think of dimensions as categories for those characteristics. Dimensions help you design a structure for your statistics plan. Because dimensions are part of the unique identifier for a metric, whenever you add a unique name/value pair to one of your metrics, you are creating a new variation of that metric.

## Opdracht
- Launch an EC2 instance. Add EC2 Monitoring dashboard
- Set an alarm for EC2 low CPU utilization (threshold: CPU utilization <1 )
- Add the alarm created to the dashboard

### Gebruikte bronnen
- https://www.youtube.com/watch?v=mcV1idfCXOo
- https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html
### Ervaren problemen

### Resultaat
### - EC2 Monitoring Dashboard:

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/cwatch111.png)

### - Alarm set for an EC2 ( Low CPU Utilization): 

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/cwatch3.png)

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/cwatch11.png)

### - Dashboard for Low CPU Utilization alarm:

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/cwatch2.png)


