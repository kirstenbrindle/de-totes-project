def get_most_recent_file(conn, table_name, bucket_name):
    '''
    Get_most_recent_file function takes aws connection \n
    and folder name as arguments and returns most recently updated \n
    file name in s3 bucket folder as output.

    Arguments: conn (Aws connection) table_name(folder within s3 bucket).
    '''
    client = conn
    objects_list = client.list_objects_v2(
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
    return file_name
