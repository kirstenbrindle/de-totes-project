import boto3

def get_file_name(s3_object_key):
    """
    This function gets the filename of the table\n
    that is store in the object of the ingestion bucket.

    Args:
    `s3_object_key`: name of the key file.

    ---------------------------
    Returns:

    `file_name`: The file name 

    """
    
    filename_complete =s3_object_key.split('/')[-1]
    filename= filename_complete.split('.')[0]
    return filename

def get_object_path(records):
    """
    This function extract the bucket name and\n
    object from the records\n
    
    Args:
    `records`: new events.

    ---------------------------
    Returns:

    `bucket name`: The bucket name of new the event.
    `object file`: The file name of new the event.

    """
    return records[0]['s3']['bucket']['name'], \
        records[0]['s3']['object']['key']
    

    
