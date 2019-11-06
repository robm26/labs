## Setup IAM Users for Immersion Day sandbox


### Overview
This folder contains scripts that will help you provision multiple users with AWS credentials to run the labs.
The process will read from the **users.txt** file, creating a new AWS IAM user for each name in this file.
These users will be granted a minimal set of privileges necessary to accomplish the labs.

The **policy.json** file defines these permissions.  

An administrator should have Python installed and configured first.

The process will create a Policy called **sandboxUserPolicy**, 
a group called **sandboxUsers**, and a set of users who are members of this group.

Each user will get an AWS console login password, and a key pair for programmatic access.


### Steps

1. Verify you have the [AWS CLI](https://aws.amazon.com/cli/) setup.
1.  Make sure the CLI is configured to point to a test, non-production AWS account.
    * Run ```aws sts get-caller-identity``` and verify the correct account.
    * If necessary, run ```aws configure``` or update the **default** profile in the ```.aws/credentials``` file in your home directory.
1. Clone or download this repository to your laptop, and navigate to this /aws-setup folder.
1. Open and update the list in **users.txt**.  Create enough entries for each person in the Immersion Day.
You can use any values, such as user1, user2, or actual logins or email addresses.
1. Examine the **setup_iam.py** script.  Notice the script creates the objects described above.
1. Examine the **policy.json** document.  Verify the permissions granted are acceptable.  The DynamoDB permissions allow access to only tables that begin with the word "sandbox".
1. From a command prompt, run `python setup_iam.py`
1. Copy the output to a new document or email, and share with the team members.



### Managing Permissions
If the users need additional permissions, you may locate the IAM Policy **sandboxUserPolicy** and update the policy document as needed.


### Cleanup DynamoDB
The AWS (always-)Free Tier allows for 25 RCU and 25 WCU of provisioned capacity, and 25 GB of storage, for the entire account.

At the end of the day, identify all DynamoDB tables that begin with "sandbox" or "Customer360" or 

For each of these, click the Capacity tab.  
Update the capacity to "On Demand" if the table will be relatively idle, 
or click the Read and Write checkboxes to adjust the Provisioned Capacity to low values.

Recommended:  
* Target Utilization: 70%
* Minimum Capacity: 1 RCU
* Max Capacity: 10 RCU

**DO NOT leave Provisioned Capacity tables running as THEY MAY INCUR ONGOING BILLING CHARGES!**


### Cleanup IAM Users 

At the end of the day, you may run the cleanup script to delete the IAM resources, 
or simply remove users from the group to limit them from creating any further resources.

 * Cleanup Script: ```python cleanup.py```
 
 