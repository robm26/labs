## Lab: DynamoDB Capacity

### Intro

In a traditional on-premises database environment, everything begins with the server.  The CPU, memory, disks, and OS must all be configured and running smoothly in order to have success. Hardware failures and software updates keep a DBA awake at night, literally.

With DynamoDB, the job of the administrator is simplified in many ways.  AWS manages fleets of servers and storage nodes that you never have to worry about.

If curious, this talk from AWS re:Invent explains the internals of DynamoDB in great detail: [Amazon DynamoDB Under the Hood: How We Built a Hyper-Scale Database](https://youtu.be/yvBR71D0nAQ)

One concern that remains for administrators is the concept of Capacity Management.  A DynamoDB DBA should have a good understanding of the data access patterns of the application workload.  Many workloads have regular cycles of high volume during business hours, low volume on nights and weekends, occasional spikes in traffic from batch operations, while others have unpredictable and spiky patterns. 

DynamoDB gives the administrator controls to tune up or down the capacity of a table.  Done right, the table can scale up and down according to traffic conditions, saving considerable costs when compared with a traditional fixed-size server environment that suffers from periods of under or over provisioning.
An administrator should be mindful of the costs of database operations, and strive to use the table in the most efficient manner while meeting business objectives.

### Throughput Capacity Management

#### Provisioned Capacity (default)
The first step for a DynamoDB administrator is to create a Table, specifying the Read and Write performance desired.  

This performance, called Provisioned Capacity, is measured in RCU and WCU, aka Read Capacity Units and Write Capacity Units.
While similar to the IOPS (I/Os per second) settings of a virtual disk, the RCU and WCU are set at the table level and may be independently changed.
Writes to DynamoDB are approximately 20x the cost of reads, depending on the size of payloads.

   * Read the guide on [Provisioned Capacity](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ProvisionedThroughput.html)

A common practice is to boost the provisioned capacity settings 
before performing a bulk load of data into or out of DynamoDB, and then reduce the capacity
once the job is complete.

#### Provisioned Capacity with Auto Scaling

While you have full control of the capacity settings, it is efficient and convenient to leverage 
DynamoDB **Auto Scaling** so that the system automatically makes adjustments to your capacity according to the 
current workload patterns.  In this case you set a minimum and maximum range of capacity, and a desired target utilization, such as 70%.

   * Read the guide on [Auto Scaling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html)

#### On-Demand
There is another option, called **On Demand** capacity mode.  In this mode, there is no minimum capacity.  
If you leave the table idle you would incur zero ongoing billing cost, whereas Provisioned Capacity requires a small minimum of 1 capacity unit.
On Demand mode allows you to submit sudden large bursts of traffic which will be automatically handled.
On Demand is most useful for extremely spiky, large, and unpredictable traffic patterns that 
might temporarily overwhelm an Auto Scaling configuration.

For steady-state workloads, Provisioned Capacity with Auto Scaling will be over 5X less expensive than On Demand.

   * Read the On-Demand [blog post](https://aws.amazon.com/blogs/aws/amazon-dynamodb-on-demand-no-capacity-planning-and-pay-per-request-pricing/)
   and [pricing guide](https://aws.amazon.com/dynamodb/pricing/on-demand/)

-----

### Lab Steps

#### Customer360 Capacity Tuning

1. Login to the console and locate the table, **Customer360** you deployed in the [NoSQL Workbench](../lab-nosql-workbench/README.md) lab.
1. Click the Capacity tab to review capacity settings.
   * By default, the table will have 10 RCU and 10 WCU for the base table.  
     However, each additional GSI also is provisioned with 10 RCU and WCU.
     It's important to give your GSI's enough capacity to support the writes they will perform as 
     changes occur in the base table, or else the GSI will eventually report Throttling Exceptions that are returned to the client.
     The second GSI is a "Sparse Index" of customer names that is unlikely to be 
     changed at the same rate as the first GSI which materializes most of the base table records.
     We could attempt to estimate the correct capacity for each of these, but we may still over or under provision the table.
     Let's set Auto Scaling and allow AWS to set the capacity for us.  
1. At the bottom of the Capacity page, click the Read capacity checkbox.  
1. Set the Min capacity to 2 units and the Max capacity to 10 units.  By default these settings apply to indexes as well.
1. Click the Write capacity checkbox, and click "Same settings as read"
1. Notice how the console estimates your monthly DynamoDB bill cost for you.  (Click on the "Capacity Calculator" link to open a modeling tool for estimating your bill based on usage.)     
1. Click Save.


#### Auto Scaling in Depth

 * A detailed lab showing how to use the CLI to define scaling policies, and run a simple load test in Python is available online.

    * [Follow the lab steps in this article](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.CLI.html).  Check your DynamoDB dashboard in CloudWatch to see details of the load test and scaling events after your script has run.
    

 * The DynamoDB Specialist Solution Architect team has published a [thorough blog post on Auto Scaling](https://aws.amazon.com/blogs/database/amazon-dynamodb-auto-scaling-performance-and-cost-optimization-at-any-scale/)
     * Here we see the Provisioned Capacity scale up and down as the load reaches 1M requests per second.  
     * The latency remains excellent at under 6ms throughout this test.


![Auto Scaling](https://d2908q01vomqb2.cloudfront.net/887309d048beef83ad3eabf2a79a64a389ab1c9f/2019/02/26/dynamodb-auto-scaling-6.gif "Auto Scaling ")


### Next Steps

Continue on to the [Global Tables lab](../lab-global-tables/README.md).
