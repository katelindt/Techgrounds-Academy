# Amazon Elastic Container Service

Amazon Elastic Container Service (ECS) is a highly scalable, high performance container management service that supports Docker containers and allows you to easily run applications on a managed cluster of Amazon Elastic Compute Cloud (Amazon EC2) instances. Amazon ECS eliminates the need for you to install, operate, and scale your own cluster management infrastructure.

## Key terminology

- An Amazon ECS cluster is a logical grouping of tasks or services. Your tasks and services are run on infrastructure that is registered to a cluster.

- Cluster management systems schedule work and manage the state of each cluster resource. 

- Amazon ECS capacity providers are used to manage the infrastructure the tasks in your clusters use. Each cluster can have one or more capacity providers and an optional default capacity provider strategy. The capacity provider strategy determines how the tasks are spread across the cluster's capacity providers. 

- Docker is the only container platform supported by Amazon ECS at this time.

## Exercise

Study
- ECS

### Sources

[https://aws.amazon.com/ecs/faqs/#General](https://aws.amazon.com/ecs/faqs/#General)

[https://docs.aws.amazon.com/AmazonECS/latest/userguide/clusters.html](https://docs.aws.amazon.com/AmazonECS/latest/userguide/clusters.html)

[https://docs.aws.amazon.com/AmazonECS/latest/userguide/cluster-capacity-providers.html](https://docs.aws.amazon.com/AmazonECS/latest/userguide/cluster-capacity-providers.html)

****

### Overcome challenges

### Results

Amazon ECS makes it easy to use containers as a building block for your applications by eliminating the need for you to install, operate, and scale your own cluster management infrastructure. Amazon ECS lets you schedule long-running applications, services, and batch processes using Docker containers. Amazon ECS maintains application availability and allows you to scale your containers up or down to meet your application's capacity requirements. Amazon ECS is integrated with familiar features like Elastic Load Balancing, EBS volumes, Amazon Virtual Private Cloud (VPC), and IAM. Simple APIs let you integrate and use your own schedulers or connect Amazon ECS into your existing software delivery process.

The Amazon ECS Service scheduler can manage long-running applications and services. The service scheduler helps you maintain application availability and allows you to scale your containers up or down to meet your application's capacity requirements. The service scheduler allows you to distribute traffic across your containers using Elastic Load Balancing (ELB). Amazon ECS will automatically register and deregister your containers from the associated load balancer.