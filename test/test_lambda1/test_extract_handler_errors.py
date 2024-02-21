from src.extract_handler1.extract_handler1 import lambda_handler
import pytest
from unittest.mock import patch
from moto import mock_aws
from botocore.exceptions import ClientError
from pg8000.native import DatabaseError

@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Test returns ValueError with correct message")
@patch("src.extract_handler1.extract_handler1.get_bucket_name")
@mock_aws
def test_get_table_names_error(mock_get_bucket_name, caplog):
    """
    Given:
    A Value error when there is no ingestion bucket

    Returns:
    log the correct message as an error
    """
    mock_get_bucket_name.side_effect = ValueError
    lambda_handler('event', 'context')
    assert "There is no ingestion bucket ..." in caplog.text
    assert "ERROR" in caplog.text


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Test returns ClientError with correct message NoSuchBucket")
@patch("src.extract_handler1.extract_handler1.is_bucket_empty")
@patch("src.extract_handler1.extract_handler1.get_bucket_name")
@mock_aws
def test_get_table_names_no_such_bucket(mock_get_bucket_name, mock_is_bucket_empty, caplog):
    """
    Given:
    A ClientError 

    Returns:
    Correct log message
    """
    operation_name ='ListObjectsV2'
    parsed_response = {'Error': {'Code': 'NoSuchBucket', 'Message': 'The specified bucket does not exist'}}
    mock_get_bucket_name.return_value = "AHHHHH-bucket"
    mock_is_bucket_empty.side_effect = ClientError(parsed_response, operation_name)
    lambda_handler('event', 'context')
    assert "No such bucket - AHHHHH-bucket" in caplog.text
    assert "ERROR" in caplog.text


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Test returns ClientError with message when other ClientErrors arise")
@patch("src.extract_handler1.extract_handler1.is_bucket_empty")
@patch("src.extract_handler1.extract_handler1.get_bucket_name")
@mock_aws
def test_get_table_names_client_error(mock_get_bucket_name, mock_is_bucket_empty, caplog):
    """
    Given:
    A ClientError 

    Returns:
    Correct log message
    """
    operation_name ='UploadPartCopy'
    parsed_response = {'Error': {'Code': '500', 'Message': 'Error Uploading'}}
    mock_get_bucket_name.return_value = "AHHHHH-bucket"
    mock_is_bucket_empty.side_effect = ClientError(parsed_response, operation_name)
    lambda_handler('event', 'context')
    assert "A ClientError has occurred" in caplog.text
    assert "ERROR" in caplog.text


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Test returns Database Error")
@patch("src.extract_handler1.extract_handler1.get_table_names")
@mock_aws
def test_get_table_names_database_error(mock_get_table_names, caplog):
    """
    Given:
    A ClientError 

    Returns:
    Correct log message
    """
    mock_get_table_names.side_effect = DatabaseError
    lambda_handler('event', 'context')
    assert "A ClientError has occurred" in caplog.text
    assert "ERROR" in caplog.text

