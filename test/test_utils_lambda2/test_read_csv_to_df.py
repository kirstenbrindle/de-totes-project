from src.transform_handler2.read_csv_to_df import read_csv_to_df
from unittest.mock import patch
import pytest
import pandas as pd
import logging
import os
from moto import mock_aws
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


@pytest.mark.describe("read_csv_to_df")
@pytest.mark.it("test pandas read method is invoked")
@mock_aws
@patch("src.transform_handler2.read_csv_to_df.pd")
def test_reads_method_is_invoked(mock_pd, mock_s3, mock_bucket):
    assert mock_pd.read_csv.call_count == 0
    mock_s3.upload_file('test/test_csv_files/test1.csv',
                        'test-bucket', 'test/test1.csv')
    read_csv_to_df(mock_s3, 'test-bucket', "test/test1.csv")
    assert mock_pd.read_csv.call_count == 1


@pytest.mark.describe("read_csv_to_df")
@pytest.mark.it("test pandas returns dataframe with file contents")
@mock_aws
def test_returns_dataframe(mock_s3, mock_bucket):
    mock_s3.upload_file('test/test_csv_files/test1.csv',
                        'test-bucket', 'test/test1.csv')
    data = {
        'column1': ['r1c1', 'r2c1', 'r3c1'],
        'column2': ['r1c2', 'r2c2', 'r3c2'],
        'column3': ['r1c3', 'r2c3', 'r3c3'],
    }
    row_labels = [0, 1, 2]
    expected = pd.DataFrame(data=data, index=row_labels)
    result = read_csv_to_df(mock_s3, 'test-bucket', "test/test1.csv")
    assert result.equals(expected)


@pytest.mark.describe("read_csv_to_df")
@pytest.mark.it("test error output when given incorrect file path to read")
@mock_aws
def test_logs_error_when_passed_incorrect_file_path(
        mock_s3, mock_bucket, caplog):
    with caplog.at_level(logging.INFO):
        read_csv_to_df(mock_s3, 'test-bucket', "test/test_csv_files/test4.csv")
        assert "The specified key does not exist." in caplog.text


@pytest.mark.describe("read_csv_to_df")
@pytest.mark.it("test error output when given incorrect file type")
@mock_aws
def test_logs_error_when_passed_incorrect_file_type(
        mock_s3, mock_bucket, caplog):
    with caplog.at_level(logging.INFO):
        read_csv_to_df(mock_s3, 'test-bucket', "requirements.txt")
        assert "File type incorrect, must be csv format" in caplog.text
