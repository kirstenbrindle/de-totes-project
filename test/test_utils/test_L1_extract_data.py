from src.utils.L1_extract_data import L1_extract_data
import pytest
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime
from pg8000.native import Connection
from moto import mock_aws
import os
import boto3


@pytest.fixture(scope="function")
def db_conn():
    """Connection to test_database"""
    user = 'tomroberts'
    password = 'password'
    host = 'localhost'
    database = 'test_database'
    return Connection(user=user, password=password,
                      host=host, database=database)


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


# @pytest.fixture
# def mock_bucket(mock_s3):
#     mock_s3.create_bucket(
#         Bucket='test-bucket',
#         CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})


@pytest.mark.describe("L1_extract_data")
@pytest.mark.it("Test L1_extract_data select * from table if boolean is True")
def test_L1_extract_data_runs_correct_query_if_boolean_true():

    mock_conn = MagicMock()
    mock_s3 = Mock()
    L1_extract_data(mock_conn, mock_s3, "currency", True, "bucket")
    mock_conn.run.assert_called_with("SELECT * FROM currency;")


@pytest.mark.describe("L1_extract_data")
@pytest.mark.it("""Test L1_extract_data invokes get most
               recent file if boolean is false""")
@patch("src.utils.L1_extract_data.get_most_recent_file")
def test_L1_extract_data_invokes_get_most_recent_file_if_boolean_is_false(mock_recent_file):
    mock_conn = MagicMock()
    mock_s3 = Mock()
    assert mock_recent_file.call_count == 0
    L1_extract_data(mock_conn, mock_s3, "currency", False, "bucket")
    assert mock_recent_file.call_count == 1
    mock_recent_file.assert_called_with(mock_s3, "bucket", "currency")


@pytest.mark.describe("L1_extract_data")
@pytest.mark.it("""Test L1_extract_data invokes
                get_timestamp if boolean is false""")
@patch("src.utils.L1_extract_data.get_timestamp")
@patch("src.utils.L1_extract_data.get_most_recent_file")
def test_L1_extract_data_invokes_get_timestamp_if_boolean_is_false(mock_get_most_recent_file, mock_timestamp):
    mock_conn = MagicMock()
    mock_s3 = Mock()
    assert mock_timestamp.call_count == 0
    L1_extract_data(mock_conn, mock_s3, "currency", False, "bucket")
    assert mock_timestamp.call_count == 1
    recent_file = mock_get_most_recent_file(mock_s3, "bucket", "currency")
    mock_timestamp.assert_called_with(recent_file)


@pytest.mark.describe("L1_extract_data")
@pytest.mark.it("""Test L1_extract_data select * from table
                with where clause if boolean is False""")
@patch("src.utils.L1_extract_data.get_timestamp")
@patch("src.utils.L1_extract_data.get_most_recent_file")
def test_L1_extract_data_runs_correct_query_if_boolean_is_false(mock_get_most_recent_file, mock_timestamp):
    mock_conn = MagicMock()
    mock_s3 = MagicMock()
    mock_timestamp.return_value = "2022-11-03 14:20:49.962"
    L1_extract_data(mock_conn, mock_s3, "currency", False, "bucket")
    mock_conn.run.assert_called_with(
        "SELECT * FROM currency WHERE last_updated > '2022-11-03 14:20:49.962';")


@pytest.mark.describe("L1_extract_data")
@pytest.mark.it("Test L1_extract_data invokes format data if boolean is false")
@patch("src.utils.L1_extract_data.get_timestamp")
@patch("src.utils.L1_extract_data.get_most_recent_file")
@patch("src.utils.L1_extract_data.format_data")
def test_L1_extract_data_invokes_format_data_if_boolean_is_false(mock_format_data, mock_get_most_recent_file, mock_get_timestamp):
    mock_conn = MagicMock()
    mock_s3 = MagicMock()
    mock_conn.run.return_value = [[1, 'GBP', datetime(2022, 11, 3, 14, 20, 49, 962000), datetime(2022, 11, 3, 14, 20, 49, 962000)], [2, 'USD', datetime(
        2022, 11, 3, 14, 20, 49, 962000), datetime(2022, 11, 3, 14, 20, 49, 962000)], [3, 'EUR', datetime(2022, 11, 3, 14, 20, 49, 962000), datetime(2022, 11, 3, 14, 20, 49, 962000)]]
    mock_conn.columns = [{'name': 'example1'}]

    assert mock_format_data.call_count == 0
    L1_extract_data(mock_conn, mock_s3, "currency", False, "bucket")
    assert mock_format_data.call_count == 1
    mock_format_data.assert_called_with(
        mock_conn.run.return_value, ['example1'])


@pytest.mark.describe("L1_extract_data")
@pytest.mark.it("Test L1_extract_data writes csv file to S3 bucket")
@mock_aws
@patch("src.utils.L1_extract_data.get_timestamp")
@patch("src.utils.L1_extract_data.get_most_recent_file")
@patch("src.utils.L1_extract_data.format_data")
def test_L1_extract_data_writes_csv_file_to_s3_bucket(mock_format_data, mock_get_most_recent_file, mock_get_timestamp, aws_credentials, mock_s3):
    mock_conn = MagicMock()
    mock_s3.create_bucket(
        Bucket='test-bucket',
        CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})
    L1_extract_data(mock_conn, mock_s3, "currency", False, "test-bucket")
    objects_list = mock_s3.list_objects_v2(
        Bucket="test-bucket")
    print(objects_list["Contents"])
    assert len(objects_list["Contents"]) == 1


# moved from format_data testing - we do not have a return val in L1 extract data.
    # Discuss how to approach - ****

# @pytest.mark.describe("L1_extract_data")
# @pytest.mark.it("Test L1_extract_data runs a Select "
#                 "query from the given table")
# def test_L1_extract_data_return_mock(db_conn):
#     """
#     checks returns value with a mock
#     """
#     expected = {
#         'payment_type_id': [1, 2, 3, 4],
#         'payment_type_name': ['SALES_RECEIPT', 'SALES_REFUND',
#                               'PURCHASE_PAYMENT', 'PURCHASE_REFUND'],
#         'created_at': [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000),
#                        datetime.datetime(2022, 11, 3, 14, 20, 49, 962000),
#                        datetime.datetime(2022, 11, 3, 14, 20, 49, 962000),
#                        datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)],
#         'last_updated': [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000),
#                          datetime.datetime(2022, 11, 3, 14, 20, 49, 962000),
#                          datetime.datetime(2022, 11, 3, 14, 20, 49, 962000),
#                          datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)]
#     }

#     result = L1_extract_data(db_conn, "payment_type")
#     assert result == expected
