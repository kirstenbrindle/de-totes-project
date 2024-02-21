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
        

```