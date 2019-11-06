## Lab: NoSQL Workbench

### Intro

AWS introduced NoSQL Workbench for Amazon DynamoDB, 
 a tool to help developers build scalable, high-performance data models 
 and to simplify query development and testing. 
 NoSQL Workbench is a free, client-side application 
 available for Windows and macOS.

* [Announcement](https://aws.amazon.com/about-aws/whats-new/2019/09/introducing-nosql-workbench-for-amazon-dynamodb-now-in-preview/)

* [Download](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.settingup.html)

### First steps

This tool ships with a few default models pre-loaded.  Open the Employee Data Model.

1. Familiarize yourself with the three modes by clicking the far-left nav.  
    * Data Modeler
    * Visualizer
    * Operation Builder

### Customer360 Model

The workbench tool helps you to define a Model, which includes definitions for a table and indexes, plus sample data.

The workbench ships with a few models loaded.  A new model, called [Customer360.json](./models/Customer360.json) 
is provided for you in the [/models](./models) folder.  This model supports a set of customer applications for a sales and support operation.
You can see several types of records exist in one single table.  This is known as overloading.  
As such, the key columns are named only as pkey, skey, etc. since the values stored vary for different types of records.

The table records model important customer interactions in the sales cycle:

* PITCH
* ORDER
* DELIVERY
* SUPPORT

### Exploration
*It's recommended to maximize the workbench window for best visibility of the sample data.*


1. Import this model to the tool by clicking "Import Model" from the Data Modeler page, and loading the Customer360.json file. ([guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/workbench.Modeler.ImportExisting.html))

1. Spend a moment examining this model:
    1. From the left nav, under Tables, click the Customer360 table.
    1. Notice the table has a composite primary key using the pkey and skey columns (partition key + sort key).

1. Visualize the sample data.   Click the eyeball icon from the left nav to move to the Visualizer.
    1. Click the blue button: "Aggregate view"
    1. The underlying records are presented in hierarchical summary form, grouped by pkey and sorted by skey values.
    For most of the records, the pkey is the CustomerID (Customer100) and the skey is a simple timestamp (20191105).
    1. Locate and click on "gsi1".  A GSI will re-group the data on another column, in this case "pkey1".
    This view shows multiple customer records now organized by application type (PITCH, ORDER, etc.) 

1. Review the raw, flat dataset.  
    1. Click back to the table name, and then click on the "Update" just next to it.  
    This looks more like a database table, with attributes (columns) defined in the header.  
    1. Since this is NoSQL, there are less constraints on the schema of items (records).  
    While each item must have a unique primary key, the rest of the columns may be null.
    All attributes end up stored on disk as either a string, number, or binary.  You may see these raw types labeled as "S", "N" or "B".
    More complex types can be defined as abstractions, such as List and Map.
    1. Notice the final attribute called "attributes" which contains a Map type.  
    This big string contains a JSON structure, of key-value pairs.  Hover over the JSON to peek at the full object.
    DynamoDB has features to inspect and update the data nested within complex types like this.  
    Altogether, this makes NoSQL very popular with developers who naturally work with structures like arrays, objects, dictionaries, etc.
    1. Click to "gsi2".  This groups by the pkey2 column.  With only three records shown, it is an example of a Sparse Index.
    This index could be used to help locate the customerID value for a given customer name.
    
    
#### Task: Add records
> 1. Click back on the Update link, then click Add Data, and Manually Add Data.  
> 1. You may now notice there is another type of record shown, used to track a simple product master list.
> 1. Enter few new records.  Your *only* requirement is that you have a unique pkey and skey!  If you like, enter the following records:
>>    * pkey:  cust102
>>    * skey:  20191106
>>    * pkey1: PITCH
>>    * skey1: 20191106
>
>>    * pkey:  cust103
>>    * skey:  profile
>>    * pkey2: Mickey Mouse
> 1. Click the button on the top right to Save.
> 1. Visualize how your new record fits into the Table and GSI views.
    

### Publish

Let's deploy this new table, indexes, and data over the network to AWS DynamoDB now.
If you are sharing an AWS account amongst other attendees, you should rename your table to make it unique.
For example, your custom table could be called "Customer360-RobertM".

Customize the Table Name (if needed)
1. Click back to the Data Model view using the first of the three left nav icons.
1. Click on the table name, Customer360, from the left nav.  
1. Within the main panel, click on the "Edit" link at the top right to edit this model.
1. The first field is the name for this new table.  Update the name of your table if necessary.
1. Scroll down to the very bottom and be sure to click "Save edits" if you have made any changes.

Publish
1. Click back to the eyeball icon to open the Visualizer.
1. Click the "Commit to DynamoDB" button to begin the process.
1. Warning: *Do not accidentally deploy to your Production AWS account!*
    * To be safe, click "add a new connection" and paste in the credentials provided to you for this sandbox account.
1. The commit will take a minute to complete.
1. Once successful, login to the AWS console and locate your new table within the DynamoDB service.



### Operation Builder
A common question we hear is if there is a SQL-like tool for interacting with DynamoDB.
DynamoDB does not have a SQL interface; rather it is a pure API with REST service interfaces.

The NoSQL Workbench includes an Operation Builder that helps you 
write custom code to perform standard database operations in your favorite language.

1. Click the third icon from the left nav, the disk, to open the Operation Builder.
1. Click the existing connection you used to publish your table.
1. You are now browsing your online DynamoDB table(s) from AWS.  
1. Click to your Customer360 table.
1. Click the blue "Build Operations" button from the top right.
1. Click Query.
1. Type in "cust101" in the Partition Key field.
1. Click Execute. 
1. Repeat step 4, but this time click the Generate Code button.

You will see a panel of generated boilerplate code, in Python, Javascript or Java.
This code is quite robust in the exception handling.  You will see handlers for ThrottlingException errors amongst others.
Within the code, locate the .query() command.

You can use this feature in future to issue data manipulations on your table, or as a basis for developing your applications data access logic.

#### Task: Write a script to scan or query your table.

> Generate or write code to query a table and test it out.
> Refer to the AWS SDK DynamoDB documentation for Python ([boto3](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/GettingStarted.Python.html)), 
[Javascript](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/AWS/DynamoDB.html), 
[Java](https://aws.amazon.com/sdk-for-java/), or your favorite language.



### Next Steps

We don't want to be billed for the capacity used by this table if we leave it running for a long time.

**Delete this table within 24 hours, or reduce the capacity settings.**

Continue on to the [Capacity lab](../lab-capacity/README.md) for more instructions.

-----

Return [Home](../README.md)
