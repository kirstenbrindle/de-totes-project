# from src.load_handler3.read_parquet import read_parquet
# from pg8000.native import Connection
# from unittest.mock import patch, MagicMock
# import pytest
# import logging
# import os
# from moto import mock_aws
# import boto3


# logger = logging.getLogger('test')
# logger.setLevel(logging.INFO)
# logger.propagate = True


# @pytest.fixture(scope="function")
# def aws_credentials():
#     """Mocked AWS Credentials for moto"""
#     os.environ["AWS_ACCESS_KEY_ID"] = "testing"
#     os.environ["AWS_SECRET_ACCESS_KEY"] = "testing"
#     os.environ["AWS_SECURITY_TOKEN"] = "testing"
#     os.environ["AWS_SESSION_TOKEN"] = "testing"
#     os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


# @pytest.fixture
# def mock_s3(aws_credentials):
#     with mock_aws():
#         yield boto3.client("s3", region_name='eu-west-2')


# @pytest.fixture
# def mock_bucket(mock_s3):
#     mock_s3.create_bucket(
#         Bucket='test-bucket',
#         CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})


# @pytest.fixture(scope='function')
# def db_conn():
#     """Connection to test_warehouse"""
#     user = 'leah'
#     password = 'password'
#     host = 'localhost'
#     database = 'test_warehouse'
#     return Connection(user=user, password=password,
#                       host=host, database=database)


# @pytest.mark.describe("read_parquet")
# @pytest.mark.it("test pandas read method is invoked")
# def test_reads_method_is_invoked(mock_s3, mock_bucket, db_conn):
#     mock_s3.upload_file('test/test_parquet_file/test-pq.parquet',
#                         'test-bucket', 'test/test-pq.parquet')
#     read_parquet(mock_s3, 'test-bucket',
# 'test_currency', db_conn, 'test/test-pq.parquet')
#     query = db_conn.run('SELECT * FROM test_currency')
#     assert query == [[1, 'GBP', 'British pound sterling'],
#                      [2, 'USD', 'United States dollar'],
#                      [3, 'EUR', 'Euro']]
