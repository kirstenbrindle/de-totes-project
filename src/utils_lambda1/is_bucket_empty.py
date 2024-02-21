def is_bucket_empty(bucket_name, s3):
    """
    This function checks if the bucket is empty and return a boolean

    Arg:

    `bucket_name`: string of the bucket name

    ---------------------------
    Returns:

    `boolean`: True if bucket is empty, false otherwise


    """
    response = s3.list_objects_v2(Bucket=bucket_name)
    if response['KeyCount'] == 0:
        return True
    return False
# potential errors
# already aware that bucket name is a bucket that exists so can be accessed. No potential errors associated. Previous function of get bucket name should catch errors.