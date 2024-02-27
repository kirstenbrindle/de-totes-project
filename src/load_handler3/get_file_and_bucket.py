def get_file_and_bucket(records):
    """
     This function extracts the bucket name and\n
     object from the records\n

     Args:
     `records`: new events.

     ---------------------------
     Returns:

     `bucket name`: The bucket name of new the event.
     `object file`: The file name of new the event.

     """
    file_name = records[0]['s3']['object']['key']
    bucket_name = records[0]['s3']['bucket']['name']
    file_name = file_name.replace('+', ' ')
    file_name = file_name.replace('%', ':')
    return f'{bucket_name}', f'{file_name}'
