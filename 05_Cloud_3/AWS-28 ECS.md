# Elastic Container Service
Amazon Elastic Container Service (Amazon ECS) is a highly scalable, fast container management service that makes it easy to run, stop, and manage containers on a cluster. Your containers are defined in a task definition that you use to run individual tasks or tasks within a service. In this context, a service is a configuration that enables you to run and maintain a specified number of tasks simultaneously in a cluster. You can run your tasks and services on a serverless infrastructure that is managed by AWS Fargate. Alternatively, for more control over your infrastructure, you can run your tasks and services on a cluster of Amazon EC2 instances that you manage.

## Key-terms
- ECS : 
 In ECS we will create a task and run that task to deploy our Docker image to a container. ECS also handles the scaling of applications that need multiple instances running. ECS Manages the deployment of our application. Learn more.
- ECR : 
ECR is versioned storage for Docker images on AWS. ECS pulls images from ECR when deploying. 
- Fargate : 
Fargate provisions and manages clusters of EC2 instances.
You don’t have to provision or manage the EC2 instances your application runs on.
You are only charged for the time your app is running. In the case of an application that runs a periodic task and exits this can save a lot of money.
- Task definitions : 
 The task definition is a text file (in JSON format) that describes one or more containers (up to a maximum of ten) that form your application. The task definition can be thought of as a blueprint for your application. It specifies various parameters for your application. 
 - Tasks : 
A task is the instantiation of a task definition within a cluster. After you have created a task definition for your application within Amazon ECS, you can specify the number of tasks to run on your cluster.
- Clusters : 
An Amazon ECS cluster is a logical grouping of tasks or services. You can register one or more Amazon EC2 instances (also referred to as container instances) with your cluster to run tasks on them. Or, you can use the serverless infrastructure that Fargate provides to run tasks. When your tasks are run on Fargate, your cluster resources are also managed by Fargate.
- Container agent
The container agent runs on each container instance within an Amazon ECS cluster. The agent sends information about the resource's current running tasks and resource utilization to Amazon ECS. It starts and stops tasks whenever it receives a request from Amazon ECS.
## Opdracht
Bestudeer:

- ECS
### Gebruikte bronnen
- https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html
- https://www.youtube.com/watch?v=peF03zwYzhk
- https://www.youtube.com/watch?v=I9VAMGEjW-Q

### Ervaren problemen

### Resultaat
