from pg8000.native import Connection, DatabaseError
import boto3
import json

# secrets manager
# db_name = boto3.client("totes_db")
#  user_id = db_name.get_secret_value(username="")
# util functions - select all from each table
# 
def lambda_handler():
    try:
        db_user = os.environ.get('PGUSER')
        db_database_name = os.environ.get('PGDATABASE')
        db_password = os.environ.get('PGPASSWORD')
        conn = Connection(
            user=db_user, database=db_database_name, password=db_password)
        # query = utils to be called. Need to decide utility functions to get staff, department etc.

        conn.close
    except DatabaseError as db_error:
        raise db_error
