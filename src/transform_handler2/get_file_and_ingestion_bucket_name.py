

def get_file_and_ingestion_bucket_name(records):
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
