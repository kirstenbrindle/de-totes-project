def get_most_recent_file_2(s3, bucket_name, table_name):
    """
    Get_most_recent_file function takes aws connection
    and bucket name as arguments and returns most recently updated
    file name in s3 bucket folder as output.

    Args:
    `s3` AWS connection
    `bucket_name` s3 ingestion bucket name
    `table_name` folder within s3 ingestion bucket
    ---------------------------

    Returns:
        `file_name`: The file name the last modified file.
    """
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
