import pytest
from unittest.mock import patch
from moto import mock_aws
import os
import boto3
from src.transform_handler2.transform_handler2 import lambda_handler


@pytest.fixture(scope='function')
def aws_credentials():
    """Mocked AWS Credentials for moto."""
    os.environ["AWS_ACCESS_KEY_ID"] = "test"
    os.environ["AWS_SECRET_ACCESS_KEY"] = "test"
    os.environ["AWS_SECURITY_TOKEN"] = "test"
    os.environ["AWS_SESSION_TOKEN"] = "test"
    os.environ["AWS_DEFAULT_REGION"] = "eu-west-2"


@pytest.fixture(scope='function')
def s3(aws_credentials):
    """Mocked s3 connection for tests"""
    s3 = boto3.client('s3')
    return s3


@pytest.fixture
def mock_bucket_pro(mock_s3):
    mock_s3.create_bucket(
        Bucket='processed_bucket',
        CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})


@pytest.fixture
def patch_fixture():
    with patch("src.transform_handler2.transform_handler2.get_file_and_ingestion_bucket_name")\
            as mock_gfaibn, \
        patch("src.transform_handler2.transform_handler2.get_bucket_name_2")\
            as mock_gbn2, \
        patch("src.transform_handler2.transform_handler2.is_bucket_empty_2")\
            as mock_ibe2, \
        patch("src.transform_handler2.transform_handler2.get_most_recent_file_2")\
            as mock_gmrf2, \
        patch("src.transform_handler2.transform_handler2.read_csv_to_df")\
            as mock_rctd, \
        patch("src.transform_handler2.transform_handler2.csv_parquet_converter")\
            as mock_cpc:
        yield (mock_gfaibn, mock_gbn2, mock_ibe2, mock_gmrf2, mock_rctd, mock_cpc)


@pytest.mark.describe("lambda_handler2")
@pytest.mark.it("""Test lambda_handler2 invokes
                get_file_and_ingestion_bucket_name""")
@patch(
    "src.transform_handler2.transform_handler2."
    "get_file_and_ingestion_bucket_name")
@mock_aws
def test_lambda_handler2_invokes_gfaibn(patch_fixture, s3):
    (mock_gfaibn, mock_gbn2, mock_ibe2, mock_gmrf2,
     mock_rctd, mock_cpc) = patch_fixture
    mock_gfaibn.return_value = 'ingestion-bucket', 'test.csv'
    mock_gbn2.return_value = 'processed-bucket'
    assert mock_gfaibn.call_count == 0
    lambda_handler({}, {})
    assert mock_gfaibn.call_count == 1


@pytest.mark.skip
@pytest.mark.describe("lambda_handler2")
@pytest.mark.it("""Test lambda_handler2 invokes
                get_bucket_name_2""")
@patch("src.transform_handler2.transform_handler2."
       "get_file_and_ingestion_bucket_name")
@patch("src.transform_handler2.transform_handler2."
       "get_bucket_name_2")
@mock_aws
def test_lambda_handler2_invokes_gbn2(mock_bucket_pro, mock_gbn2, mock_gfaibn):
    mock_gfaibn.return_value = 'ingestion_Bucket', 'filename'
    mock_gbn2.return_value = 'processed_bucket'
    assert mock_gbn2.call_count == 0
    lambda_handler({'Records': 'ello'}, {})
    assert mock_gbn2.call_count == 1
