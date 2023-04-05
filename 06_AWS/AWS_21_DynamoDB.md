# Amazon DynamoDB

Amazon DynamoDB is a fully managed, serverless, key-value NoSQL database.

• Improves performance by keeping data in memory
• Keeps data secure by encrypting data at rest
• Protects data with backups and automated copying of data between AWS Regions

## Key terminology

- DynamoDB 

- The primary key is the only data that is required when storing a row in a DynamoDB table. Any other data is optional.

- A column in a DynamoDB table is called an attribute. 

- An item is a group of attributes that is uniquely identifiable among all of the other items.

- Simple primary key 
    -  The primary key consists of one attribute. 
    - The attribute is called the partition key or hash key.
- Composite primary key 
    - The primary key consists of two attributes. 
    - The first attribute is the partition key or hash key.
    - The second attribute is the sort key or range attribute.

- DynamoDB tables store data in partitions. Each table comprises one or more partitions.

- Consistency model of DynamoDB
    - Eventually consistent reads (the default)
    - Strongly consistent reads
    - ACID transactions – DynamoDB transactions provide developers atomicity, consistency, isolation, and durability (ACID) across one or more tables within a single AWS account and region. 

- A global table is a collection of one or more DynamoDB tables, which must all be owned by a single AWS account. The DynamoDB global tables feature provides high availability and scalability across Regions.

- Replica tables - the tables in the collection. Each replica stores the same set of data items.

## Exercise



### Sources
[https://aws.amazon.com/dynamodb/](https://aws.amazon.com/dynamodb/)

[https://aws.amazon.com/dynamodb/faqs/](https://aws.amazon.com/dynamodb/faqs/)

****

### Overcome challenges

### Results


    ![image](/00_includes/AWS_12.png)