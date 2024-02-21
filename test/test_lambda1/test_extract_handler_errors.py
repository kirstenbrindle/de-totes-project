from src.extract_handler1.extract_handler1 import lambda_handler
import pytest
from unittest.mock import patch
from moto import mock_aws
from botocore.exceptions import ClientError
from pg8000.native import DatabaseError, InterfaceError
import os


@pytest.fixture(scope='function')
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "test"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
    os.environ["AWS_SECURITY_TOKEN"] = "test"
    os.environ["AWS_SESSION_TOKEN"] = "test"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


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
    lambda_handler({}, {})
    assert "There is no ingestion bucket ..." in caplog.text
    assert "ERROR" in caplog.text


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Test returns ClientError with correct message NoSuchBucket")
@patch("src.extract_handler1.extract_handler1.is_bucket_empty")
@patch("src.extract_handler1.extract_handler1.get_bucket_name")
@mock_aws
def test_get_table_names_no_such_bucket(mock_get_bucket_name,
                                        mock_is_bucket_empty, caplog):
    """
    Given:
    A ClientError

    Returns:
    Correct log message
    """
    operation_name = 'ListObjectsV2'
    parsed_response = {'Error': {'Code': 'NoSuchBucket',
                       'Message': 'The specified bucket does not exist'}}
    mock_get_bucket_name.return_value = "AHHHHH-bucket"
    mock_is_bucket_empty.side_effect = ClientError(
        parsed_response, operation_name)
    lambda_handler({}, {})
    assert "No such bucket - AHHHHH-bucket" in caplog.text
    assert "ERROR" in caplog.text


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("""Test returns ClientError with
                message when other ClientErrors arise""")
@patch("src.extract_handler1.extract_handler1.is_bucket_empty")
@patch("src.extract_handler1.extract_handler1.get_bucket_name")
@mock_aws
def test_get_table_names_client_err(mock_get_bucket_name,
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
    lambda_handler({}, {})
    assert "A ClientError has occurred" in caplog.text
    assert "ERROR" in caplog.text


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Test returns Database Error with authentication issue")
@patch("src.extract_handler1.extract_handler1.get_table_names")
@mock_aws
def test_get_table_names_database_error(mock_get_table_names, caplog):
    """
    Given:
    A Database Error

    Returns:
    Correct log message
    """

    response = {'C': '28P01'}
    mock_get_table_names.side_effect = DatabaseError(response)
    lambda_handler({}, {})
    assert "DatabaseError: authentication issue" in caplog.text
    assert "ERROR" in caplog.text


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Test returns Database Error with database name issue")
@patch("src.extract_handler1.extract_handler1.get_table_names")
@mock_aws
def test_get_table_names_db_name_err(mock_get_table_names, caplog):
    """
    Given:
    A Database Error

    Returns:
    Correct log message
    """

    response = {'C': '3D000'}
    mock_get_table_names.side_effect = DatabaseError(response)
    lambda_handler({}, {})
    assert "DatabaseError: database does not exist" in caplog.text
    assert "ERROR" in caplog.text


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Test returns InterfaceError Error when given wrong host ")
@patch("src.extract_handler1.extract_handler1.get_table_names")
@mock_aws
def test_get_table_names_db_err_host(mock_get_table_names, caplog):
    """
    Given:
    A InterfaceError when wrong host

    Returns:
    Correct log message
    """
    response = "Can't create a connection to host localhost9000\
    and port 5432 (timeout is None and source_address is None)."
    mock_get_table_names.side_effect = InterfaceError(response)
    lambda_handler({}, {})
    assert "InterfaceError: incorrect hostname" in caplog.text
    assert "ERROR" in caplog.text


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("""Test returns InterfaceError
                when connection has been closed""")
@patch("src.extract_handler1.extract_handler1.get_table_names")
@mock_aws
def test_get_table_names_db_err_conn(mock_get_table_names, caplog):
    """
    Given:
    A InterfaceError when connection is closed

    Returns:
    Correct log message
    """
    response = "connection is closed"
    mock_get_table_names.side_effect = InterfaceError(response)
    lambda_handler({}, {})
    assert "InterfaceError: connection is closed" in caplog.text
    assert "ERROR" in caplog.text


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("Test handles any other Exceptions")
@patch("src.extract_handler1.extract_handler1.get_table_names")
@mock_aws
def test_get_table_names_exceptions(mock_get_table_names, caplog):
    """
    Given:
    Any other Exceptions

    Returns:
    Correct log message and raise RUNTIME ERROR
    """

    with pytest.raises(RuntimeError):
        mock_get_table_names.side_effect = Exception(
            "Something bad has happened ...")
        lambda_handler({}, {})
        assert "Something bad has happened ..." in caplog.text
        assert "ERROR" in caplog.text
