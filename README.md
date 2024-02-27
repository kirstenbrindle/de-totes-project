# de-totes-project

Northcoders Data Engineer Nov 2023 cohort project

Team Name: TotesOps

Project specification can be found here: https://github.com/northcoders/de-project-specification

## Set-up
##### Setting up variable environment for the project
Before running the project, you will need to run the following command to set up your variable environment and install any required dependencies:

`make requirements`

##### Creating bucket to store Terraform tf state file
Run the following command to create an s3 bucket to store the terraform state file (you will be prompted to name the bucket):

`make run-make-bucket`

##### Setting up AWS SNS topic
You should then run the following command from the root of the project to create an AWS SNS topic using your email address. This is where alerts and alarms will be sent:

`./deployment/email_subscriber.sh myemail@email.com`

##### Storing database credentials in AWS Secrets Manager
In order to create a secret containing login credentials on AWS SecretsManager, you will need a db_credentials.json file in the following format:

```
{ 
    "database" : "databasename",
    "user" : "username",
    "password" : "password",
    "host" : "awshostname",
    "port" : "0000"
}
```

The contents of this JSON file is created through the command line aws secret manager and accessed in Lambda handlers to access the totesys database.


## Lambda 1

### Description
This lambda handler operates on a 5 minute schedule and checks all table in the totesys database for new data at each invocation.
If new data is found, it writes this data to a csv file and saves it in a designated S3 bucket (organised in sub-folders for each table).


### Util functions
This lamba handler utilises the following util functions:
- get_table_names
- get_bucket_name
- is_bucket_empty
- L1_extract_data
- get_most_recent_file
- get_timestamp
- format_data
- write_csv

## Lambda 2

### Description
This lambda handler is triggered by an update to the ingestion bucket. The lambda handler reads the most recent file in the ingestion bucket and converts the file from csv to a dataframe. The lambda handler then transforms the data to the desired format and writes the transformed dataframe to a parquet file in each invocation and saves this to an s3 bucket (organised in sub-folders for each table).

### Util functions
This lamba handler utilises the following util functions:
- get_bucket_name_2
- get_file_and_ingestion_bucket_name
- get_most_recent_file_2
- make_dim_counterparty
- make_dim_currency
- make_dim_date
- make_dim_design
- make_dim_location
- make_dim_staff
- make_fact_sales_order
- read_csv_to_df
- transform_handler2
- write_to_parquet

## Lambda 3

### Description
This lambda handler is triggered by an update to the processed bucket. The lambda handler reads the most recent parquet file in the processed bucket and **?inserts data into data warehouse?**

### Util functions
This lamba handler utilises the following util functions:
- read_parquet
- get_file_and_processed_bucket_name
- get_table_name
- insert_data


### Deployment
All required AWS infrastructure is deployed via Terraform (except for the aforementioned tf state bucket and SNS topic).

The deployment is automated via a CI/CD pipeline carried out with GitHub Actions.