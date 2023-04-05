# AWS Config

AWS Config is a fully managed service that provides you with an AWS resource inventory, configuration history, and configuration change notifications to enable security and governance.

## Key terminology

- AWS Config rules evaluate the configuration settings of your AWS resources. A rule can run when AWS Config detects a configuration change to an AWS resource or at a periodic frequency that you choose (for example, every 24 hours). There are two types of rules: AWS Config Managed Rules and AWS Config Custom Rules.

- A conformance pack is a collection of Config rules and remediation actions that is built using a common framework and packaging model in AWS Config.

- A Configuration Item (CI) is the configuration of a resource at a given point-in-time. 

- An aggregator is an AWS Config resource type that collects AWS Config data from multiple accounts and regions. Use an aggregator to view the resource configuration and compliance data recorded in AWS Config for multiple accounts and regions.

## Exercise

Study
- AWS Config

### Sources

[https://aws.amazon.com/config/faq/](https://aws.amazon.com/config/faq/)

[https://aws.amazon.com/config/features/](https://aws.amazon.com/config/features/)

[https://docs.aws.amazon.com/config/latest/developerguide/how-does-config-work.html](https://docs.aws.amazon.com/config/latest/developerguide/how-does-config-work.html)

****

### Overcome challenges

### Results

AWS Config records details of changes to your AWS resources to provide you with a configuration history. You can use the AWS Management Console, API, or CLI to obtain details of what a resource’s configuration looked like at any point in the past. AWS Config will also automatically deliver a configuration history file to the Amazon S3 bucket you specify.

AWS Config enables you to record software configuration changes within your Amazon EC2 instances and servers running on-premises, as well as servers and Virtual Machines in environments provided by other cloud providers. With AWS Config, you gain visibility into operating system (OS) configurations, system-level updates, installed applications, network configuration and more. AWS Config also provides a history of OS and system-level configuration changes alongside infrastructure configuration changes recorded for EC2 instances.

AWS Config can provide you with a configuration snapshot — a point-in-time capture of all your resources and their configurations. Configuration snapshots are generated on demand via the AWS CLI or API and delivered to the Amazon S3 bucket you specify.
