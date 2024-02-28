from src.extract_handler1.is_bucket_empty import is_bucket_empty
import pytest
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
def mock_s3(aws_credentials):
    """Mocked S3 connection using mock credentials"""
    with mock_aws():
        yield boto3.client("s3", region_name='eu-west-2')


@pytest.fixture
def mock_bucket(mock_s3):
    """Mocked S3 bucket"""
    mock_s3.create_bucket(
        Bucket='test_totes_123',
        CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})


@pytest.mark.describe("is_bucket_empty")
@pytest.mark.it("Test returns true if bucket is empty")
@mock_aws
def test_return_true_when_bucket_is_empty(mock_s3, mock_bucket):
    """
    Given:
    S3 connection and bucket_name

    Returns:
    A boolean of True
    """
    result = is_bucket_empty('test_totes_123', mock_s3)
    assert result is True


@pytest.mark.describe("is_bucket_empty")
@pytest.mark.it("Test returns false if bucket is not empty")
@mock_aws
def test_return_false_when_bucket_is_not_empty(mock_s3, mock_bucket):
    """
    Given:
    S3 connection and bucket_name

    Returns:
    A boolean of False
    """
    mock_s3.put_object(
        Body='',
        Bucket='test_totes_123',
        Key='test_file.txt',
    )
    result = is_bucket_empty('test_totes_123', mock_s3)
    assert result is False
