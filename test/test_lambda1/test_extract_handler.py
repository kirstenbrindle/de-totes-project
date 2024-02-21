from src.extract_handler1.extract_handler1 import lambda_handler
import pytest
from unittest.mock import patch
from moto import mock_aws
import os
import boto3


@pytest.fixture(scope='function')
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "test"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
    os.environ["AWS_SECURITY_TOKEN"] = "test"
    os.environ["AWS_SESSION_TOKEN"] = "test"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


@pytest.fixture
def patch_fixture():
    with patch("src.extract_handler1.extract_handler1.get_table_names")\
        as mock_get_table_names, \
         patch("src.extract_handler1.extract_handler1.is_bucket_empty")\
            as mock_is_bucket_empty, \
         patch("src.extract_handler1.extract_handler1.get_bucket_name")\
            as mock_get_bucket_name, \
         patch("src.extract_handler1.extract_handler1.L1_extract_data")\
            as mock_L1_extract_data:
        yield (mock_get_table_names, mock_is_bucket_empty,
               mock_get_bucket_name, mock_L1_extract_data)


@pytest.fixture(scope='function')
def s3(aws_credentials):
    """Mocked s3 connection for tests"""
    s3 = boto3.client('s3')
    return s3


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("""Test lambda_handler invokes
                get_table_names""")
@patch("src.extract_handler1.extract_handler1.get_table_names")
@mock_aws
def test_lambda_handler_invokes_get_table_names(mock_get_table_names):
    assert mock_get_table_names.call_count == 0
    lambda_handler({}, {})
    assert mock_get_table_names.call_count == 1


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("""Test lambda_handler invokes
                get_bucket_name""")
@mock_aws
def test_lambda_handler_invokes_get_bucket_name(patch_fixture, s3):
    (mock_get_table_names, mock_is_bucket_empty,
     mock_get_bucket_name, mock_L1_extract_data) = patch_fixture
    mock_get_bucket_name.return_value = 'ingestion_bucket'
    mock_is_bucket_empty.return_value = True
    assert mock_get_bucket_name.call_count == 0
    lambda_handler({}, {})
    assert mock_get_bucket_name.call_count == 1


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("""Test lambda_handler invokes
                is_bucket_empty""")
@mock_aws
def test_lambda_handler_invokes_is_bucket_empty(patch_fixture, s3):
    (mock_get_table_names, mock_is_bucket_empty,
     mock_get_bucket_name, mock_L1_extract_data) = patch_fixture
    mock_get_bucket_name.return_value = 'ingestion_bucket'
    mock_is_bucket_empty.return_value = True
    assert mock_is_bucket_empty.call_count == 0
    lambda_handler({}, {})
    assert mock_is_bucket_empty.call_count == 1


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("""Test lambda_handler invokes L1_extract_data
                relative to number of tables in bucket""")
@mock_aws
def test_lambda_handler_invokes_L1_extract_data(patch_fixture, s3):
    (mock_get_table_names, mock_is_bucket_empty,
     mock_get_bucket_name, mock_L1_extract_data) = patch_fixture
    mock_get_bucket_name.return_value = 'ingestion_bucket'
    mock_get_table_names.return_value = ["table1", "table2", "table3"]
    mock_is_bucket_empty.return_value = True
    assert mock_L1_extract_data.call_count == 0
    lambda_handler({}, {})
    assert mock_L1_extract_data.call_count == 3
