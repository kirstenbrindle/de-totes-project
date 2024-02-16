import boto3


def is_bucket_empty(bucket_name):
    """
    This function checks if the bucket is empty and return a boolean

    Arg:

    `bucket_name`: string of the bucket name

    ---------------------------
    Returns:

    `boolean`: True if bucket is empty, false otherwise


    """
    try:
        s3 = boto3.client('s3')
        response = s3.list_objects_v2(Bucket=bucket_name)
        if response['KeyCount'] == 0:
            return True
        return False
    except Exception as error:
        print(error.response['Error']['Message'])
