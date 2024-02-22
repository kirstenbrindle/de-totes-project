import boto3
import re


def get_bucket_name():
    s3 = boto3.client('s3')
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
        raise ValueError
    else:
        return matching_string

    # potential errors -
    # missing ingestion bucket
    # invalid bucket name, ingestion spelt incorrectly.
