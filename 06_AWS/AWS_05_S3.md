# Simple Storage Service (S3)

S3 - Amazon Simple Storage Service is a service offered by Amazon Web Services (AWS) that provides object storage through a web service interface. Amazon S3 uses the same scalable storage infrastructure that Amazon.com uses to run its e-commerce network. Amazon S3 can store any type of object, which allows uses like storage for Internet applications, backups, disaster recovery, data archives, data lakes for analytics, and hybrid cloud storage

## Key terminology

- Object- an object is a file and any metadata that describes the file.

- Bucket- a bucket is a container for objects stored in Amazon S3. You can store any number of objects in a bucket and can have up to 100 buckets in your account.

- S3 Standard offers high durability, availability, and performance object storage for frequently accessed data. Because it delivers low latency and high throughput, S3 Standard is appropriate for a wide variety of use cases, including cloud applications, dynamic websites, content distribution, mobile and gaming applications, and big data analytics.

- S3 Standard-IA (Amazon S3 Standard-Infrequent Access) is for data that is accessed less frequently, but requires rapid access when needed. S3 Standard-IA offers the high durability, high throughput, and low latency of S3 Standard, with a low per GB storage price and per GB retrieval charge. This combination of low cost and high performance make S3 Standard-IA ideal for long-term storage, backups, and as a data store for disaster recovery files.

- S3 One-zone IA (Amazon S3 One Zone-Infrequent Access) is for data that is accessed less frequently, but requires rapid access when needed. Unlike other S3 Storage Classes which store data in a minimum of three Availability Zones (AZs), S3 One Zone-IA stores data in a single AZ and costs 20% less than S3 Standard-IA. S3 One Zone-IA is ideal for customers who want a lower-cost option for infrequently accessed data but do not require the availability and resilience of S3 Standard or S3 Standard-IA. It’s a good choice for storing secondary backup copies of on-premises data or easily re-creatable data. You can also use it as cost-effective storage for data that is replicated from another AWS Region using S3 Cross-Region Replication.

- S3 Glacier - The Amazon S3 Glacier storage classes are purpose-built for data archiving, and are designed to provide you with the highest performance, the most retrieval flexibility, and the lowest cost archive storage in the cloud. You can choose from three archive storage classes optimized for different access patterns and storage duration. For archive data that needs immediate access, such as medical images, news media assets, or genomics data, choose the S3 Glacier Instant Retrieval storage class, an archive storage class that delivers the lowest cost storage with milliseconds retrieval. For archive data that does not require immediate access but needs the flexibility to retrieve large sets of data at no cost, such as backup or disaster recovery use cases, choose S3 Glacier Flexible Retrieval (formerly S3 Glacier), with retrieval in minutes or free bulk retrievals in 5—12 hours. To save even more on long-lived archive storage such as compliance archives and digital media preservation, choose S3 Glacier Deep Archive, the lowest cost storage in the cloud with data retrieval from 12—48 hours.



## Exercise

- Exercise 1

    - Create new S3 bucket with the following requirements:
        Region: Frankfurt (eu-central-1)
    - Upload a cat picture to your bucket.
    - Share the object URL of your cat picture with a peer. Make sure they are able to see the picture.

- Exercise 2

    - Create new bucket with the following requirements:
        Region: Frankfurt (eu-central-1)
    - Upload the four files that make up AWS’ demo website.
    - Enable static website hosting.
    - Share the bucket website endpoint with a peer. Make sure they are able to see the website.




### Sources

[https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html)

[https://youtube.com/watch?v=nmliQPCPpSY](https://youtube.com/watch?v=nmliQPCPpSY)

****

### Overcome challenges

### Results

- Exercise 1
I created a new not public S3 bucket, uploaded a cat picture and shared with a presigned URL

![screenshot](/00_includes/AWS_05_1_screenshot.png)

My peer shared a screenshot of the picture

![screenshot](/00_includes/AWS_05_1_screenshot_by_jayashree.png)


- Exercise 2
I created new bucket, uploaded website, enabled static website hosting and shared the link with my peer.

![screenshot](/00_includes/AWS_05_2_screenshot.png)

My peer shared a screenshot of the website

![screenshot](/00_includes/AWS_05_2_screenshot_by_jayashree.png)