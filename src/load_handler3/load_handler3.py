from pg8000.native import Connection, DatabaseError, InterfaceError
import boto3
import json
import logging
from botocore.exceptions import ClientError
from src.load_handler3.get_file_and_bucket import get_file_and_bucket
from src.load_handler3.get_table_name import get_table_name
from src.load_handler3.read_parquet import read_parquet
from src.load_handler3.upload_data import upload_data

secretm = boto3.client("secretsmanager", region_name='eu-west-2')
secret_file_name = secretm.get_secret_value(
    SecretId="warehouseCredentials")
secrets_dict = json.loads(secret_file_name["SecretString"])

logger = logging.getLogger('lambda3Logger')
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    '''This function is triggered by a timed schedule
    - reads the parquet files from the processed bucket
    - connects to warehouse database using credentials stored in SecretsManager
    - loads file contents to warehouse db
    - logs errors
    '''
    try:
        conn = Connection(**secrets_dict)
        s3 = boto3.client('s3', region_name='eu-west-2')
        bucket_name, file_name = get_file_and_bucket(
            event['Records'])
        table_name = get_table_name(file_name)
        df = read_parquet(s3, bucket_name, file_name)
        upload_data(conn, table_name, df)
        
        logger.info(f"Data from {file_name} has successfully been uploaded to data warehouse")
    except ValueError:
        logger.error("Insert value error...")
        # ^^^ subject to change if more ValueErrors pop up^^^
    except ClientError as c:
        if c.response['Error']['Code'] == 'NoSuchBucket':
            logger.error('UPDATED WITH SOME CLIENT ERROR')
        else:
            logger.info(c)
            logger.error("A ClientError has occurred")

    except DatabaseError as db:
        if db.args[0]['C'] == '28P01':
            logger.error("DatabaseError: authentication issue")
        elif db.args[0]['C'] == '3D000':
            logger.error("DatabaseError: database does not exist")
        else:
            logger.info(db)
            logger.error('A DatabaseError has occurred')

    except InterfaceError as i:
        if "create a connection" in i.args[0]:
            logger.error("InterfaceError: incorrect hostname")
        elif "connection is closed" in i.args[0]:
            logger.error("InterfaceError: connection is closed")
        else:
            logger.info(i)
            logger.error("An InterfaceError has occurred")

    except Exception as e:
        logger.error(e)
        raise RuntimeError

    conn.close()
