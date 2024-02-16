from datetime import datetime 

def get_most_recent_file(conn, table_name):
    client = conn 
    objects_list = client.list_objects_v2(Bucket="test_bucket")
    # get_folder = client.get_object(Bucket="test_bucket", Key=table_name)
    files_list = []
    file_name = ""
    for value in objects_list["Contents"]:
        print(value["Key"])
        key = (str(value["Key"]).split("/"))[0]
        if key == table_name:
            print(table_name, key)
            if len(files_list) < 1:
                last_modified_string = value["LastModified"]
                files_list.append(last_modified_string)
                file_name = value["Key"]
                print("file", file_name)
            if value["LastModified"] > files_list[0]:
                files_list = []
                file_name = value["Key"]
                files_list.append(last_modified_string)
                print("hi2")
    return file_name
                

            

        


    