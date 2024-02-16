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
    split_file = latest_file.split("-", 1)
    timestamp = split_file[1]
    return timestamp
