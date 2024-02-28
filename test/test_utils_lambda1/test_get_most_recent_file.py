from src.extract_handler1.get_most_recent_file import get_most_recent_file
import pytest
from moto import mock_aws
import boto3
import time
import os


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
    """Mocked S3 connection using mock credentials"""
    with mock_aws():
        yield boto3.client("s3", region_name='eu-west-2')


@pytest.fixture
def mock_bucket(mock_s3):
    """Mocked S3 bucket"""
    mock_s3.create_bucket(
        Bucket='test_bucket',
        CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})


@pytest.mark.describe("get_most_recent_file")
@pytest.mark.it("test returns file name as a string")
@mock_aws
def test_returns_type_of_string(mock_s3, mock_bucket):
    """
    Given:
    S3 connection, bucket_name and table_name

    Returns:
    A string type of the file last uploaded
    """
    mock_s3.put_object(Bucket="test_bucket",
                       Key="folder1/test_file_1.txt", Body="test_string")
    mock_s3.put_object(Bucket="test_bucket",
                       Key="folder1/test_file_2.txt", Body="test_string2")
    mock_s3.put_object(Bucket="test_bucket",
                       Key="folder2/test_file_3.txt", Body="test_string3")
    result = get_most_recent_file(mock_s3, "test_bucket", "folder1")
    assert type(result) is str


@pytest.mark.describe("get_most_recent_file")
@pytest.mark.it("test returns file name in folder")
@mock_aws
def test_returns_file_name_in_folder(mock_s3, mock_bucket):
    """
    Given:
    S3 connection, bucket_name and table_name

    Returns:
    A the correct folder and file name last uploaded as a string
    """
    mock_s3.put_object(Bucket="test_bucket",
                       Key="folder1/test_file_1.txt", Body="test_string")
    time.sleep(1)
    mock_s3.put_object(Bucket="test_bucket",
                       Key="folder1/test_file_2.txt", Body="test_string2")
    result = get_most_recent_file(mock_s3, "test_bucket", "folder1")
    assert result == "folder1/test_file_2.txt"


@pytest.mark.describe("get_most_recent_file")
@pytest.mark.it("test returns file name in folder "
                "with multiple files with differing last updated times")
@mock_aws
def test_returns_most_recent_file_name(mock_s3, mock_bucket):
    """
    Given:
    S3 connection, bucket_name and table_name

    Returns:
    A the correct folder and file name last uploaded as a string
    """
    mock_s3.put_object(
        Bucket="test_bucket",
        Key="folder1/test_file_1.txt", Body="test_string")
    time.sleep(1)
    mock_s3.put_object(
        Bucket="test_bucket",
        Key="folder1/test_file_2.txt", Body="test_string2")
    time.sleep(1)
    mock_s3.put_object(
        Bucket="test_bucket",
        Key="folder1/test_file_3.txt", Body="test_string2")
    result = get_most_recent_file(mock_s3, "test_bucket", "folder1")
    assert result == "folder1/test_file_3.txt"
