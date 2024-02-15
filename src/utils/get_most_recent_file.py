
def get_most_recent_file(conn, table_name):
    client = conn 
    objects_list = client.list_objects_v2(Bucket="test_bucket")
    # get_folder = client.get_object(Bucket="test_bucket", Key=table_name)
    print(objects_list)


    