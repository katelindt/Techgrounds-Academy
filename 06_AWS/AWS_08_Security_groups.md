# Security Groups

A security group controls the traffic that is allowed to reach and leave the resources that it is associated with. For example, after you associate a security group with an EC2 instance, it controls the inbound and outbound traffic for the instance.

## Key terminology

- Security Group
- Network Access Control List

## Exercise

Study
- Security Groups in AWS
- Network Access Control Lists in AWS


### Sources

[https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html)

[https://www.knowledgehut.com/tutorials/aws/nacl-vs-security-groups](https://www.knowledgehut.com/tutorials/aws/nacl-vs-security-groups)


### Results

- A Network Access Control List (NACL) is an optional layer of security for the VPC that acts as a firewall for controlling traffic in and out of one or more subnets. You might set up network ACLs with rules similar to your security groups in order to add an additional layer of security to your VPC.

- NACL can be understood as the firewall or protection for the subnet. Security group can be understood as a firewall to protect EC2 instances.

More about security groups in presentation :

[https://docs.google.com/presentation/d/1omMu7X7H7U9l49kDpmmVW8kyE3Yp7lVnbTHORaWDYA0/edit#slide=id.p](https://docs.google.com/presentation/d/1omMu7X7H7U9l49kDpmmVW8kyE3Yp7lVnbTHORaWDYA0/edit#slide=id.p)