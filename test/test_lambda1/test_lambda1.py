from src.extract_handler1.extract_handler1 import lambda_handler
import pytest
from unittest.mock import patch, MagicMock, Mock
from moto import mock_aws
import os
import boto3
from src.extract_handler1.extract_handler1 import get_table_names

@pytest.fixture(scope='function')
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "test"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
    os.environ["AWS_SECURITY_TOKEN"] = "test"
    os.environ["AWS_SESSION_TOKEN"] = "test"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


@pytest.fixture(scope='function')
def s3():
    """Mocked s3 connection for tests"""
    s3 = boto3.client('s3')
    return s3


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("""Test lambda_handler invokes
                get_table_names""")
@patch("src.extract_handler1.extract_handler1.get_table_names")
def test_lambda_handler_invokes_get_table_names(mock_get_table_names):
    assert mock_get_table_names.call_count == 0
    lambda_handler('event', 'context')
    assert mock_get_table_names.call_count == 1


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("""Test lambda_handler invokes
                get_bucket_name""")
@patch("src.extract_handler1.extract_handler1.get_bucket_name")
def test_lambda_handler_invokes_get_bucket_name(mock_get_bucket_name):
    assert mock_get_bucket_name.call_count == 0
    lambda_handler('event', 'context')
    assert mock_get_bucket_name.call_count == 1


@pytest.mark.describe("lambda_handler")
@pytest.mark.it("""Test lambda_handler invokes
                is_bucket_empty""")
@patch("src.extract_handler1.extract_handler1.get_bucket_name")
@patch("src.extract_handler1.extract_handler1.is_bucket_empty")
@mock_aws
def test_lambda_handler_invokes_is_bucket_empty(bucket_empty, bucket_name, s3):
    bucket_name.return_value = 'ingestion_bucket'
    assert bucket_empty.call_count == 0
    lambda_handler('event', 'context')
    assert bucket_empty.call_count == 1