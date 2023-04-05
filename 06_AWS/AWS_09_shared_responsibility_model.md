# Shared Responsibility Model

AWS has a “Shared Responsibility Model” that determines which cloud components AWS is responsible for securing and which are the customer’s responsibility to secure. 

## Key terminology


## Exercise

Study
- The AWS Shared Responsibility Model

### Sources

[https://aws.amazon.com/compliance/shared-responsibility-model/](https://aws.amazon.com/compliance/shared-responsibility-model/)

[The AWS Shared Responsibility Model: Everything You Need to Know](https://ermetic.com/blog/aws/the-aws-shared-responsibility-model-everything-you-need-to-know/?utm_adgroup=sc-all_bs-dsa&caid=17364497905&agid=142847490408&ad_id=600968942361&utm_feeditemid=&utm_device=c&utm_source=google&utm_medium=cpc&utm_campaign=gs_ge-row_cat-all_dv-desktop_bs-dsa&utm_campaign=&utm_term=&utm_term=&utm_content=AdID^600968942361^Placement^^Device^c&hsa_cam=17364497905&hsa_grp=142847490408&hsa_mt=&hsa_src=g&hsa_ad=600968942361&hsa_acc=3779647694&hsa_net=adwords&hsa_kw=&hsa_tgt=dsa-1573430999936&hsa_ver=3&gclid=CjwKCAjw5P2aBhAlEiwAAdY7dAJdUs_pGhlAYuKZYJrtOjh__UIDyeevXTq1wCOfP1YSEH2tkCfVkRoCrpsQAvD_BwE)

****


### Results

AWS responsibility “Security of the Cloud” - AWS is responsible for protecting the infrastructure that runs all of the services offered in the AWS Cloud. This infrastructure is composed of the hardware, software, networking, and facilities that run AWS Cloud services.

Customer responsibility “Security in the Cloud” – Customer responsibility will be determined by the AWS Cloud services that a customer selects. This determines the amount of configuration work the customer must perform as part of their security responsibilities. For example, a service such as Amazon Elastic Compute Cloud (Amazon EC2) is categorized as Infrastructure as a Service (IaaS) and, as such, requires the customer to perform all of the necessary security configuration and management tasks. Customers that deploy an Amazon EC2 instance are responsible for management of the guest operating system (including updates and security patches), any application software or utilities installed by the customer on the instances, and the configuration of the AWS-provided firewall (called a security group) on each instance. For abstracted services, such as Amazon S3 and Amazon DynamoDB, AWS operates the infrastructure layer, the operating system, and platforms, and customers access the endpoints to store and retrieve data. Customers are responsible for managing their data (including encryption options), classifying their assets, and using IAM tools to apply the appropriate permissions.


![image](/00_includes/AWS_09.jpg)