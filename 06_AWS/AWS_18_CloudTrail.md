# AWS CloudTrail

CloudTrail events help you answer the questions of "who did what, where, and when?"

## Key terminology

- AWS CloudTrail

- Event history provides a 90-day history of control plane actions at no additional cost.

- CloudTrail Lake is a managed data lake for capturing, storing, accessing, and analyzing user and API activity on AWS for audit and security purposes. You can aggregate, immutably store your activity logs (control plane and data plane) for up to seven years, and query logs within seconds for search and analysis. 

- Trails capture a record of AWS account activities, delivering and storing these events in Amazon S3, with optional delivery to Amazon CloudWatch Logs and Amazon EventBridge.

- AWS CloudTrail Insights analyzes control plane events for anomalous behavior in API call volumes, and can detect unusual activity such as spikes in resource provisioning or gaps in periodic activity.

## Exercise

Study 
- AWS CloudTrail

### Sources

[https://aws.amazon.com/cloudtrail/](https://aws.amazon.com/cloudtrail/)

[https://aws.amazon.com/cloudtrail/features/?pg=ln&sec=hs](https://aws.amazon.com/cloudtrail/features/?pg=ln&sec=hs)

****

### Overcome challenges

### Results

AWS CloudTrail enables auditing, security monitoring, and operational troubleshooting by tracking user activity and API usage. CloudTrail logs, continuously monitors, and retains account activity related to actions across your AWS infrastructure, giving you control over storage, analysis, and remediation actions.

CloudTrail records two types of events:
- Management events that capture control plane actions on resources, such as creating or deleting Amazon Simple Storage Service (Amazon S3) buckets.
- Data events that capture data plane actions within a resource, such as reading or writing an Amazon S3 object.

AWS CloudTrail is enabled on all AWS accounts and records management events across AWS services without the need for any manual setup.