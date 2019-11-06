## Labs
A set of labs for exploring and learning NoSQL with DynamoDB.

### Pre-requisites
 * Download and setup the [AWS CLI](https://aws.amazon.com/cli/)
 * Locate and install your favorite [AWS SDK](https://aws.amazon.com/tools/).
 * Install Python 2.7 (recommended)
   * Alternately, you may launch a new [Cloud9](https://us-east-1.console.aws.amazon.com/cloud9/home) environment, 
which has the CLI and Python pre-installed on the virtual command line.

 * Install the [NoSQL Workbench](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.settingup.html)

 * Download this repository to your laptop via ```git clone``` or by clicking the green download button.

### Authenticating to AWS

If you do not already have admin access to a sandbox AWS account, 
your administrator may run the setups in the [aws-setup](./aws-setup/README.md) folder
and share a unique set of credentials with you.  

You will get a special login URL for the AWS console, a password, and a separate pair of programmatic access keys.

Steps:
1. Run ```aws configure``` from your command line
1. Enter these keys, a default region (us-east-1) and default output type (json).
1. Type ```aws sts get-caller-identity``` to test your connection.  You should not receive any errors.

### Labs Overview

The following labs are available.  

1. [NoSQL Workbench](./lab-nosql-workbench/README.md)
1. [Capacity](./lab-capacity/README.md)
1. [Global Tables](./lab-global-tables/README.md)
1. [Backup Restore](./lab-backup-restore/README.md)

