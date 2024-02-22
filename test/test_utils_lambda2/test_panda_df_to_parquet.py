from src.transform_handler2.panda_df_to_parquet import csv_parquet_converter
import pytest
from moto import mock_aws
import boto3
import pandas as pd

data = {
    'name': ['Xavier', 'Ann', 'Jana', 'Yi', 'Robin', 'Amal', 'Nori'],
    'city': ['Mexico City', 'Toronto', 'Prague', 'Shanghai',
             'Manchester', 'Cairo', 'Osaka'],
    'age': [41, 28, 33, 34, 38, 31, 37],
    'py-score': [88.0, 79.0, 81.0, 80.0, 68.0, 61.0, 84.0]
}
row_labels = [101, 102, 103, 104, 105, 106, 107]


df = pd.DataFrame(data=data, index=row_labels)


@mock_aws
def test_uploads_a_file_to_s3():

    session = boto3.session.Session()
    mockedClient = session.client(service_name="s3")
    mockedClient.create_bucket(
        Bucket="test_bucket", CreateBucketConfiguration={
            'LocationConstraint': 'eu-west-2'})

    csv_parquet_converter(mockedClient, 'test_bucket', 'table1', df)

    assert 'table1/table1' in f"{mockedClient.list_objects_v2(Bucket='test_bucket',)}"


@mock_aws
def test_uploads_a_parquet_file_to_s3():

    session = boto3.session.Session()
    mockedClient = session.client(service_name="s3")
    mockedClient.create_bucket(
        Bucket="test_bucket", CreateBucketConfiguration={
            'LocationConstraint': 'eu-west-2'})

    csv_parquet_converter(mockedClient, 'test_bucket', 'table1', df)

    assert '.parquet' in f"{mockedClient.list_objects_v2(Bucket='test_bucket', Prefix='table1')}"

