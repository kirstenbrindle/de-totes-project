from src.transform_handler2.transform_handler2 import lambda_handler
import pytest
from unittest.mock import patch
from moto import mock_aws
import boto3
from botocore.exceptions import ClientError
import os


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
    with patch("src.transform_handler2.transform_handler2."
               "get_file_and_ingestion_bucket_name")\
        as get_file_ing_bucket, \
         patch("src.transform_handler2.transform_handler2.get_bucket_name_2")\
            as get_pro_bucket, \
         patch("src.transform_handler2.transform_handler2.read_csv_to_df")\
            as read_csv, \
         patch("src.transform_handler2.transform_handler2.write_to_parquet")\
            as write_parquet:
        yield (get_file_ing_bucket, get_pro_bucket,
               read_csv, write_parquet)


@pytest.mark.describe("lambda_handler2")
@pytest.mark.it("Test returns ValueError with correct message")
@mock_aws
def test_get_bucket_name_error(patch_fixture, mock_s3, caplog):
    (get_file_ing_bucket, get_pro_bucket,
     read_csv, write_parquet) = patch_fixture
    """
    Given:
    A Value error when there is no processed bucket

    Returns:
    log the correct message as an error
    """
    get_pro_bucket.side_effect = ValueError
    get_file_ing_bucket.return_value = 'ingestion-bucket', 'test.csv'
    lambda_handler({'Records': 'test'}, {})
    assert "There is no processed bucket ..." in caplog.text
    assert "ERROR" in caplog.text


@pytest.mark.describe("transform_handler2")
@pytest.mark.it("Test returns ClientError with correct message NoSuchBucket")
@patch("src.transform_handler2.transform_handler2.make_fact_sales_order")
@mock_aws
def test_client_err_no_such_bucket(fact_sales, patch_fixture, mock_s3, caplog):
    (get_file_ing_bucket, get_pro_bucket,
     read_csv, write_parquet) = patch_fixture
    """
    Given:
    A ClientError

    Returns:
    Correct log message
    """
    operation_name = 'ListObjectsV2'
    parsed_response = {'Error': {'Code': 'NoSuchBucket',
                       'Message': 'The specified bucket does not exist'}}
    get_file_ing_bucket.return_value = 'ingestion-bucket', 'sales_order'
    get_pro_bucket.return_value = "AHHHHH-bucket"
    write_parquet.side_effect = ClientError(
        parsed_response, operation_name)
    lambda_handler({'Records': 'test'}, {})
    assert "No such bucket - AHHHHH-bucket" in caplog.text
    assert "ERROR" in caplog.text


@pytest.mark.describe("lambda_handler 2")
@pytest.mark.it("Test returns ClientError with message when "
                "other ClientErrors arise")
@patch("src.transform_handler2.transform_handler2.make_fact_sales_order")
@mock_aws
def test_lambda_handler_2_client_err(
        fact_sales, patch_fixture, mock_s3, caplog):
    (get_file_ing_bucket, get_pro_bucket,
     read_csv, write_parquet) = patch_fixture
    """
    Given:
    A ClientError

    Returns:
    Correct log message
    """
    operation_name = 'UploadPartCopy'
    parsed_response = {'Error': {'Code': '500', 'Message': 'Error Uploading'}}
    get_file_ing_bucket.return_value = 'ingestion-bucket', 'sales_order'
    get_pro_bucket.return_value = "AHHHHH-bucket"
    write_parquet.side_effect = ClientError(
        parsed_response, operation_name)
    lambda_handler({'Records': 'test'}, {})
    assert "A ClientError has occurred" in caplog.text
    assert "ERROR" in caplog.text


@pytest.mark.describe("lambda_handler_2")
@pytest.mark.it("Test handles any other Exceptions")
@mock_aws
def test_other_exceptions(patch_fixture, mock_s3, caplog):
    (get_file_ing_bucket, get_pro_bucket,
     read_csv, write_parquet) = patch_fixture
    """
    Given:
    Any other Exceptions

    Returns:
    Correct log message and raise RUNTIME ERROR
    """

    with pytest.raises(RuntimeError):
        get_file_ing_bucket.side_effect = Exception(
            "Something bad has happened ...")
        lambda_handler({'Records': 'test'}, {})
        assert "Something bad has happened ..." in caplog.text
        assert "ERROR" in caplog.text
