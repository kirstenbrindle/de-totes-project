import boto3
import pytest
import os
from moto import mock_aws
from src.utils_lambda1.write_csv import write_csv
from datetime import datetime
from unittest.mock import patch


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


@pytest.mark.describe('writes csv file')
@pytest.mark.it("writes a csv file to bucket "
                "with folder when passed a table_name")
@patch('src.utils_lambda1.write_csv.datetime')
def test_writes_csv_file_with_folder(mock_datetime, mock_bucket, mock_s3):
    mock_datetime.now.side_effect = [datetime(2024, 2, 15, 1, 1, 15)]
    table_name = 'testing'
    bucket = 'test-bucket'
    data = {
        'payment_type_id': [1],
        'payment_type_name': ['SALES_RECEIPT'],
        'created_at': ["2022-11-03 14:20:49.962"],
        'last_updated': ["2022-11-03 14:20:49.962"]
    }
    write_csv(table_name, bucket, mock_s3, data)
    response = mock_s3.list_objects_v2(Bucket=bucket)
    listed_objects = [file['Key'] for file in response['Contents']]
    assert listed_objects == [
        f'testing/testing-{datetime(2024,2,15,1,1,15)}.csv']


@pytest.mark.describe('writes csv file')
@pytest.mark.it("writes the correct content to "
                "a csv file to the correct bucket")
@patch('src.utils_lambda1.write_csv.datetime')
def test_writes_csv_file_in_folder(mock_datetime, mock_bucket, mock_s3):
    mock_datetime.now.side_effect = [datetime(2024, 2, 15, 1, 1, 15)]
    table_name = 'testing'
    bucket = 'test-bucket'
    data = {'payment_type_id': [1],
            'payment_type_name': ['SALES_RECEIPT'],
            'created_at': ["2022-11-03 14:20:49.962"],
            'last_updated': ["2022-11-03 14:20:49.962"]
            }
    write_csv(table_name, bucket, mock_s3, data)
    response = mock_s3.get_object(
        Bucket=bucket, Key=f'testing/testing-{datetime(2024,2,15,1,1,15)}.csv')
    result = response['Body']
    readable_result = result.read()
    decoded_result = readable_result.decode('utf-8')
    assert decoded_result == (
        ',payment_type_id,payment_type_name,created_at,last_updated\n'
        '0,1,SALES_RECEIPT,2022-11-03 14:20:49.962,2022-11-03 14:20:49.962\n')


@pytest.mark.describe('writes csv file')
@pytest.mark.it('writes multiple csv files to the same folder')
@patch('src.utils_lambda1.write_csv.datetime')
def test_writes_csv_file_to_same_folder(mock_datetime, mock_bucket, mock_s3):
    mock_datetime.now.side_effect = [
        datetime(2024, 2, 15, 1, 1, 15), datetime(2024, 2, 16, 1, 1, 10)]
    table_name = 'testing'
    bucket = 'test-bucket'
    data = {
        'payment_type_id': [1],
        'payment_type_name': ['SALES_RECEIPT'],
        'created_at': ["2022-11-03 14:20:49.962"],
        'last_updated': ["2022-11-03 14:20:49.962"]
    }
    write_csv(table_name, bucket, mock_s3, data)
    data1 = {
        'payment_type_id': [2],
        'payment_type_name': ['REFUND_RECEIPT'],
        'created_at': ["2022-11-03 14:20:49.900"],
        'last_updated': ["2022-11-03 14:20:49.900"]
    }
    write_csv(table_name, bucket, mock_s3, data1)
    response = mock_s3.list_objects_v2(Bucket=bucket)
    listed_objects = [file['Key'] for file in response['Contents']]
    assert listed_objects == [
        f'testing/testing-{datetime(2024,2,15,1,1,15)}.csv',
        f'testing/testing-{datetime(2024, 2, 16, 1, 1, 10)}.csv']


@pytest.mark.describe('writes csv file')
@pytest.mark.it('writes multiple csv files to different folders')
@patch('src.utils_lambda1.write_csv.datetime')
def test_writes_csv_file_to_diff_folder(mock_datetime, mock_bucket, mock_s3):
    mock_datetime.now.side_effect = [
        datetime(2024, 2, 15, 1, 1, 15), datetime(2024, 2, 16, 1, 1, 10)]
    table_name = 'testing'
    bucket = 'test-bucket'
    data = {
        'payment_type_id': [1],
        'payment_type_name': ['SALES_RECEIPT'],
        'created_at': ["2022-11-03 14:20:49.962"],
        'last_updated': ["2022-11-03 14:20:49.962"]
    }
    write_csv(table_name, bucket, mock_s3, data)
    table_name1 = 'mock'
    data1 = {
        'payment_type_id': [2],
        'payment_type_name': ['REFUND_RECEIPT'],
        'created_at': ["2022-11-03 14:20:49.900"],
        'last_updated': ["2022-11-03 14:20:49.900"]
    }
    write_csv(table_name1, bucket, mock_s3, data1)
    response = mock_s3.list_objects_v2(Bucket=bucket)
    listed_objects = [file['Key'] for file in response['Contents']]
    # needs to be in alphabetical order!!
    assert listed_objects == [
        f'mock/mock-{datetime(2024, 2, 16, 1, 1, 10)}.csv',
        f'testing/testing-{datetime(2024,2,15,1,1,15)}.csv']
