## Lab: Global Tables

### Intro

Amazon DynamoDB global tables provide a fully managed solution for deploying a multiregion, multi-master database, without having to build and maintain your own replication solution. 
When you create a global table, you specify the AWS Regions where you want the table to be available. DynamoDB performs all of the necessary tasks to create identical tables in these Regions and propagate ongoing data changes to all of them.


Items can be written to any of the tables, and will be replicated in about 1 second to the other replicas.

In the event of simultaneous writes to the same Primary Key during this replication timespan, the system will resolve the conflict by applying the latest timestamped version of the data to all replicas.

Global Tables appends three additional attributes to your base table; You will see these columns with names beginning with "aws:rep:".  Do not attempt to modify these attributes.

### Best Practices

Global Tables should be identically configured with name, indexes, and capacity settings.

See the full set of [requirements and recommendations](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables_reqs_bestpractices.html)

Monitor the ongoing replication performance via these named CloudWatch metrics:
 * ReplicationLatency
 * PendingReplicationCount

You can find charts of these metrics embedded at the bottom of the DynamoDB Global Tables tab.


### Lab Steps

Follow the online [Global Tables tutorial](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/globaltables.tutorial.html).

If you have the AWS CLI configured, you may copy and paste the provided CLI commands to implement and test your Global Table.

Be sure to adjust the table name to something unique if you are sharing an AWS account with other participants!

Continue on to the [Backup and Restore Lab](../lab-backup-restore/README.md) for more instructions.


-----

Return [Home](../README.md)



