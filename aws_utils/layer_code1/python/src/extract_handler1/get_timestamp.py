import logging

logger = logging.getLogger('lambda1Logger')
logger.setLevel(logging.INFO)

def get_timestamp(latest_file: str) -> str:
    """
    This function takes the file name of the most recent file in a bucket \n
    sub-folder and reutrns the timestamp contained in the file name.

    Args:

    `latest_file`: string of the file name

    ---------------------------
    Returns:

    `timestamp`: a string of the timestamp in the file name


    """
    try:
        split_file = latest_file.split("-", 1)
        timestamp_with_csv = split_file[1]
        timestamp_parts = timestamp_with_csv.split(".", 2)
        timestamp = f'{timestamp_parts[0]}.{timestamp_parts[1]}'
        return timestamp
    except Exception as e:
        logger.info("something has gone wrong in the get_timestamp.py")
        logger.warning(e) 