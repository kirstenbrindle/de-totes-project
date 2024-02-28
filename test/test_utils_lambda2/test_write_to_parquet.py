from src.transform_handler2.write_to_parquet import write_to_parquet
import os
from moto import mock_aws
import boto3
import pandas as pd
import pytest


@pytest.fixture
def test_df():
    data = {
        'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
        'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai',
                 'Manchester', 'Cairo', 'Osaka'],
        'age': [41, 28, 33, 34, 38, 31, 37],
        'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
    }
    row_labels = [101, 102, 103, 104, 105, 106, 107]
    return pd.DataFrame(data=data, index=row_labels)


@pytest.fixture(scope="function")
def aws_credentials():
    """Mocked AWS Credentials for moto"""
    os.environ["AWS_ACCESS_KEY_ID"] = "testing"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
    os.environ["AWS_SECURITY_TOKEN"] = "testing"
    os.environ["AWS_SESSION_TOKEN"] = "testing"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


@pytest.fixture
def mock_s3(aws_credentials):
    with mock_aws():
        yield boto3.client("s3", region_name='eu-west-2')


@pytest.fixture
def mock_bucket(mock_s3):
    mock_s3.create_bucket(
        Bucket='test-bucket',
        CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})


@pytest.mark.describe("write_to_parquet")
@pytest.mark.it("test a file is uploaded to s3 bucket")
@mock_aws
def test_uploads_a_file_to_s3(mock_s3, mock_bucket, test_df):
    """
    Given:
    A s3 connection, bucket name, table name and dataframe

    Returns:
    No return. Check it uploads a file to the bucket.
    """
    write_to_parquet(mock_s3, 'test-bucket', 'table1', test_df)
    response = mock_s3.list_objects_v2(Bucket='test-bucket')
    assert 'table1/table1' in response['Contents'][0]['Key']


@pytest.mark.describe("write_to_parquet")
@pytest.mark.it("test a parquet file is uploaded to s3 bucket")
@mock_aws
def test_uploads_a_parquet_file_to_s3(mock_s3, mock_bucket, test_df):
    write_to_parquet(mock_s3, 'test-bucket', 'table1', test_df)
    response = mock_s3.list_objects_v2(Bucket='test-bucket',
                                       Prefix='table1')
    assert '.parquet' in response['Contents'][0]['Key']
