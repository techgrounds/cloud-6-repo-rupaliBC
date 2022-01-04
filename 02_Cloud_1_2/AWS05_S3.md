# AWS S3 Storage
AWS offers object based storage in the form of S3. S3 makes use of buckets as a container for objects. A single object in S3 has a maximum size of 5TB. However, the total size of a bucket is virtually unlimited.
Bucket names must be globally unique. That is, even other AWS accounts in different regions cannot share the same bucket name. Buckets, and objects within buckets, can be accessed using a URL.
The bucket policy acts as an access control list. Data can be encrypted for even further protection.
Objects are automatically replicated within a region, so that there’s always at least three copies available. This redundancy greatly increases the availability and durability of objects stored in S3.

## Key-terms
Storage classes:
  - S3 Standard
  - S3 Standard-IA
  - S3 One-zone IA
  - S3 Glacier


## Opdracht
### Exercise 1
- Start your sandbox lab and open the AWS console.
- Navigate to the S3 menu.
- Create new bucket with the following requirements:
- Region: Frankfurt (eu-central-1)
- Public access enabled
- Upload a cat picture to your bucket.
- Share the object URL of your cat picture with a peer. Make sure they are able to see the picture.
### Exercise 2
- Create new bucket with the following requirements
- Region: Frankfurt (eu-central-1)
- Public access enabled
- Upload the four files that make up AWS’ demo website.
- Enable static website hosting.
- Share the bucket website endpoint with a peer. Make sure they are able to see the website.

- 

### Gebruikte bronnen
- https://aws.amazon.com/s3/
- https://aws.amazon.com/s3/storage-classes/?nc=sn&loc=3
- https://www.backblaze.com/blog/cloud-storage-durability-vs-availability/
- https://wellarchitectedlabs.com/common/documentation/createnews3bucketandaddobjects/

### Ervaren problemen
.

### Resultaat
https://rupalibucket123.s3.eu-central-1.amazonaws.com/cat.png

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/s3cat.png)

http://bucket.for.static.website.s3-website.eu-central-1.amazonaws.com

![alt_text](https://github.com/techgrounds/cloud-6-repo-rupaliBC/blob/main/00_includes/staticwebsite.png)
