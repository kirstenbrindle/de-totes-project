# de-totes-project

Northcoders Data Engineer Nov 2023 cohort project

Project spec can be found here: https://github.com/northcoders/de-project-specification

Before running the project, you will need to run the following command in order to create an s3 bucket to store the terraform state file:

make run-make-bucket

You will be prompted to name the bucket.


File created db_credentials.json to store secret containing login credentials to connect to Totesys database in JSON format:
{
    "database" : "databasename",
    "user" : "username",
    "password" : "password",
    "host" : "awshostname",
    "port" : "0000"
}
File uploaded to aws secrets manager using command line. JSON file contents is then used to access the database through the lambda handler.

<!-- Update throughout -->