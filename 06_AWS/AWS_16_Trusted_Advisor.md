# AWS Trusted Advisor

 AWS Trusted Advisor is an application that draws upon best practices learned from AWS’s aggregated operational history of serving hundreds of thousands of AWS customers. Trusted Advisor inspects your AWS environment and makes recommendations for saving money, improving system performance, or closing security gaps.

## Key terminology

- AWS Trusted Advisor
- Trusted Advisor checks

## Exercise

Study 
- Trusted Advisor

### Sources

[https://aws.amazon.com/premiumsupport/faqs/?nc=sn&loc=6](https://aws.amazon.com/premiumsupport/faqs/?nc=sn&loc=6)

[https://aws.amazon.com/blogs/aws/trusted-advisor-console-basic/](https://aws.amazon.com/blogs/aws/trusted-advisor-console-basic/)

****


### Results

Trusted Advisor includes an expanding list of checks in the categories of cost optimization, security, fault tolerance, performance, and service limits

The Trusted Advisor notification feature helps you stay up-to-date with your AWS resource deployment. You will be notified by weekly email when you opt in for this service. A refresh of checks is required to ensure up-to-date summary of check status in email notification. Automated weekly refresh of checks is performed for accounts with AWS Business Support, AWS Enterprise On-Ramp, and AWS Enterprise Support. Accounts with AWS Developer Support and AWS Basic Support will need to login to the AWS Management Console to trigger check refresh.

AWS Trusted Advisor Priority helps to focus on the most important recommendations to optimize your cloud deployments, improve resilience, and address security gaps. Available to AWS Enterprise Support customers, Trusted Advisor Priority provides prioritized and context-driven recommendations that come from your AWS account team as well as machine-generated checks from AWS services.

Four Best Practices at no Charge
The following Trusted Advisor checks are available to all AWS users at no charge:

Service Limits Check – This check inspects your position with regard to the most important service limits for each AWS product. It alerts you when you are using more than 80% of your allocation resources such as EC2 instances and EBS volumes.

Security Groups – Specific Ports Unrestricted Check – This check will look for and notify you of overly permissive access to your EC2 instances and help you to avoid malicious activities such as hacking, denial-of-service attacks, and loss of data.

IAM Use Check – This check alerts you if you are using account-level credentials to control access to your AWS resources instead of following security best practices by creating users, groups, and roles to control access to the resources.

MFA on Root Account Check – This check recommends the use of multi-factor authentication (MFA), to improve security by requiring additional authentication data from a secondary device.