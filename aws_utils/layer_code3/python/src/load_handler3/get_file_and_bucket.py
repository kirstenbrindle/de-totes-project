import logging

logger = logging.getLogger('lambda3Logger')
logger.setLevel(logging.INFO)


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
    try:
        file_name = records[0]['s3']['object']['key']
        bucket_name = records[0]['s3']['bucket']['name']
        file_name = file_name.replace('+', ' ')
        file_name = file_name.replace('%3A', ':')
        return f'{bucket_name}', f'{file_name}'
    except Exception as e:
        logger.error(e)
        logger.info("Something has happened in the read_and_upload_wh.py...")
