from pg8000.native import Connection, DatabaseError
import boto3
import json
import logging


secretm = boto3.client("secretsmanager")
secret_file_name = secretm.get_secret_value(SecretId="totes_secret_aws")
secrets_dict = json.loads(secret_file_name["SecretString"])

logger = logging.getLogger('lambda1Logger')
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    '''Connects to Totesys database using credentials stored in SecretsManager.\n

    When the database is updated, the handler checks what data is new and writes\n
    to a csv file in the injestion bucket.

    Returns:
        None

    Raises:
        RuntimeError: An unexpected error occurred in execution. Other errors
        result in an informative log message.
    '''

    conn = Connection(**secrets_dict)
    s3 = boto3.client('s3')
    # get bucket name from s3.list_buckets and find injestion

    logger.info("Checking database for new info...")

    conn.close()
