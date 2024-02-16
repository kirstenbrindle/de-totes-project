from src.utils.get_most_recent_file import get_most_recent_file
import pytest
from unittest.mock import Mock, patch
from moto import mock_aws
import boto3
from pprint import pprint
from datetime import datetime
import time


@mock_aws
def test_returns_type_of_string():
    """
    checks returns string
    """
    session = boto3.session.Session()
    mockedClient = session.client(service_name="s3")
    mockedClient.create_bucket(Bucket="test_bucket", CreateBucketConfiguration={
                               'LocationConstraint': 'eu-west-2'})
    mockedClient.put_object(Bucket="test_bucket",
                            Key="folder1/test_file_1.txt", Body="test_string")
    mockedClient.put_object(Bucket="test_bucket",
                            Key="folder1/test_file_2.txt", Body="test_string2")
    mockedClient.put_object(Bucket="test_bucket",
                            Key="folder2/test_file_3.txt", Body="test_string3")
    result = get_most_recent_file(mockedClient, "folder1")
    assert type(result) == str


@mock_aws
def test_returns_file_name_in_folder():
    """
    checks returns most recent filename as string 
    """
    session = boto3.session.Session()
    mockedClient = session.client(service_name="s3")
    mockedClient.create_bucket(Bucket="test_bucket", CreateBucketConfiguration={
                               'LocationConstraint': 'eu-west-2'})
    mockedClient.put_object(Bucket="test_bucket",
                            Key="folder1/test_file_1.txt", Body="test_string")
    time.sleep(1)
    mockedClient.put_object(Bucket="test_bucket",
                            Key="folder1/test_file_2.txt", Body="test_string2")
    mockedClient.put_object(Bucket="test_bucket",
                            Key="folder1/test_file_3.txt", Body="test_string2")
    result = get_most_recent_file(mockedClient, "folder1")
    assert result == "folder1/test_file_2.txt"


@mock_aws
def test_returns_file_name_in_folder_with_multiple_files_with_differing_last_updated_times():
    """
    checks returns most recent filename as string 
    """
    session = boto3.session.Session()
    mockedClient = session.client(service_name="s3")
    mockedClient.create_bucket(Bucket="test_bucket", CreateBucketConfiguration={
                               'LocationConstraint': 'eu-west-2'})
    mockedClient.put_object(Bucket="test_bucket",
                            Key="folder1/test_file_1.txt", Body="test_string")
    time.sleep(1)
    mockedClient.put_object(Bucket="test_bucket",
                            Key="folder1/test_file_2.txt", Body="test_string2")
    time.sleep(1)
    mockedClient.put_object(Bucket="test_bucket",
                            Key="folder1/test_file_3.txt", Body="test_string2")
    result = get_most_recent_file(mockedClient, "folder1")
    assert result == "folder1/test_file_3.txt"
