# Lambda

AWS Lambda is a serverless computing service provided by Amazon Web Services (AWS). Users of AWS Lambda create functions, self-contained applications written in one of the supported languages and runtimes, and upload them to AWS Lambda, which executes those functions in an efficient and flexible manner.

## Key-terms
- Function: 
A function is a resource that you can invoke to run your code in Lambda. A function has code to process the events that you pass into the function or that other AWS services send to the function.

- Trigger : 
A trigger is a resource or configuration that invokes a Lambda function.

- Event : 
An event is a JSON-formatted document that contains data for a Lambda function to process. The runtime converts the event to an object and passes it to your function code. When you invoke a function, you determine the structure and contents of the event.

- Execution environment : 
An execution environment provides a secure and isolated runtime environment for your Lambda function.

- Runtime : 
The runtime provides a language-specific environment that runs in an execution environment.

## Opdracht
We will create a sample Lambda function to be triggered on an S3 Object upload event. The lambda function will make a copy of that object and place it in a different s3 bucket.
- Log in to the AWS Management Console.
- Create two S3 buckets. One for the source and one for the destination.
- Create a Lambda function to copy the object from one bucket to another bucket.
- Test the Lambda Function.

### Gebruikte bronnen

- https://docs.aws.amazon.com/lambda/
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


#### JSon Policy 

```
{ 
   "Version":"2012-10-17",
   "Statement":[ 
      { 
         "Effect":"Allow",
         "Action":[ 
            "s3:GetObject"
         ],
         "Resource":[ 
            "arn:aws:s3:::your_source_bucket_name/*"
         ]
      },
      { 
         "Effect":"Allow",
         "Action":[ 
            "s3:PutObject"
         ],
         "Resource":[ 
            "arn:aws:s3:::your_destination_bucket_name/*"
         ]
      }
   ]
}
```
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