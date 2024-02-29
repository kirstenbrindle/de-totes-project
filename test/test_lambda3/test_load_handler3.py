import pytest
from unittest.mock import patch
from moto import mock_aws
import os
import boto3
from src.load_handler3.load_handler3 import lambda_handler


@pytest.fixture(scope='function')
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "test"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
    os.environ["AWS_SECURITY_TOKEN"] = "test"
    os.environ["AWS_SESSION_TOKEN"] = "test"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


@pytest.fixture(scope='function')
def mock_s3(aws_credentials):
    """Mocked s3 connection for tests"""
    mock_s3 = boto3.client('s3')
    return mock_s3


@pytest.fixture
def patch_fixture():
    with patch("src.load_handler3.load_handler3."
               "get_file_and_bucket")\
        as get_file_bucket, \
        patch("src.load_handler3.load_handler3.get_table_name")\
            as get_table, \
         patch("src.load_handler3.load_handler3.read_parquet")\
            as read_parquet, \
         patch("src.load_handler3.load_handler3.upload_data")\
            as upload:
        yield (get_file_bucket, get_table,
               read_parquet, upload)


@pytest.mark.describe("lambda_handler3")
@pytest.mark.it("Test lambda_handler3 invokes get_file_bucket")
@mock_aws
def test_lambda_handler2_invokes_get_file_bucket(patch_fixture, mock_s3):
    """
    Given:
    lambda_handler is invoked by an s3 put object event

    Returns:
    No return. Check get_file_and_bucket util function is invoked
    if no errors
    """
    (get_file_bucket, get_table,
     read_parquet, upload) = patch_fixture
    get_file_bucket.return_value = 'processed-bucket', 'test.parquet'
    assert get_file_bucket.call_count == 0
    lambda_handler({'Records': 'test'}, {})
    assert get_file_bucket.call_count == 1


@pytest.mark.describe("lambda_handler3")
@pytest.mark.it("Test lambda_handler3 invokes get_table")
@mock_aws
def test_lambda_handler2_invokes_get_table(patch_fixture, mock_s3):
    """
    Given:
    lambda_handler is invoked by an s3 put object event

    Returns:
    No return. Check get_table_name util function is invoked
    if no errors
    """
    (get_file_bucket, get_table,
     read_parquet, upload) = patch_fixture
    get_file_bucket.return_value = 'processed-bucket', 'test.parquet'
    assert get_table.call_count == 0
    lambda_handler({'Records': 'test'}, {})
    assert get_table.call_count == 1


@pytest.mark.describe("lambda_handler3")
@pytest.mark.it("Test lambda_handler3 invokes read_parquet if no errors")
@mock_aws
def test_lambda_handler2_invokes_read_parquet(patch_fixture, mock_s3):
    """
    Given:
    lambda_handler is invoked by an s3 put object event

    Returns:
    No return. Check read_parquet util function is invoked
    if no errors
    """
    (get_file_bucket, get_table,
     read_parquet, upload) = patch_fixture
    get_file_bucket.return_value = 'processed-bucket', 'test.parquet'
    assert read_parquet.call_count == 0
    lambda_handler({'Records': 'test'}, {})
    assert read_parquet.call_count == 1


@pytest.mark.describe("lambda_handler3")
@pytest.mark.it("Test lambda_handler3 invokes upload_data if no error")
@mock_aws
def test_lambda_handler3_invokes_upload_data(patch_fixture, mock_s3):
    """
    Given:
    lambda_handler is invoked by an s3 put object event

    Returns:
    No return. Check upload_data util function is invoked
    if no errors
    """
    (get_file_bucket, get_table,
     read_parquet, upload) = patch_fixture
    get_file_bucket.return_value = 'processed_Bucket', 'sales_order.parquet'
    assert upload.call_count == 0
    lambda_handler({'Records': 'test'}, {})
    assert upload.call_count == 1


@pytest.mark.describe("lambda_handler3")
@pytest.mark.it("Test logs message if data uploaded successfully")
@mock_aws
def test_logs_success_message(patch_fixture, mock_s3, caplog):
    """
    Given:
    lambda_handler is invoked by an s3 put object event and successfully
    uploads data

    Returns:
    Logs an info message to inform that data has been uploaded
    """
    (get_file_bucket, get_table,
     read_parquet, upload) = patch_fixture
    get_file_bucket.return_value = 'processed', 'test.parquet'
    lambda_handler({'Records': 'test'}, {})
    assert "Data from test.parquet has successfully "
    "been uploaded to data warehouse" in caplog.text
    assert "INFO" in caplog.text
