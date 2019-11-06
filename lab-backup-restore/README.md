## Lab: Backup and Restore

### Intro

DynamoDB provides an integrated, managed backup service.

Backup and restore operations don't affect performance or API latencies. Backups are preserved regardless of table deletion.

Restores are performed at your request to a new table.  The backup is managed internally and is not available to you via S3, EBS, etc.

In the past, many customers would export all their records via the Scan operation, and restore records with Batch-Write-Item; 
however these approaches require lots of pagination for a large table, and consume provisioned capacity.


Backups and Restores always include GSIs and LSIs from the original table.  Restores cannot be performed to a different region.

Backups can be managed outside of DynamoDB by the [AWS Backup Service](https://aws.amazon.com/backup/)

There are costs with backups; however backup and restore does not consume RCU or WCU from your table.

#### On Demand Backups
Amazon DynamoDB provides on-demand backup capability. It allows you to create full backups of your tables for long-term retention and archival for regulatory compliance needs. You can back up and restore your DynamoDB table data anytime with a single click in the AWS Management Console or with a single API call. Backup and restore actions execute with zero impact on table performance or availability.

On-demand backup and restore scales without degrading the performance or availability of your applications. It uses a new and unique distributed technology that allows you to complete backups in seconds regardless of table size. You can create backups that are consistent within seconds across thousands of partitions without worrying about schedules or long-running backup processes. All backups are cataloged, easily discoverable, and retained until explicitly deleted.


#### Point in Time Recovery
You can enable point-in-time recovery.  When enabled, point-in-time recovery provides continuous backups until you explicitly turn it off.



### Lab Steps

 * [Backup Tutorial](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Backup.Tutorial.html)
 * [Restore Tutorial](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Restore.Tutorial.html)
 * [Point in Time Recovery](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/PointInTimeRecovery.Tutorial.html)
  



-----

Return [Home](../README.md)



