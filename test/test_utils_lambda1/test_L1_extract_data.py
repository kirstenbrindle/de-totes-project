from src.extract_handler1.L1_extract_data import L1_extract_data
import pytest
from unittest.mock import Mock, patch, MagicMock
from datetime import datetime
from moto import mock_aws
import os
import boto3
import logging


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


@pytest.mark.describe("L1_extract_data")
@pytest.mark.it("Test L1_extract_data select * from table if boolean is True")
def test_L1_extract_data_runs_correct_query_if_boolean_true():
    """
    checks select query is correct if boolean is true.
    """
    mock_conn = MagicMock()
    mock_s3 = Mock()
    L1_extract_data(mock_conn, mock_s3, "currency", True, "bucket")
    mock_conn.run.assert_called_with("SELECT * FROM currency;")


@pytest.mark.describe("L1_extract_data")
@pytest.mark.it("""Test L1_extract_data invokes get most
               recent file if boolean is false""")
@patch("src.extract_handler1.L1_extract_data.get_most_recent_file")
def test_L1_extract_data_invokes_get_most_recent_if_false(mock_recent_file):
    """
    checks get_most_recent_file function is invoked if boolean is false.
    """
    mock_conn = MagicMock()
    mock_s3 = Mock()
    assert mock_recent_file.call_count == 0
    L1_extract_data(mock_conn, mock_s3, "currency", False, "bucket")
    assert mock_recent_file.call_count == 1
    mock_recent_file.assert_called_with(mock_s3, "bucket", "currency")


@pytest.mark.describe("L1_extract_data")
@pytest.mark.it("""Test L1_extract_data invokes
                get_timestamp if boolean is false""")
@patch("src.extract_handler1.L1_extract_data.get_timestamp")
@patch("src.extract_handler1.L1_extract_data.get_most_recent_file")
def test_L1_extract_data_invokes_get_timestamp_if_false(mock_gmrf, mock_gts):
    """
    checks get_timestamp function is invoked if boolean is false.
    """
    mock_conn = MagicMock()
    mock_s3 = Mock()
    assert mock_gts.call_count == 0
    L1_extract_data(mock_conn, mock_s3, "currency", False, "bucket")
    assert mock_gts.call_count == 1
    recent_file = mock_gmrf(mock_s3, "bucket", "currency")
    mock_gts.assert_called_with(recent_file)


@pytest.mark.describe("L1_extract_data")
@pytest.mark.it("""Test L1_extract_data select * from table
                with where clause if boolean is False""")
@patch("src.extract_handler1.L1_extract_data.get_timestamp")
@patch("src.extract_handler1.L1_extract_data.get_most_recent_file")
def test_L1_extract_data_runs_correct_query_if_false(mock_gmrf, mock_gts):
    """
    checks select query is correct if boolean is false.
    """
    mock_conn = MagicMock()
    mock_s3 = MagicMock()
    mock_gts.return_value = "2022-11-03 14:20:49.962"
    L1_extract_data(mock_conn, mock_s3, "currency", False, "bucket")
    mock_conn.run.assert_called_with(
        "SELECT * FROM currency WHERE last_updated > "
        "'2022-11-03 14:20:49.962';")


@pytest.mark.describe("L1_extract_data")
@pytest.mark.it("Test L1_extract_data invokes format data if boolean is false")
@patch("src.extract_handler1.L1_extract_data.get_timestamp")
@patch("src.extract_handler1.L1_extract_data.get_most_recent_file")
@patch("src.extract_handler1.L1_extract_data.format_data")
def test_L1_invokes_format_data_if_false(mock_fd, mock_gmrf, mock_gts):
    """
    checks format_data function is invoked if boolean is false.
    """
    mock_conn = MagicMock()
    mock_s3 = MagicMock()
    mock_conn.run.return_value = [[1, 'GBP',
                                   datetime(2022, 11, 3, 14, 20, 49, 962000),
                                   datetime(2022, 11, 3, 14, 20, 49, 962000)],
                                  [2, 'USD',
                                   datetime(2022, 11, 3, 14, 20, 49, 962000),
                                   datetime(2022, 11, 3, 14, 20, 49, 962000)],
                                  [3, 'EUR',
                                   datetime(2022, 11, 3, 14, 20, 49, 962000),
                                   datetime(2022, 11, 3, 14, 20, 49, 962000)]]
    mock_conn.columns = [{'name': 'example1'}]

    assert mock_fd.call_count == 0
    L1_extract_data(mock_conn, mock_s3, "currency", False, "bucket")
    assert mock_fd.call_count == 1
    mock_fd.assert_called_with(
        mock_conn.run.return_value, ['example1'])


@pytest.mark.describe("L1_extract_data")
@pytest.mark.it("Test L1_extract_data writes csv file to S3 bucket")
@mock_aws
@patch("src.extract_handler1.L1_extract_data.get_timestamp")
@patch("src.extract_handler1.L1_extract_data.get_most_recent_file")
@patch("src.extract_handler1.L1_extract_data.format_data")
def test_L1_extract_data_writes_csv_file_to_s3_bucket(
        mock_fd, mock_gmrf, mock_gts, mock_s3, mock_bucket):
    """
    checks it writes file to s3 bucket with mocks.
    """
    mock_conn = MagicMock()
    objects_list_before = mock_s3.list_objects_v2(
        Bucket="test-bucket")
    assert objects_list_before["KeyCount"] == 0
    L1_extract_data(mock_conn, mock_s3, "currency", True, "test-bucket")
    objects_list_after = mock_s3.list_objects_v2(
        Bucket="test-bucket")
    assert objects_list_after["KeyCount"] == 1
    assert 'currency' in objects_list_after['Contents'][0]['Key']


@pytest.mark.describe("L1_extract_data")
@pytest.mark.it("Test L1_extract_data runs a Select "
                "query from the given table if boolean is false")
@mock_aws
def test_L1_extract_data_test_database_false(mock_s3, mock_bucket):
    """
    checks writes file from test database to mock s3 bucket if boolean false.
    """
    mock_conn = MagicMock()
    mock_s3.put_object(
        Body='',
        Bucket='test-bucket',
        Key='payment_type/payment_type-2022-11-02 14:20:49.96244.csv',
    )
    objects_list_before = mock_s3.list_objects_v2(
        Bucket="test-bucket")
    assert objects_list_before["KeyCount"] == 1
    L1_extract_data(mock_conn, mock_s3, "payment_type", False, "test-bucket")
    objects_list_after = mock_s3.list_objects_v2(
        Bucket="test-bucket")
    assert objects_list_after["KeyCount"] == 2
    assert 'payment_type' in objects_list_after['Contents'][0]['Key']
    assert 'payment_type' in objects_list_after['Contents'][1]['Key']


@pytest.mark.describe("L1_extract_data")
@pytest.mark.it("Test L1_extract_data does not write "
                "to csv if boolean is "
                "false and no new data")
@patch("src.extract_handler1.L1_extract_data.get_most_recent_file")
@patch("src.extract_handler1.L1_extract_data.format_data")
@patch("src.extract_handler1.L1_extract_data.get_timestamp")
@mock_aws
def test_L1_extract_data_does_not_write(mock_get_timestamp,
                                        mock_get_format_data,
                                        mock_get_most_recent_file,
                                        mock_s3, mock_bucket):
    """
    checks writes file from test database to mock s3 bucket if boolean false.
    """

    mock_conn = MagicMock()
    mock_conn.run.return_value = []
    objects_list_before = mock_s3.list_objects_v2(
        Bucket="test-bucket")
    assert objects_list_before["KeyCount"] == 0
    L1_extract_data(mock_conn, mock_s3, "currency", False, "test-bucket")
    objects_list_after = mock_s3.list_objects_v2(
        Bucket="test-bucket")
    assert objects_list_after["KeyCount"] == 0
