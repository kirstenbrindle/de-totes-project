from src.transform_handler2.get_most_recent_file_2 import (
    get_most_recent_file_2)
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
    with mock_aws():
        yield boto3.client("s3", region_name='eu-west-2')


@pytest.fixture
def mock_bucket(mock_s3):
    mock_s3.create_bucket(
        Bucket='test-bucket',
        CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})


@pytest.mark.describe("get_most_recent_file_2")
@pytest.mark.it("Test returns a string")
@mock_aws
def test_returns_type_of_string(mock_s3, mock_bucket):
    """
    Given:
    An s3 connection, bucket name and database table name

    Returns:
    The most recent file name as a string
    """
    mock_s3.put_object(Bucket="test-bucket",
                       Key="folder1/test_file_1.txt", Body="test_string")
    mock_s3.put_object(Bucket="test-bucket",
                       Key="folder1/test_file_2.txt", Body="test_string2")
    mock_s3.put_object(Bucket="test-bucket",
                       Key="folder2/test_file_3.txt", Body="test_string3")
    result = get_most_recent_file_2(mock_s3, "test-bucket", "folder1")
    assert type(result) is str


@pytest.mark.describe("get_most_recent_file_2")
@pytest.mark.it("Test returns correct file name")
@mock_aws
def test_returns_file_name_in_folder(mock_s3, mock_bucket):
    """
    Given:
    An s3 connection, bucket name and database table name

    Returns:
    The most recent file name in the given sub-folder
    """
    mock_s3.put_object(Bucket="test-bucket",
                       Key="folder1/test_file_1.txt", Body="test_string")
    time.sleep(1)
    mock_s3.put_object(Bucket="test-bucket",
                       Key="folder1/test_file_2.txt", Body="test_string2")
    time.sleep(1)
    mock_s3.put_object(Bucket="test-bucket",
                       Key="folder2/test_file_3.txt", Body="test_string2")
    result = get_most_recent_file_2(mock_s3, "test-bucket", "folder1")
    assert result == "folder1/test_file_2.txt"


@pytest.mark.describe("get_most_recent_file_2")
@pytest.mark.it("Test returns correct file name with "
                "multiple files")
@mock_aws
def test_returns_most_recent_file_name_multiple_files(mock_s3, mock_bucket):
    """
    Given:
    An s3 connection, bucket name and database table name

    Returns:
    The most recent file name in the given sub-folder
    """
    mock_s3.put_object(
        Bucket="test-bucket",
        Key="folder1/test_file_1.txt", Body="test_string")
    time.sleep(1)
    mock_s3.put_object(
        Bucket="test-bucket",
        Key="folder1/test_file_2.txt", Body="test_string2")
    time.sleep(1)
    mock_s3.put_object(
        Bucket="test-bucket",
        Key="folder1/test_file_3.txt", Body="test_string2")
    result = get_most_recent_file_2(mock_s3, "test-bucket", "folder1")
    assert result == "folder1/test_file_3.txt"
