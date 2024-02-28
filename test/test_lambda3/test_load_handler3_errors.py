from src.load_handler3.load_handler3 import lambda_handler
import pytest
from unittest.mock import patch
from moto import mock_aws
from botocore.exceptions import ClientError
from pg8000.native import DatabaseError, InterfaceError
import os
import pandas as pd


@pytest.fixture(scope='function')
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "test"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
    os.environ["AWS_SECURITY_TOKEN"] = "test"
    os.environ["AWS_SESSION_TOKEN"] = "test"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


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


@pytest.mark.describe("lambda_handler3")
@pytest.mark.it("Test returns ValueError with correct message")
@patch("src.load_handler3.load_handler3.get_file_and_bucket")
@mock_aws
def test_get_bucket_error(mock_get_file_bucket, caplog):
    """
    Given:
    A Value error when there is no processed bucket

    Returns:
    log the correct message as an error
    """
    mock_get_file_bucket.side_effect = ValueError
    lambda_handler({'Records': 'test'}, {})
    assert "ERROR" in caplog.text


@pytest.mark.describe("lambda_handler3")
@pytest.mark.it("Test returns ClientError with correct message NoSuchBucket")
@patch("src.load_handler3.load_handler3.get_file_and_bucket")
@patch("src.load_handler3.load_handler3.read_parquet")
@mock_aws
def test_read_parquet_no_such_bucket(
        mock_read_parquet, mock_file_bucket, caplog):
    """
    Given:
    A ClientError

    Returns:
    Correct log message
    """
    operation_name = 'GetObject'
    parsed_response = {'Error': {'Code': 'NoSuchBucket',
                       'Message': 'The specified bucket does not exist'}}
    mock_file_bucket.return_value = 'fake-bucket', 'test.parquet'
    mock_read_parquet.side_effect = ClientError(
        parsed_response, operation_name)
    lambda_handler({'Records': 'test'}, {})
    assert "There is no bucket..." in caplog.text
    assert "ERROR" in caplog.text


@pytest.mark.describe("lambda_handler3")
@pytest.mark.it("Test returns Database Error with authentication issue")
@patch("src.load_handler3.load_handler3.get_file_and_bucket")
@patch("src.load_handler3.load_handler3.read_parquet")
@patch("src.load_handler3.load_handler3.upload_data")
@mock_aws
def test_upload_data_database_error(
        upload_data, read_parq, get_file_bucket, test_df, caplog):
    """
    Given:
    A Database Error

    Returns:
    Correct log message
    """
    response = {'C': '28P01'}
    get_file_bucket.return_value = ('processed-bucket',
                                    'test/test123456.parquet')
    read_parq.return_value = test_df
    upload_data.side_effect = DatabaseError(response)
    lambda_handler({'Records': 'test'}, {})
    assert "DatabaseError: authentication issue" in caplog.text
    assert "ERROR" in caplog.text


@pytest.mark.describe("lambda_handler3")
@pytest.mark.it("Test returns Database Error with database name issue")
@patch("src.load_handler3.load_handler3.get_file_and_bucket")
@patch("src.load_handler3.load_handler3.read_parquet")
@patch("src.load_handler3.load_handler3.upload_data")
@mock_aws
def test_upload_data_db_name_err(
        upload_data, read_parq, get_file_bucket, caplog):
    """
    Given:
    A Database Error

    Returns:
    Correct log message
    """

    response = {'C': '3D000'}
    get_file_bucket.return_value = ('processed-bucket',
                                    'test/test+123%3A456.parquet')
    upload_data.side_effect = DatabaseError(response)
    lambda_handler({'Records': 'test'}, {})
    assert "DatabaseError: database does not exist" in caplog.text
    assert "ERROR" in caplog.text


@pytest.mark.describe("lambda_handler3")
@pytest.mark.it("Test returns InterfaceError Error when given wrong host ")
@patch("src.load_handler3.load_handler3.get_file_and_bucket")
@patch("src.load_handler3.load_handler3.read_parquet")
@patch("src.load_handler3.load_handler3.upload_data")
@mock_aws
def test_upload_data_db_err_host(
        upload_data, read_parq, get_file_bucket, caplog):
    """
    Given:
    A InterfaceError when wrong host

    Returns:
    Correct log message
    """
    response = "Can't create a connection to host localhost9000 "
    "and port 5432 (timeout is None and source_address is None)."
    get_file_bucket.return_value = ('processed-bucket',
                                    'test/test+123%3A456.parquet')
    upload_data.side_effect = InterfaceError(response)
    lambda_handler({'Records': 'test'}, {})
    assert "InterfaceError: incorrect hostname" in caplog.text
    assert "ERROR" in caplog.text


@pytest.mark.describe("lambda_handler3")
@pytest.mark.it("""Test returns InterfaceError
                when connection has been closed""")
@patch("src.load_handler3.load_handler3.get_file_and_bucket")
@patch("src.load_handler3.load_handler3.read_parquet")
@patch("src.load_handler3.load_handler3.upload_data")
@mock_aws
def test_get_table_names_db_err_conn(
        upload_data, read_parq, get_file_bucket, caplog):
    """
    Given:
    A InterfaceError when connection is closed

    Returns:
    Correct log message
    """
    response = "connection is closed"
    get_file_bucket.return_value = ('processed-bucket',
                                    'test/test+123%3A456.parquet')
    upload_data.side_effect = InterfaceError(response)
    lambda_handler({'Records': 'test'}, {})
    assert "InterfaceError: connection is closed" in caplog.text
    assert "ERROR" in caplog.text


@pytest.mark.describe("lambda_handler3")
@pytest.mark.it("Test handles any other Exceptions")
@patch("src.load_handler3.load_handler3.get_file_and_bucket")
@patch("src.load_handler3.load_handler3.read_parquet")
@patch("src.load_handler3.load_handler3.upload_data")
@mock_aws
def test_get_table_names_exceptions(
        upload_data, read_parq, get_file_bucket, caplog):
    """
    Given:
    Any other Exceptions

    Returns:
    Correct log message and raise RUNTIME ERROR
    """

    with pytest.raises(RuntimeError):
        get_file_bucket.return_value = ('processed-bucket',
                                        'test/test+123%3A456.parquet')
        upload_data.side_effect = Exception(
            "Something bad has happened ...")
        lambda_handler({'Records': 'test'}, {})
        assert "Something bad has happened ..." in caplog.text
        assert "ERROR" in caplog.text
