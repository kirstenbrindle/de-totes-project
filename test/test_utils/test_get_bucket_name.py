import boto3
import pytest
import os
from moto import mock_aws
from src.utils.get_bucket_name import get_bucket_name


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
def mock_bucket_one(mock_s3):
    mock_s3.create_bucket(
        Bucket='test-bucket',
        CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})


@pytest.fixture
def mock_bucket_two(mock_s3):
    mock_s3.create_bucket(
        Bucket='test-bucket-ingestion',
        CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})


@pytest.mark.describe('get bucket name')
@pytest.mark.it('test get bucket name return correct name of ingestion bucket')
def test_get_bucket_name(mock_bucket_one, mock_bucket_two):
    expected = 'test-bucket-ingestion'
    result = get_bucket_name()
    assert result == expected


@pytest.mark.describe('get bucket name')
@pytest.mark.it('''test get bucket name raises error''')
def test_get_bucket_name_error(mock_bucket_one):
    with pytest.raises(ValueError):
        get_bucket_name()



    
