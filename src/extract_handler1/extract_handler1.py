from pg8000.native import Connection, DatabaseError, InterfaceError
import boto3
import json
import logging
from botocore.exceptions import ClientError
from src.extract_handler1.get_table_names import get_table_names
from src.extract_handler1.get_bucket_name import get_bucket_name
from src.extract_handler1.is_bucket_empty import is_bucket_empty
from src.extract_handler1.L1_extract_data import L1_extract_data

secretm = boto3.client("secretsmanager", region_name='eu-west-2')
secret_file_name = secretm.get_secret_value(
    SecretId="totes_secret_aws")
secrets_dict = json.loads(secret_file_name["SecretString"])

logger = logging.getLogger('lambda1Logger')
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    """
    Connects to Totesys database using
    credentials stored in SecretsManager.
    When the database is updated, the handler
    checks what data is new and writes
    to a csv file in the ingestion bucket.

    Args:
        event: takes an aws event
    ---------------------------

    Returns:
        nothing

    Raises:
        RuntimeError: An unexpected error occurred in execution. Other errors
        result in an informative log message.
    """
    try:
        conn = Connection(**secrets_dict)
        s3 = boto3.client('s3', region_name='eu-west-2')
        table_names = get_table_names(conn)
        bucket_name = get_bucket_name()
        boolean = is_bucket_empty(bucket_name, s3)
        for table_name in table_names:
            L1_extract_data(conn, s3, table_name, boolean, bucket_name)

    except ValueError:
        logger.error("There is no ingestion bucket ...")

    except ClientError as c:
        if c.response['Error']['Code'] == 'NoSuchBucket':
            logger.error(f'No such bucket - {bucket_name}')
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
