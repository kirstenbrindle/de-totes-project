from pg8000.native import Connection
import boto3
import json
import logging
from botocore.exceptions import ClientError
from src.utils.get_table_names import get_table_names
from src.utils.get_bucket_name import get_bucket_name
from src.utils.is_bucket_empty import is_bucket_empty
from src.utils.L1_extract_data import L1_extract_data

secretm = boto3.client("secretsmanager")
secret_file_name = secretm.get_secret_value(SecretId="totes_secret_aws")
secrets_dict = json.loads(secret_file_name["SecretString"])

logger = logging.getLogger('lambda1Logger')
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    '''Connects to Totesys database using
    credentials stored in SecretsManager.

    When the database is updated, the handler
    checks what data is new and writes
    to a csv file in the ingestion bucket.

    Returns:
        None

    Raises:
        RuntimeError: An unexpected error occurred in execution. Other errors
        result in an informative log message.
    '''
    try:
        conn = Connection(**secrets_dict)
        s3 = boto3.client('s3')
        table_names = get_table_names(conn)
        bucket_name = get_bucket_name()
        boolean = is_bucket_empty(bucket_name, s3)
        for table_name in table_names:
            L1_extract_data(conn, s3, table_name, boolean, bucket_name)


    except ValueError:
        logger.error("There is no ingestion bucket ...")
        # ^^^ subject to change if more ValueErrors pop up^^^

    except ClientError as c:
        if c.response['Error']['Code'] == 'NoSuchBucket':
            logger.error(f'No such bucket - {bucket_name}')
        else:
            logger.error("A ClientError has occurred")

    conn.close()

    
    # except ClientError as c:
    #     if c.response['Error']['Code'] == 'NoSuchKey':
    #         logger.error(f'No object found - {s3_object_name}')
    #     elif c.response['Error']['Code'] == 'NoSuchBucket':
    #         logger.error(f'No such bucket - {s3_bucket_name}')
    #     else:
    #         raise
    # except Exception as e:
    #     logger.error(e)
    #     raise RuntimeError
