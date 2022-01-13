# Lambda

## Key-terms

## Opdracht
We will create a sample Lambda function to be triggered on an S3 Object upload event. The lambda function will make a copy of that object and place it in a different s3 bucket.
- Log in to the AWS Management Console.
- Create two S3 buckets. One for the source and one for the destination.
- Create a Lambda function to copy the object from one bucket to another bucket.
- Test the Lambda Function.

### Gebruikte bronnen

- https://zacks.one/aws-lambda-lab/?highlight=lam

### Ervaren problemen

### Resultaat
#### Create Amazon S3 Source Bucket :

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/lamb1.png)

#### Create Amazon S3 Destination Bucket :

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/lamb2.png)

#### Create an IAM Policy :

- As a pre-requisite for creating the Lambda function, we need to create a user role with a custom policy.

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/lamb3.png)

#### IAM Role: 

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/lamb4.png)


#### Create a Lambda Function :
![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/lamb5.png)


#### Adding Triggers to Lambda Function :

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/lamb6.png)

#### we need to write a NodeJs function which copies the object from the source bucket and paste it into the destination bucket.

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/lamb7.png)


#### You can see a copy of your uploaded source bucket image in the destination bucket.

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/lambl.png)