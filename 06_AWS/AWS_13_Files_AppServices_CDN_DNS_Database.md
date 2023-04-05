# Files, AppServices, CDN, DNS, Database


## Key terminology

- Elastic Beanstalk
- CloudFront
- Route53
- Amazon Elastic File System (Amazon EFS) is a simple, serverless, set-and-forget, elastic file system. There is no minimum fee or setup charge. You pay only for the storage you use, for read and write access to data stored in Infrequent Access storage classes, and for any provisioned throughput.

- Amazon Relational Database Service (Amazon RDS) is a collection of managed services that makes it simple to set up, operate, and scale databases in the cloud.

- Amazon Aurora is a modern relational database service offering performance and high availability at scale, fully open source MySQL and PostgreSQL-compatible editions, and a range of developer tools for building serverless and machine learning (ML)-driven applications.

## Exercise

Exercise 1

 Study
- Elastic Beanstalk
- CloudFront
- Route53

Exercise 2

Practice
- EFS
- RDS, Aurora

### Sources

[https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.html](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/AWSHowTo.html)

[https://www.qovery.com/blog/deploying-containers-on-aws-elastic-beanstalk-vs-ecs-vs-eks](https://www.qovery.com/blog/deploying-containers-on-aws-elastic-beanstalk-vs-ecs-vs-eks)

[https://aws.amazon.com/cloudfront/](https://aws.amazon.com/cloudfront/)

[https://medium.com/mindful-engineering/today-we-will-learn-about-cloudfront-690bf3a8819a](https://medium.com/mindful-engineering/today-we-will-learn-about-cloudfront-690bf3a8819a)

[https://aws.amazon.com/lambda/edge/](https://aws.amazon.com/lambda/edge/)

[https://www.freewebstack.com/cloudflare-vs-cloudfront-what-exactly-are-the-differences-between-them/](https://www.freewebstack.com/cloudflare-vs-cloudfront-what-exactly-are-the-differences-between-them/)

[https://aws.amazon.com/route53/](https://aws.amazon.com/route53/)

[https://aws.amazon.com/efs/](https://aws.amazon.com/efs/)

[https://aws.amazon.com/rds/](https://aws.amazon.com/rds/)

[https://aws.amazon.com/rds/aurora/](https://aws.amazon.com/rds/aurora/)
****

### Overcome challenges

### Results

Exercise 1

### Elastic Beanstalk

Elastic Beanstalk is a service for deploying and scaling web applications and services.

Use cases:
- to quickly launch web applications
- to create mobile API backends for your applications
- to replatform critical business applications
    
Elastic Beanstalk uses core AWS services such as Amazon Elastic Compute Cloud (EC2), Amazon Elastic Container Service (ECS), AWS Auto Scaling, and Elastic Load Balancing (ELB) to easily support applications that need to scale to serve millions of users.

Can be integrated with Amazon CloudFront, Amazon CloudWatch, Amazon DynamoDB Amazon ElastiCache, Amazon RDS, Amazon Route 53, Amazon Simple Storage Service, Amazon VPC and IAM.

### CloudFront

Amazon CloudFront is a fast content delivery network (CDN) service that securely delivers data, videos, applications, and APIs to customers globally with low latency and high transfer speeds.

Use cases:
- to deliver fast, secure websites
- to accelerate dynamic content delivery and APIs
- to stream video live and on-demand
- to distribute software, game patches and Internet of Things (IoT), and over-the-air (OTA) updates

CloudFront works seamlessly with any AWS origin, such as Amazon S3, Amazon EC2, Elastic Load Balancing, or with any custom HTTP origin. You can customize your content delivery through CloudFront using the secure and programmable edge computing features CloudFront Functions and AWS Lambda@Edge.

### Route53

Amazon Route 53 is a highly available and scalable Domain Name System (DNS) web service. Route 53 connects user requests to internet applications running on AWS or on-premises.

Use cases:

- to manage network traffic globally
- to build highly available applications
- to set up private DNS

Exercise 2

### EFS
### RDS
### Aurora
###
![screenshot](/00_includes/AWS_13_1_screenshot.png)