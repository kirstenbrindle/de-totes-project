from src.load_handler3.read_parquet import read_parquet
from src.transform_handler2.write_to_parquet import write_to_parquet
from unittest.mock import patch
import pytest
import pandas as pd
import logging
import os
from moto import mock_aws
from datetime import datetime
import boto3


logger = logging.getLogger('test')
logger.setLevel(logging.INFO)
logger.propagate = True


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


# result = f'table1-{datetime(2024,2,15,1,1,15)}.parquet'

@pytest.mark.describe("read_parquet")
@pytest.mark.it("test pandas read method is invoked")
@patch('src.transform_handler2.write_to_parquet.datetime')
def test_reads_method_is_invoked(mock_datetime, mock_s3, mock_bucket):
    assert mock_pd.read_parquet.call_count == 0
    mock_datetime.now.side_effect = [datetime(2024, 2, 15, 1, 1, 15)]
    data = {
    'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Olivia', 'Tony'],
    'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai',
             'Manchester', 'Cairo', 'Osaka'],
    'age': [41, 28, 33, 34, 38, 31, 37],
    'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
    }
    row_labels = [101, 102, 103, 104, 105, 106, 107]

    df = pd.DataFrame(data=data, index=row_labels)

    write_to_parquet(mock_s3, mock_bucket, 'table1', df)
    
    mock_s3.get_object(Bucket='test-bucket', Key=f'table1-{datetime(2024,2,15,1,1,15)}.parquet')
    read_parquet(mock_s3, "test-bucket", f'table1/table1-{datetime(2024,2,15,1,1,15)}.parquet')
    assert mock_pd.read_parquet.call_count == 1


# @pytest.mark.describe("read_pq_to_df")
# @pytest.mark.it("test pandas returns dataframe with file contents")
# @mock_aws
# def test_returns_dataframe(mock_s3, mock_bucket):
#     mock_s3.get_object(Bucket='test-bucket', Key='test/test1.parquet')
#     data = {
#         'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
#         'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai',
#                 'Manchester', 'Cairo', 'Osaka'],
#         'age': [41, 28, 33, 34, 38, 31, 37],
#         'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
#     }
#     row_labels = [101, 102, 103, 104, 105, 106, 107]

#     expected = pd.DataFrame(data=data, index=row_labels)
#     result = read_parquet(mock_s3, 'test-bucket', "test/test1.parquet")
#     assert result.equals(expected)


@pytest.mark.describe("uploads to warehouse db")
@pytest.mark.it("test dataframe is uploaded to postgres")
def test_uploads_parquet_to_postgres():
    pass
