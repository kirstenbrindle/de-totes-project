
from pg8000.native import Connection
import boto3
import json
import logging
# from botocore.exceptions import ClientError


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
        logger.info("Checking database for new info...")
        logger.error("ERROR AHHHHHHH")

        conn = Connection(**secrets_dict)
        # s3 = boto3.client('s3')
        logger.info("Checking database for new info...")
        logger.error("Test error")

    except ValueError:
        logger.error("There is no ingestion bucket ...")
        # ^^^ subject to change if more ValueErrors pop up^^^

    conn.close()

    # except KeyError as k:
    #     logger.error(f'Error retrieving data, {k}')
    # except ClientError as c:
    #     if c.response['Error']['Code'] == 'NoSuchKey':
    #         logger.error(f'No object found - {s3_object_name}')
    #     elif c.response['Error']['Code'] == 'NoSuchBucket':
    #         logger.error(f'No such bucket - {s3_bucket_name}')
    #     else:
    #         raise
    # except UnicodeError:
    #     logger.error(f'File {s3_object_name} is not a valid text file')
    # except InvalidFileTypeError:
    #     logger.error(f'File {s3_object_name} is not a valid text file')
    # except Exception as e:
    #     logger.error(e)
    #     raise RuntimeError