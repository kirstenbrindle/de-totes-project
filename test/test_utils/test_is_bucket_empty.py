from src.utils.is_bucket_empty import is_bucket_empty
import pytest
from moto import mock_aws
import os
import boto3
from unittest.mock import patch


@pytest.fixture(scope='function')
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "test"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
    os.environ["AWS_SECURITY_TOKEN"] = "test"
    os.environ["AWS_SESSION_TOKEN"] = "test"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


@pytest.mark.describe("is_bucket_empty")
@pytest.mark.it("Test returns true if bucket is empty")
@mock_aws
def test_return_true_when_bucket_is_empty(aws_credentials):
    s3=boto3.client('s3')
    s3.create_bucket(Bucket='test_totes_123' ,
                     CreateBucketConfiguration={"LocationConstraint": "eu-west-2"})
    result = is_bucket_empty('test_totes_123')
    assert result is True

@pytest.mark.describe("is_bucket_empty")
@pytest.mark.it("Test returns false if bucket is not empty")
@mock_aws
def test_return_false_when_bucket_is_not_empty(aws_credentials):
    s3=boto3.client('s3')
    s3.create_bucket(Bucket='test_totes_123' ,
                     CreateBucketConfiguration={"LocationConstraint": "eu-west-2"})
    s3.upload_file('/home/cinthya/northcoders/phyton/project/de-totes-project/test_file.txt', 'test_totes_123','test_file.txt')
    result = is_bucket_empty('test_totes_123')
    assert result is False

@pytest.mark.describe("is_bucket_empty")
@pytest.mark.it("Test returns appropiate message if invalid bucket name")
@patch("builtins.print")
@mock_aws
def test_return_message_invalid_bucket_name(mock_print,aws_credentials):
    s3=boto3.client('s3')
    s3.create_bucket(Bucket='test_totes_123' ,
                     CreateBucketConfiguration={"LocationConstraint": "eu-west-2"})
    is_bucket_empty('test_totes_3')
    mock_print.assert_called_with('The specified bucket does not exist')
      