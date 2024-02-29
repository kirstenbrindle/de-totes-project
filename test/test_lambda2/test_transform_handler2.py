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
def mock_s3(aws_credentials):
    """Mocked s3 connection for tests"""
    mock_s3 = boto3.client('s3')
    return mock_s3


@pytest.fixture
def patch_fixture():
    with patch("src.transform_handler2.transform_handler2."
               "get_file_and_ingestion_bucket_name")\
        as get_file_ing_bucket, \
         patch("src.transform_handler2.transform_handler2.get_bucket_name_2")\
            as get_pro_bucket, \
         patch("src.transform_handler2.transform_handler2.read_csv_to_df")\
            as read_csv, \
         patch("src.transform_handler2.transform_handler2.write_to_parquet")\
            as write_parquet:
        yield (get_file_ing_bucket, get_pro_bucket,
               read_csv, write_parquet)


@pytest.mark.describe("lambda_handler2")
@pytest.mark.it("Test lambda_handler2 invokes "
                "get_file_and_ingestion_bucket_name")
@mock_aws
def test_lambda_handler2_invokes_get_file_ing_bucket(patch_fixture, mock_s3):
    """
    Given:
    lambda_handler is invoked by an s3 put object event

    Returns:
    No return. Check get_file_and_ingestion_bucket_name 
    util function is invoked
    """
    (get_file_ing_bucket, get_pro_bucket,
     read_csv, write_parquet) = patch_fixture
    get_file_ing_bucket.return_value = 'ingestion-bucket', 'test.csv'
    assert get_file_ing_bucket.call_count == 0
    lambda_handler({'Records': 'test'}, {})
    assert get_file_ing_bucket.call_count == 1


@pytest.mark.describe("lambda_handler2")
@pytest.mark.it("Test lambda_handler2 invokes get_bucket_name_2")
@mock_aws
def test_lambda_handler2_invokes_get_pro_bucket(patch_fixture, mock_s3):
    """
    Given:
    lambda_handler is invoked by an s3 put object event

    Returns:
    No return. Check get_bucket_name_2 util function is invoked
    """
    (get_file_ing_bucket, get_pro_bucket,
     read_csv, write_parquet) = patch_fixture
    get_file_ing_bucket.return_value = 'ingestion-bucket', 'test.csv'
    assert get_pro_bucket.call_count == 0
    lambda_handler({'Records': 'test'}, {})
    assert get_pro_bucket.call_count == 1


@pytest.mark.describe("lambda_handler2")
@pytest.mark.it("Test lambda_handler2 invokes read_csv_to_df if no error")
@mock_aws
def test_lambda_handler2_invokes_read_csv(patch_fixture, mock_s3):
    """
    Given:
    lambda_handler is invoked by an s3 put object event

    Returns:
    No return. Check read_csv_to_df util function is invoked
    if no errors
    """
    (get_file_ing_bucket, get_pro_bucket,
     read_csv, write_parquet) = patch_fixture
    get_file_ing_bucket.return_value = 'ingestion_Bucket', 'sales_order'
    assert read_csv.call_count == 0
    lambda_handler({'Records': 'test'}, {})
    assert read_csv.call_count == 1


@pytest.mark.describe("lambda_handler2")
@pytest.mark.it("Test lambda_handler2 invokes write_to_parquet if no error")
@mock_aws
def test_lambda_handler2_invokes_write_parquet(patch_fixture, mock_s3):
    """
    Given:
    lambda_handler is invoked by an s3 put object event

    Returns:
    No return. Check write_to_parquet util function is invoked
    if no errors
    """
    (get_file_ing_bucket, get_pro_bucket,
     read_csv, write_parquet) = patch_fixture
    get_file_ing_bucket.return_value = 'ingestion_Bucket', 'sales_order'
    assert write_parquet.call_count == 0
    lambda_handler({'Records': 'test'}, {})
    assert write_parquet.call_count == 1


@pytest.mark.describe("lambda_handler2")
@pytest.mark.it("Test lambda_handler2 invokes correct formatting function")
@patch("src.transform_handler2.transform_handler2.make_fact_sales_order")
@patch("src.transform_handler2.transform_handler2.make_dim_design")
@mock_aws
def test_lambda_handler2_invokes_formatting_function(
        dim_design, fact_sales, patch_fixture, mock_s3):
    """
    Given:
    lambda_handler is invoked by an s3 put object event

    Returns:
    No return. Check formatting util function relating to the correct
    data warehouse table is invoked if no errors
    """
    (get_file_ing_bucket, get_pro_bucket,
     read_csv, write_parquet) = patch_fixture
    get_file_ing_bucket.return_value = 'ingestion_Bucket', 'sales_order'
    assert fact_sales.call_count == 0
    lambda_handler({'Records': 'test'}, {})
    assert fact_sales.call_count == 1
    assert dim_design.call_count == 0
    get_file_ing_bucket.return_value = 'ingestion_Bucket', 'design'
    lambda_handler({'Records': 'test'}, {})
    assert dim_design.call_count == 1


@pytest.mark.describe("lambda_handler2")
@pytest.mark.it("Test lambda_handler2 writes dim_date file "
                "if currency is invoked")
@patch("src.transform_handler2.transform_handler2.make_dim_currency")
@patch("src.transform_handler2.transform_handler2.make_dim_date")
@mock_aws
def test_lambda_handler2_invokes_dim_date(
        dim_date, dim_curr, patch_fixture, mock_s3):
    """
    Given:
    lambda_handler is invoked by an s3 put object event to the 'currency'
    sub-folder

    Returns:
    No return. Check make_dim_date util function is invoked
    """
    (get_file_ing_bucket, get_pro_bucket,
     read_csv, write_parquet) = patch_fixture
    get_file_ing_bucket.return_value = 'ingestion_Bucket', 'currency'
    assert dim_curr.call_count == 0
    assert dim_date.call_count == 0
    lambda_handler({'Records': 'test'}, {})
    assert dim_curr.call_count == 1
    assert dim_date.call_count == 1


@pytest.mark.describe("lambda_handler2")
@pytest.mark.it("Test lambda_handler2 invokes get most recent file "
                "for staff or counterparty")
@patch("src.transform_handler2.transform_handler2.get_most_recent_file_2")
@patch("src.transform_handler2.transform_handler2.make_dim_counterparty")
@patch("src.transform_handler2.transform_handler2.make_dim_staff")
@mock_aws
def test_lambda_handler2_invokes_get_most_recent_file_2(
        dim_staff, dim_cp, get_file, patch_fixture, mock_s3):
    """
    Given:
    lambda_handler is invoked by an s3 put object event to the 'counterparty'
    or 'staff' sub-folder

    Returns:
    No return. Check get_most_recent_file_2 util function is invoked
    """
    (get_file_ing_bucket, get_pro_bucket,
     read_csv, write_parquet) = patch_fixture
    get_file_ing_bucket.return_value = 'ingestion_Bucket', 'counterparty'
    assert dim_cp.call_count == 0
    assert get_file.call_count == 0
    lambda_handler({'Records': 'test'}, {})
    assert dim_cp.call_count == 1
    assert get_file.call_count == 1
    assert dim_staff.call_count == 0
    get_file_ing_bucket.return_value = 'ingestion_Bucket', 'staff'
    lambda_handler({'Records': 'test'}, {})
    assert dim_staff.call_count == 1
    assert get_file.call_count == 2


@pytest.mark.describe("lambda_handler2")
@pytest.mark.it("Test logs message if not a MVP table")
@mock_aws
def test_get_bucket_name_error(patch_fixture, mock_s3, caplog):
    (get_file_ing_bucket, get_pro_bucket,
     read_csv, write_parquet) = patch_fixture
    """
    Given:
    lambda_handler is invoked by an s3 put object event to a
    sub-folder for a non-MVP table

    Returns:
    Logs an info message to inform that no update is needed
    """
    get_file_ing_bucket.return_value = 'ingestion_Bucket', 'nonsense'
    lambda_handler({'Records': 'test'}, {})
    assert "Non-MVP data: update not needed" in caplog.text
    assert "INFO" in caplog.text
