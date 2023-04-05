# AWS Global Infrastructure

The AWS Cloud spans 87 Availability Zones within 27 geographic regions around the world, with announced plans for 24 more Availability Zones and 8 more AWS Regions in Australia, Canada, India, Israel, New Zealand, Spain, Switzerland, and Thailand.

## Key terminology

- AWS Availability Zone
- Region
- Edge Location

## Exercise
- Study
    - What is an AWS Availability Zone?
    - What is a Region?
    - What is an Edge Location?
    - Why would you choose one region over another? (e.g. eu-central-1 (Frankfurt) over us-west-2 (Oregon))


### Sources

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html)

[https://cloudacademy.com/blog/aws-regions-and-availability-zones-the-simplest-explanation-you-will-ever-find-around/#:~:text=What%20are%20AWS%20Regions%3F,host%20their%20cloud%20infrastructure%20there.](https://cloudacademy.com/blog/aws-regions-and-availability-zones-the-simplest-explanation-you-will-ever-find-around/#:~:text=What%20are%20AWS%20Regions%3F,host%20their%20cloud%20infrastructure%20there.)

[https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/](https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/)

****


### Results
- What is an AWS Availability Zone?

Availability Zones are distinct locations within an AWS Region that are engineered to be isolated from failures in other Availability Zones. They provide inexpensive, low-latency network connectivity to other Availability Zones in the same AWS Region.

- What is a Region?

AWS Regions are separate geographic areas that AWS uses to house its infrastructure. These are distributed around the world so that customers can choose a region closest to them in order to host their cloud infrastructure there. The closer your region is to you, the better, so that you can reduce network latency as much as possible for your end-users. You want to be near the data centers for fast service.

- What is an Edge Location?

Edge locations are AWS data centers designed to deliver services with the lowest latency possible. Amazon has dozens of these data centers spread across the world. They're closer to users than Regions or Availability Zones, often in major cities, so responses can be fast and snappy.

- Why would you choose one region over another? (e.g. eu-central-1 (Frankfurt) over us-west-2 (Oregon))

There are four main factors that play into evaluating each AWS Region for a workload deployment:

- Compliance. If your workload contains data that is bound by local regulations, then selecting the Region that complies with the regulation overrides other evaluation factors. This applies to workloads that are bound by data residency laws where choosing an AWS Region located in that country is mandatory.
- Latency. A major factor to consider for user experience is latency. Reduced network latency can make substantial impact on enhancing the user experience. Choosing an AWS Region with close proximity to your user base location can achieve lower network latency. It can also increase communication quality, given that network packets have fewer exchange points to travel through.
- Cost. AWS services are priced differently from one Region to another. Some Regions have lower cost than others, which can result in a cost reduction for the same deployment.
- Services and features. Newer services and features are deployed to Regions gradually. Although all AWS Regions have the same service level agreement (SLA), some larger Regions are usually first to offer newer services, features, and software releases. Smaller Regions may not get these services or features in time for you to use them to support your workload.



