from src.transform_handler2.is_bucket_empty_2 import is_bucket_empty_2
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


@pytest.fixture(scope='function')
def s3():
    """Mocked s3 connection for tests"""
    s3 = boto3.client('s3')
    return s3


@pytest.mark.describe("is_bucket_empty")
@pytest.mark.it("Test returns true if bucket is empty")
@mock_aws
def test_return_true_when_bucket_is_empty(aws_credentials, s3):
    s3.create_bucket(Bucket='test_totes_123',
                     CreateBucketConfiguration={
                         "LocationConstraint": "eu-west-2"})
    result = is_bucket_empty_2('test_totes_123', s3)

    assert result is True


@pytest.mark.describe("is_bucket_empty")
@pytest.mark.it("Test returns false if bucket is not empty")
@mock_aws
def test_return_false_when_bucket_is_not_empty(aws_credentials, s3):
    s3.create_bucket(Bucket='test_totes_123',
                     CreateBucketConfiguration={
                         "LocationConstraint": "eu-west-2"})
    s3.put_object(
        Body='',
        Bucket='test_totes_123',
        Key='test_file.txt',
    )
    result = is_bucket_empty_2('test_totes_123', s3)
    assert result is False
