# Identity and Access Management
AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources.
## Key-terms
- Principal
A principal is a person or application that can make a request for an action or operation on an AWS resource. The principal is authenticated as the AWS account root user or an IAM entity to make requests to AWS

- Multi-factor authentication (MFA) : 
You can add two-factor authentication to your account and to individual users for extra security. With MFA you or your users must provide not only a password or access key to work with your account, but also a code from a specially configured device.

- Identity-based policies – Identity-based policies are JSON permissions policy documents that control what actions an identity (users, groups of users, and roles) can perform, on which resources, and under what conditions. 

- Resource-based policies – Resource-based policies are JSON policy documents that you attach to a resource such as an Amazon S3 bucket. These policies grant the specified principal permission to perform specific actions on that resource and defines under what conditions this applies. Resource-based policies are inline policies. There are no managed resource-based policies.

## Opdracht
- Create a s3 bucket for a company where each user can create their own Read and Write data with Multi-Factor authetication. 
- Provide a policy where a user is allowed to read or denied to write an object in s3 bucket.
### Gebruikte bronnen
- https://www.youtube.com/watch?v=GjVFf83dcE8
- https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_identity-management.html#intro-identity-users
### Ervaren problemen

### Resultaat
### - Create a bucket.

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/iam11.png)

### - Policy applied to the bucket :
```` ``` {
    "Version": "2012-10-17",
    "Id": "123",
    "Statement": [
        {
            "Sid": "",
            "Effect": "Deny",
            "Principal": "*",
            "Action": "s3:*",
            "Resource": "arn:aws:s3:::mfabucket11/taxdocuments/*",
            "Condition": {
                "Null": {
                    "aws:MultiFactorAuthAge": "true"
                }
            }
        },
        {
            "Sid": "",
            "Effect": "Allow",
            "Principal": "*",
            "Action": "s3:GetObject",
            "Resource": "arn:aws:s3:::mfabucket11/*"
        }
    ]
}  ``` ````

### - 2 Users created one with assigned MFA device
![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/iam1.png)

### - Barcode to assgin MFA to one of the user:

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/iam2.png)

### - MFA assigned to the user: 

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/iam3.png)

### - While signing in as a MFA User , needed to enter MFA code

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/iam7.png)

### - A User only with assigned MFA could write in the s3 bucket . This is because we have json policy which says only MFA users are allowed to access the bucket for write/read opertions.

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/iam11.png)