from pg8000.native import Connection, DatabaseError
import boto3
import json

# Creating client connection to secret manager
# gets secret file name value (secret identifier)
# reads secret database, user and password details from json file
secretm = boto3.client("secretsmanager")
secret_file_name = secretm.get_secret_value(SecretId="totes_db")
secrets_dict = json.loads(secret_file_name["SecretString"])
conn = Connection(**secrets_dict)

def lambda_handler():
    # try:
    #     conn = Connection(**secrets_dict)
    #     # query = utils to be called. Need to decide utility functions to get staff, department etc.
        db_query = "SELECT * FROM currency;"
        data = conn.run(db_query)
        conn.close
        print(data)
        return data
    # except DatabaseError as db_error:
    #     raise db_error
lambda_handler()