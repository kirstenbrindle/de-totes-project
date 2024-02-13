from pg8000.native import Connection, DatabaseError
import os
from dotenv import load_dotenv
load_dotenv()


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
