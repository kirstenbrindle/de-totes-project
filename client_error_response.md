```

@pytest.mark.describe('get bucket name')
@pytest.mark.it('test get bucket name return correct name of ingestion bucket')
def test_get_bucket_name_client_error(mock_s3):
    try:
        mock_s3.list_objects_v2(Bucket='wrong-bucket')
    except Exception as e:
        print(e, "<<<<<<<------ exception")
        print(e.response, "<<<<<<---- client error response")


@pytest.mark.describe('write csv')
@pytest.mark.it('test write csv return correct name of ingestion bucket')
def test_write_csv_client_error(mock_s3, mock_bucket):
    try:
        mock_s3.put_object(Body='i am the body', Bucket=mock_bucket, Key='?table_name}/?file_name.csv')
    except Exception as e:
        print(e, "<<<<<<<------ exception")
        

@pytest.mark.describe("get_table_names")
@pytest.mark.it("Test returns contents of Database error")
def test_get_table_names_database_error():
    """
    Given:
    A database error
    -> WRONG USERNAME, NO PASSWORD GIVEN
    pg8000.exceptions.DatabaseError: {'S': 'FATAL',\
    'V': 'FATAL', 'C': '28P01', 'M': 'password authentication failed \
    for user "helloooo"', 'F': 'auth.c', 'L': '335', 'R': 'auth_failed'}

    -> WRONG DB NAME
    pg8000.exceptions.DatabaseError: {'S': 'FATAL', 'V': 'FATAL', 'C': '3D000',\
    'M': 'database "test_database90000" does not exist', 'F': 'postinit.c', 'L':\
    '885', 'R': 'InitPostgres'}

    
    -> WRONG HOST ERROR
     pg8000.exceptions.InterfaceError: Can't create a connection to host localhost9000\
    and port 5432 (timeout is None and source_address is None).


    -> CLOSED CONNECTION
    pg8000.exceptions.InterfaceError: connection is closed
    Returns:
    Raises 
    """
    try:
        """Connection to test_database"""
        user = 'minnie'
        password = ''
        host = 'localhost'
        database = 'test_database'
        conn = Connection(user=user, password=password,
                        host=host, database=database)
        get_table_names(conn)
    except Exception as e:
        if e.args[0]['C'] == '28P01':
            print(e.args[0]['C'], "<<<<<----- args of db error")
        print(e, "<<<<<<----- error!!!")
        assert False
    

```