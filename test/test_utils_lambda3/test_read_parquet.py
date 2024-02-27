from src.load_handler3.read_parquet import read_parquet
from unittest.mock import patch
import pytest
import os
from moto import mock_aws
import boto3
import pandas as pd


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


@pytest.mark.describe("read_parquet")
@pytest.mark.it("test pandas read method is invoked")
@patch("src.load_handler3.read_parquet.pd")
def test_reads_method_is_invoked(mock_pd, mock_s3, mock_bucket):
    assert mock_pd.read_parquet.call_count == 0
    mock_s3.upload_file('test/test_parquet_file/test-pq.parquet',
                        'test-bucket', 'test/test-pq.parquet')
    read_parquet(mock_s3, 'test-bucket', 'test/test-pq.parquet')
    assert mock_pd.read_parquet.call_count == 1


@pytest.mark.describe("read_parquet")
@pytest.mark.it("test pandas returns dataframe with file contents")
@mock_aws
def test_returns_dataframe(mock_s3, mock_bucket):
    mock_s3.upload_file('test/test_parquet_file/test-pq.parquet',
                        'test-bucket', 'test/test-pq.parquet')
    data = {
        'currency_id': [1, 2, 3],
        'currency_code': ['GBP', 'USD', 'EUR'],
        'currency_name': ['British pound sterling',
                          'United States dollar', 'Euro'],
    }
    row_labels = [0, 1, 2]
    expected = pd.DataFrame(data=data, index=row_labels)
    result = read_parquet(mock_s3, 'test-bucket', 'test/test-pq.parquet')
    assert result.equals(expected)
