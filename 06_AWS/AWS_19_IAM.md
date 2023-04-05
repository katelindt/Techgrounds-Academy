# AWS Identity and Access Management (IAM)

IAM provides authentication and authorization for AWS services. A service evaluates if an AWS request is allowed or denied. Access is denied by default and is allowed only when a policy explicitly grants access. 

## Key terminology

- AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources.


- IAM Resources - the user, group, role, policy, and identity provider objects that are stored in IAM. As with other AWS services, you can add, edit, and remove resources from IAM.

- IAM Identities - the IAM resource objects that are used to identify and group. You can attach a policy to an IAM identity. These include users, groups, and roles.

- IAM Entities - the IAM resource objects that AWS uses for authentication. These include IAM users and roles.

- An IAM role is an IAM identity that you can create in your account that has specific permissions. An IAM role is similar to an IAM user, in that it is an AWS identity with permission policies that determine what the identity can and cannot do in AWS. However, instead of being uniquely associated with one person, a role is intended to be assumable by anyone who needs it. Also, a role does not have standard long-term credentials such as a password or access keys associated with it. Instead, when you assume a role, it provides you with temporary security credentials for your role session.

- Principals - a person or application that uses the AWS account root user, an IAM user, or an IAM role to sign in and make requests to AWS. Principals include federated users and assumed roles.

- Explicit deny. AWS checks each policy that applies to the context of your request. If a single permissions policy includes a denied action, AWS denies the entire request and stops evaluating. This is called an explicit deny.

- Identity provider(IdP).  With an identity provider, you can manage your user identities outside of AWS and give these external user identities permissions to use AWS resources in your account. This is useful if your organization already has its own identity system, such as a corporate user directory. It is also useful if you are creating a mobile app or web application that requires access to AWS resources.



## Exercise



### Sources

[https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html)

[https://aws.amazon.com/iam/faqs/?nc=sn&loc=5](https://aws.amazon.com/iam/faqs/?nc=sn&loc=5)

[https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html](https://docs.aws.amazon.com/IAM/latest/UserGuide/intro-structure.html)

****

### Overcome challenges

### Results

The IAM infrastructure includes the following elements:

- Terms
- Principal
- Request
When a principal tries to use the AWS Management Console, the AWS API, or the AWS CLI, that principal sends a request to AWS.

- Authentication
- Authorization
- Actions or operations
- Resources

IAM features:

- Shared access to your AWS account
- Granular permissions
- Secure access to AWS resources for applications that run on Amazon EC2
- Multi-factor authentication (MFA)
- Identity federation
- Identity information for assurance
- PCI DSS Compliance
- Integrated with many AWS services
- Eventually Consistent
- Free to use


### Results



Created a new IAM user
![screenshot](/00_includes/AWS_19_1_screenshot.png)

![screenshot](/00_includes/AWS_19_2_screenshot.png)

![screenshot](/00_includes/AWS_19_3_screenshot.png)

Created access key, accessed AWS using CLI, checked list of users

![screenshot](/00_includes/AWS_19_4_screenshot.png)

Created IAM role, that allows EC2 instances to call AWS services on my behalf

![screenshot](/00_includes/AWS_19_5_screenshot.png)