# AWS Global Infrastructure
AWS has a global infrastructure made up of the following components:
- Regions
- Availability Zones
- Edge Locations


## Key-terms
An Availability Zone (AZ)- AZ is one or more discrete data centers with redundant power, networking, and connectivity in an AWS Region. 

Region -AWS has the concept of a Region, which is a physical location around the world where we cluster data centers. 

Edge Location - An Edge location is basically a small setup in different locations that provides low latency connectivity by providing static contents to be available from nearest location of the request.
What happens is that instead of getting the information from the source it just routes to the nearest edge location and delivers the information reducing the latency. 



## Opdracht

- What is an AWS Availability Zone?
- What is a Region?
- What is an Edge Location?
- Why would you choose one region over another? (e.g. eu-central-1 (Frankfurt) over us-west-2 (Oregon)).


### Gebruikte bronnen
- https://aws.amazon.com/about-aws/global-infrastructure/regions_az/
- https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html
- https://betterprogramming.pub/5-things-to-consider-when-choosing-your-aws-region-484e800cb6f0
- https://www.lastweekinaws.com/blog/what-is-an-edge-location-in-aws-a-simple-explanation/
- 

### Ervaren problemen
.

### Resultaat
### Availability zones 
(AZs) are isolated locations within data center regions from which public cloud services originate and operate. 
### Regions 
Regions are geographic locations in which public cloud service providers' data centers reside.
### Edge Location
An edge location is where end users access services located at AWS. They are located in most of the major cities around the world and are specifically used by CloudFront (CDN) to distribute content to end user to reduce latency. 
### Why would you choose one region over another?

Five important factors that you must consider when choosing an AWS region and availability zones for new services.
1. Available services 

New services that are made available on AWS are not always supported in all regions. Usually, it takes AWS some time to make a new feature available in all regions. Therefore, sometimes you must use specific regions just because they are the only ones supporting the service you wish to launch. 

2. Geographic location 

If you are launching an application that targets people located in a specific geographic location, it doesn’t make a lot of sense to choose a region that is far away from it, as this is going to increase latency. Therefore, you should pick a region that is close to the location of the vast majority of users. Obviously, for large-scale applications, you would need to launch your service(s) in multiple regions to keep latency low. 

3. Compliance and regulations 

Usually, companies have to meet certain legal requirements. For instance, you may wish to keep the data in the country the application is deployed in. Sometimes this is essentially the only factor considered when choosing AWS regions. If you are obligated by law to host your data or application in a specific country or continent, then no other factor can outweigh this one. 

4. Availability and fault tolerance 

Apart from choosing an AWS region, you may also have to consider choosing a specific availability zone(s) to host your applications. AZs let you run highly available and scalable services. 

For instance, let’s assume we want to launch a Kafka service. If the broker’s Kafka clusters are distributed across the availability zones of the AWS region we chose, the service would be able to survive disasters such as power outages and natural disasters. 

5. Pricing 

Finally, the same service may have different pricing from region to region. Sometimes it makes sense to pick the cheapest region — especially if it is close enough to your preferred region that is more expensive. 
