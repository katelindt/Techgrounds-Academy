# Elastic Block Store (EBS)

Amazon Elastic Block Store (Amazon EBS) is an easy-to-use, scalable, high-performance block-storage service designed for Amazon Elastic Compute Cloud (Amazon EC2).

## Key terminology
- An Amazon EBS volume is a durable, block-level storage device that you can attach to your instances. After you attach a volume to an instance, you can use it as you would use a physical hard drive. EBS volumes are flexible. 

- Block-Storage - a form of cloud storage that is used to store data. Developers favor block storage for computing situations where they require fast, efficient, and reliable data transportation.

- EBS Multi-Attach allows the attachment of a single io1 Provisioned IOPS volume to up to 16 Nitro-based instances in the same Availability Zone. EBS Multi-Attach volumes can be used as a block-level subcomponent of an overall shared storage solution.

- Difference between io1 and io2?
The io2 volume provides up to 500 IOPS per GiB – ten times for than io1's 50 IOPS/GiB.

- gp3 - Amazon EBS gp3 volumes are the latest generation of general-purpose SSD-based EBS volumes that enable customers to provision performance independent of storage capacity

- A snapshot - EBS Snapshots are a point-in-time copy of your data, and can be used to enable disaster recovery, migrate data across regions and accounts, and improve backup compliance. 

- mkfs is a command used to format a block storage device with a specific file system.

- mount command is used to mount the filesystem found on a device to big tree structure(Linux filesystem) rooted at '/'. Conversely, another command umount can be used to detach these devices from the Tree.


## Exercise

- Exercise 1

    - Navigate to the EC2 menu.
    - Create a t2.micro Amazon Linux 2 machine with all the default settings.
    - Create a new EBS volume with the following requirements:
        - Volume type: General Purpose SSD (gp3)
        - Size: 1 GiB
        - Availability Zone: same as your EC2
    - Wait for its state to be available.

- Exercise 2

    - Attach your new EBS volume to your EC2 instance.
    - Connect to your EC2 instance using SSH.
    - Mount the EBS volume on your instance.
    - Create a text file and write it to the mounted EBS volume.

- Exercise 3

    - Create a snapshot of your EBS volume.
    - Remove the text file from your original EBS volume.
    - Create a new volume using your snapshot.
    - Detach your original EBS volume.
    - Attach the new volume to your EC2 and mount it.
    - Find your text file on the new EBS volume.


### Sources

[https://aws.amazon.com/ebs/](https://aws.amazon.com/ebs/)

[https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes.html](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes.html)

****

### Overcome challenges

### Results
Created a t2.micro Amazon Linux 2 machine with all the default settings:

![screenshot](/00_includes/AWS_07_1_screenshot.png)

Created a new EBS volume:

![screenshot](/00_includes/AWS_07_2_screenshot.png)

Attached my new EBS volume to my EC2 instance:

![screenshot](/00_includes/AWS_07_3_screenshot.png)

![screenshot](/00_includes/AWS_07_4_screenshot.png)

Connected to my EC2 instance using SSH, formatted and
mounted the EBS volume on my instance and created a text file

![screenshot](/00_includes/AWS_07_5_screenshot.png)

![screenshot](/00_includes/AWS_07_6_screenshot.png)

![screenshot](/00_includes/AWS_07_7_screenshot.png)

- Exercise 3:

![screenshot](/00_includes/AWS_07_8_screenshot.png)

![screenshot](/00_includes/AWS_07_9_screenshot.png)

![screenshot](/00_includes/AWS_07_10_screenshot.png)

![screenshot](/00_includes/AWS_07_11_screenshot.png)