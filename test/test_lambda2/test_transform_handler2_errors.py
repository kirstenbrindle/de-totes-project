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
@patch("src.transform_handler2.transform_handler2.get_file_and_ingestion_bucket_name")
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