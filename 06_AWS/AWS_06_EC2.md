# Elastic Compute Cloud (EC2)
EC2 allows users to rent virtual computers on which to run their own computer applications. EC2 encourages scalable deployment of applications by providing a web service through which a user can boot an Amazon Machine Image (AMI) to configure a virtual machine, which Amazon calls an "instance", containing any software desired.

## Key terminology
- AMI (Amazon Machine Image). An AMI is a supported and maintained image that contains all the informaton to launch an instance. 

- Security Group - a stateful firewall that works using explicit allow rules. 

- User Data - the set of commands/data you can provide to a instance at launch time.



## Exercise
- Exercise 1
    - Navigate to the EC2 menu.
    - Launch an EC2 instance with the following requirements:
        - AMI: Amazon Linux 2 AMI (HVM), SSD Volume Type
        - Instance type: t2.micro
        - Default network, no preference for subnet
        - Termination protection: enabled
        - User data:

            #!/bin/bash

            yum -y install httpd

            systemctl enable httpd

            systemctl start httpd

            echo '<html><h 1>Hello From Your Web Server!</h 1></html>' >   /var/www/html/index.html

        - Root volume: general purpose SSD, Size: 8 GiB
        - New Security Group:

            Name: Web server SG

            Rules: Allow SSH, HTTP and HTTPS from anywhere

- Exercise 2
    - Wait for the Status Checks to get out of the initialization stage. When you click the Status Checks tab, you should see that the System reachability and the Instance reachability checks have passed.
    - Log in to your EC2 instance using an ssh connection.
    - Terminate your instance.



### Sources

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html)

[https://stackoverflow.com/questions/9764145/amazon-ec2-user-data-how-does-it-work](https://stackoverflow.com/questions/9764145/amazon-ec2-user-data-how-does-it-work)



****

### Overcome challenges

### Results
Instance state:

![screenshot](/00_includes/AWS_06_1_screenshot.png)

Security group rules:

![screenshot](/00_includes/AWS_06_2_screenshot.png)

Instance details:

![screenshot](/00_includes/AWS_06_3_screenshot.png)

Logged in to the instance using an ssh connection:

![screenshot](/00_includes/AWS_06_4_screenshot.png)