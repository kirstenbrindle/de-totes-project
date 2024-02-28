import logging

logger = logging.getLogger('lambda1Logger')
logger.setLevel(logging.INFO)


def get_most_recent_file(s3, bucket_name, table_name):
    '''
    Get_most_recent_file function takes aws connection \n
    and folder name as arguments and returns most recently updated \n
    file name in s3 bucket folder as output.

    Arguments: conn (Aws connection) table_name(folder within s3 bucket).
    '''
    """
     Get_most_recent_file function takes aws connection
     and folder name as arguments and returns most recently updated
     file name in s3 bucket folder as output.

     Args:
        `s3` aws connection.
        `bucket_name` name of the bucket you want to access.
        `table_name` this is the name of the folder the files are in.

     ---------------------------
     Returns:
        The name of the file last uploaded to aws.
     """

    try:
        objects_list = s3.list_objects_v2(
            Bucket=bucket_name, Prefix=table_name)
        files_list = []
        file_name = ""
        for value in objects_list["Contents"]:
            if len(files_list) < 1:
                last_modified_file = value["LastModified"]
                files_list.append(last_modified_file)
                file_name = value["Key"]
            if value["LastModified"] > files_list[0]:
                files_list = []
                last_modified_file = value["LastModified"]
                file_name = value["Key"]
                files_list.append(last_modified_file)
        return f'{file_name}'
    except Exception as e:
        logger.info("something has gone wrong in the get_most_recent_file.py")
        logger.warning(e)
