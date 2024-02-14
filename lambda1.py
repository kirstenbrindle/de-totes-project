from pg8000.native import Connection, DatabaseError
import boto3
import json

# Creating client connection to secret manager
# gets secret file name value (secret identifier)
# reads secret database, user and password details from json file
secretm = boto3.client("secretsmanager")
secret_file_name = secretm.get_secret_value(SecretId="totes_secret_aws")
secrets_dict = json.loads(secret_file_name["SecretString"])


def lambda_handler():
    '''Connects to Totesys database using given value in secrets_dict
    Lambda handler invokes each db query utility function and closes connection to the database once queries are complete
    Returns value of db queries'''
    conn = Connection(**secrets_dict)
    # utility functions to be called within lambda handler
    conn.close()
    # return query values
