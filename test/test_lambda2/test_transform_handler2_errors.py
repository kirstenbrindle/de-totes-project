from src.transform_handler2.transform_handler2 import lambda_handler
import pytest
from unittest.mock import patch
from moto import mock_aws
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


@pytest.mark.describe("lambda_handler2")
@pytest.mark.it("Test returns ValueError with correct message")
@patch("src.transform_handler2.transform_handler2.get_bucket_name_2")
@patch('''src.transform_handler2.transform_handler2
       .get_file_and_ingestion_bucket_name''')
@mock_aws
def test_get_bucket_name_error(mock_gfaibn, mock_get_bucket_name2, caplog):
    """
    Given:
    A Value error when there is no processed bucket

    Returns:
    log the correct message as an error
    """
    mock_get_bucket_name2.side_effect = ValueError
    mock_gfaibn.return_value = 'ingestion-bucket', 'test.csv'
    lambda_handler({'Records': 'test'}, {})
    assert "There is no processed bucket ..." in caplog.text
    assert "ERROR" in caplog.text


@pytest.mark.describe("transform_handler2")
@pytest.mark.it("Test returns ClientError with correct message NoSuchBucket")
@patch('''src.transform_handler2.transform_handler2
       .get_file_and_ingestion_bucket_name''')
@patch("src.transform_handler2.transform_handler2.write_to_parquet")
@patch("src.transform_handler2.transform_handler2.get_bucket_name_2")
@mock_aws
def test_get_table_names_no_such_bucket(mock_get_bucket_name,
                                        mock_write_to_parquet,
                                        mock_gfaibn, caplog):
    """
    Given:
    A ClientError

    Returns:
    Correct log message
    """
    operation_name = 'ListObjectsV2'
    parsed_response = {'Error': {'Code': 'NoSuchBucket',
                       'Message': 'The specified bucket does not exist'}}
    mock_gfaibn.return_value = 'ingestion-bucket', 'test.csv'
    mock_get_bucket_name.return_value = "AHHHHH-bucket"
    mock_write_to_parquet.side_effect = ClientError(
        parsed_response, operation_name)
    lambda_handler({'Records': 'test'}, {})
    assert "No such bucket - AHHHHH-bucket" in caplog.text
    assert "ERROR" in caplog.text


@pytest.mark.describe("lambda_handler 2")
@pytest.mark.it("""Test returns ClientError with
                message when other ClientErrors arise""")
@patch("src.transform_handler2.transform_handler2.is_bucket_empty_2")
@patch("src.transform_handler2.transform_handler2.get_bucket_name_2")
@mock_aws
def test_lambda_handler_2_client_err(mock_get_bucket_name,
                                     mock_is_bucket_empty, caplog):
    """
    Given:
    A ClientError

    Returns:
    Correct log message
    """
    operation_name = 'UploadPartCopy'
    parsed_response = {'Error': {'Code': '500', 'Message': 'Error Uploading'}}
    mock_get_bucket_name.return_value = "AHHHHH-bucket"
    mock_is_bucket_empty.side_effect = ClientError(
        parsed_response, operation_name)
    event = {
        "Records": [
            {
                "s3": {
                    "bucket": {
                        "name": "test-bucket"
                    },
                    "object": {
                        "key": "test.csv"
                    }
                }
            }
        ],
    }
    lambda_handler(event, {})
    assert "A ClientError has occurred" in caplog.text
    assert "ERROR" in caplog.text


@pytest.mark.describe("lambda_handler_2")
@pytest.mark.it("Test handles any other Exceptions")
@patch('''src.transform_handler2.transform_handler2
       .get_file_and_ingestion_bucket_name''')
@mock_aws
def test_get_table_names_exceptions(mock_gfaibn, caplog):
    """
    Given:
    Any other Exceptions

    Returns:
    Correct log message and raise RUNTIME ERROR
    """

    with pytest.raises(RuntimeError):
        mock_gfaibn.side_effect = Exception(
            "Something bad has happened ...")
        event = {
            "Records": [
                {
                    "s3": {
                        "bucket": {
                            "name": "test-bucket"
                        },
                        "object": {
                            "key": "test.csv"
                        }
                    }
                }
            ],
        }
        lambda_handler(event, {})
        assert "Something bad has happened ..." in caplog.text
        assert "ERROR" in caplog.text
