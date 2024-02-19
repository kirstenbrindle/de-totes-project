import boto3
import re
import logging


def get_bucket_name():
    s3 = boto3.client('s3')
    logger = logging.getLogger(__name__)
    response = s3.list_buckets()
    bucket_list = [bucket['Name'] for bucket in response['Buckets']]
    matching_string = ''

    for bucket in bucket_list:
        match = re.search('ingestion', bucket)

        if match:
            matching_string = match.string
        else:
            continue
    if matching_string == '':
        logger.warning('No bucket name matching "ingestion"')
    else:
        return matching_string
