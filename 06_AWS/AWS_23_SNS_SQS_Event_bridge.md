# SNS, SQS, Event Bridge

SQS, SNS, and Eventbridge are three message orchestration services offered through AWS. Although having somewhat similar names, each of these services provides very different functionalities.

## Key terminology

- Amazon Simple Queue Service (SQS) lets you send, store, and receive messages between software components at any volume, without losing messages or requiring other services to be available.

    - Queues are the first class citizens of AWS. They are what you as the user will create either through the console, CLI, or IaC. 

    - Messages are the content or payload of what gets sent to the queue.

    - Polling is the mechanism by which the consumer of the queue will process them. 

- AWS SNS (Simple Notification Service) is a web service that makes it easy to set up, operate, and send notifications from the cloud.

    - Topics are the first class citizens of SNS. They are similar to queues in that messages are published to them, but they are not stateful in any way. They do not ‘hold’ messages, they simply are an endpoint that a publishing application can write to, and in turn, rely on SNS to broadcast a copy of that message out to all recipients.

    - Messages – Messages are simply JSON blobs that contain payload data. 

    - Publish/Subscribe or PubSub is a term that loosely defines the relationships between owners of data, and consumers of data. 

- AWS EventBridge is a service that provides real-time access to changes in data in AWS services, your own applications, and software as a service (SaaS) applications without writing code. 

    - Buses are very similar to SNS topics in that they receive events that need to be broadcaster to downstream consumers.

    - Events are similar to messages in the context of SNS and SQS, just with a fancier name. They consist of JSON blobs that describes the source and payload of the event. Events can also be “scheduled” to run at periodic intervals using a cron expression. This is useful for those of you looking to perform timed batch jobs regularly at a certain time of day.

    - Targets are the downstream recipient of events that are published to the message bus. 

    - Rules are the routing logic component for Message Buses. An Event Pattern is something that you define that matches the content of the message to a specific target. You can have many rules that all match to different patterns, but only 5 targets per rule. If you’d like to have more, you would need to create a new rule with the same event pattern, but with different configured targets.

Use SQS when:

- You’re looking for reliable 1:1 Asynchronous communication to decouple your applications from one another
- You want to rate limit your consumption of messages (perhaps due to a database bottleneck or some other use case)
- You want ordered message processing of vents

Use SNS when:

- You want to publish messages to MANY different subscribers with a single action
- Require high throughput and reliability for publishing and delivery to consumers
- Have many subscribers

Use Eventbridge when:

- You want to publish messages to many subscribers, and use the event data itself to match targets interested certain patterns.
- Want integration with other SaaS providers such as Shopify, Datadog, Pagerduty, or others
- Want to easily discover schemas that other teams produce and incorporate them into your application.
- You want to use regularly scheduled events using a cron-like expression to periodically send messages to your event bus.

## Exercise



### Sources
[https://aws.amazon.com/sqs/]https://aws.amazon.com/sqs/

[https://aws.amazon.com/sns/](https://aws.amazon.com/sns/)

[https://aws.amazon.com/eventbridge/](https://aws.amazon.com/eventbridge/)

[https://beabetterdev.com/2021/09/10/aws-sqs-vs-sns-vs-eventbridge/](https://beabetterdev.com/2021/09/10/aws-sqs-vs-sns-vs-eventbridge/)

[https://aws.amazon.com/blogs/compute/choosing-between-messaging-services-for-serverless-applications/](https://aws.amazon.com/blogs/compute/choosing-between-messaging-services-for-serverless-applications/)

****

### Overcome challenges

### Results


    ![image](/00_includes/AWS_12.png)