# Elastic Load Balancing (ELB) & Auto Scaling

Amazon EC2 Auto Scaling helps ensure that your application always has the right amount of capacity to handle the current traffic demand. Better cost management. Amazon EC2 Auto Scaling can dynamically increase and decrease capacity as needed.

Elastic Load Balancing automatically distributes your incoming traffic across multiple targets, such as EC2 instances, containers, and IP addresses, in one or more Availability Zones. It monitors the health of its registered targets, and routes traffic only to the healthy targets.

## Key terminology

AWS’ ELB is a managed service that provides load balancing to a fleet of instances. 

four types of ELBs:
- Application Load Balancer: this ELB works using HTTP and HTTPS protocols (layer 7 of the OSI stack).
- Network Load Balancer: this ELB works using TCP and UDP (layer 4 of the OSI stack).
- Classic Load Balancer: this ELB is outdated and not recommended for use. AWS has (so far) never stopped supporting any services. The reason for this is that it can harm existing applications.
- Gateway Load Balancer: this ELB acts as a gateway into your network, as well as a load balancer. It will first route traffic to a (3rd party) application that checks the traffic, like an IDS/IPS or Firewall. After the packet has been inspected, the GWLB acts like a NLB routing to your application. GWLB act on layers 3 and 4 of the OSI stack.

- Auto Scaling Group contains a collection of EC2 instances that are treated as a logical grouping for the purposes of automatic scaling and management. 

- An Amazon Machine Image (AMI) is a supported and maintained image provided by AWS that provides the information required to launch an instance. 

- Amazon CloudWatch collects and visualizes real-time logs, metrics, and event data in automated dashboards to streamline your infrastructure and application maintenance.


## Exercise

Exercise 1
- Launch an EC2 instance with the following requirements:
    - Region: Frankfurt (eu-central-1)
    - AMI: Amazon Linux 2
    - Type: t3.micro
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

    - Security Group: Allow HTTP
    - Wait for the status checks to pass.
    - Create an AMI from your instance with the following requirements:
    - Image name: Web server AMI    

Exercise 2
- Create an application load balancer with the following requirements:
    - Name: LabELB
    - Listener: HTTP on port 80
    - AZs: eu-central-1a and eu-central-1b
    - Subnets: must be public
    - Security Group: 
        - Name: ELB SG
        - Rules: allow HTTP access
    - Target Group:
        - Name: LabTargetGroup
        - Targets: to be registered by Auto Scaling
  
Exercise 3
- Create a launch configuration for the Auto Scaling group. It has to be identical to the server that is currently running.
- Create an auto scaling group with the following requirements:
    - Name: Lab ASG
    - Launch Configuration: Web server launch configuration
    - Subnets: must be in eu-central-1a and eu-central-1b
    - Load Balancer: LabELB
    - Group metrics collection in CloudWatch must be enabled
    - Group Size:
        - Desired Capacity: 2
        - Minimum Capacity: 2
        - Maximum Capacity: 4
    - Scaling policy: Target tracking with a target of 60% average CPU utilisation

Exercise 4
- Verify that the EC2 instances are online and that they are part of the target group for the load balancer.
- Access the server via the ELB by using the DNS name of the ELB.
- Perform a load test on your server(s) using the website on your server to activate auto scaling. There might be a delay on the creation of new servers in your fleet, depending on the settings on your Auto Scaling Group.


### Sources

[https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/tkv-create-ami-from-instance.html](https://docs.aws.amazon.com/toolkit-for-visual-studio/latest/user-guide/tkv-create-ami-from-instance.html) 

[https://aws.amazon.com/elasticloadbalancing/?nc=sn&loc=0](https://aws.amazon.com/elasticloadbalancing/?nc=sn&loc=0)

[https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/get-started-with-ec2-auto-scaling.html)

[https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html)

[https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-register-targets.html](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/target-group-register-targets.html)

- 

****

### Overcome challenges

### Results

Launched an EC2 instance

![screenshot](/00_includes/AWS_11_1_screenshot.png)

![screenshot](/00_includes/AWS_11_2_screenshot.png)

Created the AMI from the instance

![screenshot](/00_includes/AWS_11_3_screenshot.png)

Created an application load balancer

![screenshot](/00_includes/AWS_11_4_screenshot.png)

![screenshot](/00_includes/AWS_11_5_screenshot.png)

Created a launch template

![screenshot](/00_includes/AWS_11_6_screenshot.png)

Created an Auto Scaling group

![screenshot](/00_includes/AWS_11_7_screenshot.png)

![screenshot](/00_includes/AWS_11_8_screenshot.png)

target group:
![screenshot](/00_includes/AWS_11_9_screenshot.png)

Accessed the server via the ELB by using the DNS name of the ELB

![screenshot](/00_includes/AWS_11_10_screenshot.png)

Performed a load test on your server(s) using the website on your server to activate auto scaling

![screenshot](/00_includes/AWS_11_11_screenshot.png)

![screenshot](/00_includes/AWS_11_12_screenshot.png)

![screenshot](/00_includes/AWS_11_13_screenshot.png)

![screenshot](/00_includes/AWS_11_14_screenshot.png)

![screenshot](/00_includes/AWS_11_15_screenshot.png)

