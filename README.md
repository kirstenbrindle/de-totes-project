# de-totes-project

Northcoders Data Engineer Nov 2023 cohort project

File created db_credentials.json to store secret containing login credentials to connect to Totesys database in JSON format:
{
    "database" : "databasename",
    "user" : "username",
    "password" : "password",
    "host" : "awshostname",
    "port" : "0000"
}
File uploaded to aws secrets manager using command line. JSON file contents is then used to access the database through the lambda handler.




