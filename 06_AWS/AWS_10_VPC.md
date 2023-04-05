# Virtual Private Cloud (VPC)

A virtual private cloud (VPC) is a virtual network dedicated to your AWS account. It is logically isolated from other virtual networks in the AWS Cloud. You can specify an IP address range for the VPC, add subnets, add gateways, and associate security groups. 

## Key terminology

- A subnet is a range of IP addresses in your VPC. A subnet must reside in a single Availability Zone. After you add subnets, you can deploy AWS resources in your VPC.

- IP addressing. You can assign IPv4 addresses and IPv6 addresses to your VPCs and subnets. You can also bring your public IPv4 and IPv6 GUA addresses to AWS and allocate them to resources in your VPC, such as EC2 instances, NAT gateways, and Network Load Balancers.

- Routing. Use route tables to determine where network traffic from your subnet or gateway is directed.

- Gateways and endpoints. A gateway connects your VPC to another network. For example, use an internet gateway to connect your VPC to the internet. Use a VPC endpoint to connect to AWS services privately, without the use of an internet gateway or NAT device.

- An Elastic IP address is a static public IPv4 address associated with your AWS account in a specific Region. Unlike an auto-assigned public IP address, an Elastic IP address is preserved after you stop and start your instance in a virtual private cloud (VPC).



## Exercise

Exercise 1  

- Allocate an Elastic IP address to your account.
- Use the Launch VPC Wizard option to create a new VPC with the following requirements:
    - Region: Frankfurt (eu-central-1)
    - VPC with a public and a private subnet
    - Name: Lab VPC
    - CIDR: 10.0.0.0/16  

- Requirements for the public subnet:
    - Name: Public subnet 1
    - CIDR: 10.0.0.0/24
    - AZ: eu-central-1a  

- Requirements for the private subnet:
    - Name: Private subnet 1
    - CIDR: 10.0.1.0/24
    - AZ: eu-central-1a  

Exercise 2
- Create an additional public subnet without using the wizard with the following requirements:  
    - VPC: Lab VPC
    - Name: Public Subnet 2
    - AZ: eu-central-1b
    - CIDR: 10.0.2.0/24  

- Create an additional private subnet without using the wizard with the following requirements:  
    - VPC: Lab VPC
    - Name: Private Subnet 2
    - AZ: eu-central-1b
    - CIDR: 10.0.3.0/24  

- View the main route table for Lab VPC. It should have an entry for the NAT gateway. Rename this route table to Private Route Table.  
- Explicitly associate the private route table with your two private subnets.  
- View the other route table for Lab VPC. It should have an entry for the internet gateway. Rename this route table to Public Route Table.  
- Explicitly associate the public route table to your two public subnets.  

Exercise 3
- Create a Security Group with the following requirements:  
    - Name: Web SG  
    - Description: Enable HTTP Access  
    - VPC: Lab VPC  
    - Inbound rule: allow HTTP access from anywhere  
    - Outbound rule: Allow all traffic  

Exercise 4
- Launch an EC2 instance with the following requirements:  
    - AMI: Amazon Linux 2  
    - Type: t3.micro  
    - Subnet: Public subnet 2  
    - Auto-assign Public IP: Enable  
    - User data:   
    #!/bin/bash

    #Install Apache Web Server and PHP

    yum install -y httpd mysql php

    #Download Lab files

    wget https://aws-tc-largeobjects.s3.amazonaws.com/CUR-TF-100-RESTRT-1/80-lab-vpc-web-server/lab-app.zip

    unzip lab-app.zip -d /var/www/html/

    #Turn on web server

    chkconfig httpd on
    
    service httpd start

- Tag:  
    - Key: Name  
    - Value: Web server  
- Security Group: Web SG  
- Key pair: no key pair  
- Connect to your server using the public IPv4 DNS name.


### Sources

[https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html](https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html)

****

### Overcome challenges

### Results

Exercise 1  

![screenshot](/00_includes/AWS_10_1_screenshot.png)


![screenshot](/00_includes/AWS_10_2_screenshot.png)


![screenshot](/00_includes/AWS_10_3_screenshot.png)

Exercise 2 

![screenshot](/00_includes/AWS_10_4_screenshot.png)


![screenshot](/00_includes/AWS_10_5_screenshot.png)


![screenshot](/00_includes/AWS_10_6_screenshot.png)


![screenshot](/00_includes/AWS_10_7_screenshot.png)


![screenshot](/00_includes/AWS_10_8_screenshot.png)


![screenshot](/00_includes/AWS_10_9_screenshot.png)   


![screenshot](/00_includes/AWS_10_10_screenshot.png)

Exercise 3

![screenshot](/00_includes/AWS_10_11_screenshot.png)

Exercise 4

![screenshot](/00_includes/AWS_10_12_screenshot.png)


![screenshot](/00_includes/AWS_10_13_screenshot.png)