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


@pytest.mark.describe("lambda_handler2")
@pytest.mark.it("""Test lambda_handler2 invokes
                get_file_and_ingestion_bucket_name""")
@patch("src.transform_handler2.transform_handler2."
       "get_file_and_ingestion_bucket_name")
@patch("src.transform_handler2.transform_handler2."
       "get_bucket_name_2")
@patch("src.transform_handler2.transform_handler2."
       "is_bucket_empty_2")
@patch("src.transform_handler2.transform_handler2."
       "get_most_recent_file_2")
@patch("src.transform_handler2.transform_handler2."
       "read_csv_to_df")
@patch("src.transform_handler2.transform_handler2."
       "make_fact_sales_order")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_design")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_location")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_currency")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_staff")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_date")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_counterparty")
@patch("src.transform_handler2.transform_handler2."
       "write_to_parquet")
@mock_aws
def test_lambda_handler2_invokes_gfaibn(
        mock_wtp, dim_cp, dim_date, dim_staff, dim_cur, dim_loc,
        dim_design, mock_sales, mock_rcsvdf, mock_gmrf2,
        mock_ibe2, mock_gbn2, mock_gfaibn, mock_s3):
    mock_gfaibn.return_value = 'ingestion-bucket', 'test.csv'
    mock_gbn2.return_value = 'processed-bucket'
    assert mock_gfaibn.call_count == 0
    lambda_handler({'Records': 'test'}, {})
    assert mock_gfaibn.call_count == 1


@pytest.mark.describe("lambda_handler2")
@pytest.mark.it("""Test lambda_handler2 invokes
                get_bucket_name_2""")
@patch("src.transform_handler2.transform_handler2."
       "get_file_and_ingestion_bucket_name")
@patch("src.transform_handler2.transform_handler2."
       "get_bucket_name_2")
@patch("src.transform_handler2.transform_handler2."
       "is_bucket_empty_2")
@patch("src.transform_handler2.transform_handler2."
       "get_most_recent_file_2")
@patch("src.transform_handler2.transform_handler2."
       "read_csv_to_df")
@patch("src.transform_handler2.transform_handler2."
       "make_fact_sales_order")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_design")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_location")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_currency")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_staff")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_date")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_counterparty")
@patch("src.transform_handler2.transform_handler2."
       "write_to_parquet")
@mock_aws
def test_lambda_handler2_invokes_gbn2(
        mock_wtp, dim_cp, dim_date, dim_staff, dim_cur, dim_loc,
        dim_design, mock_sales, mock_rcsvdf, mock_gmrf2,
        mock_ibe2, mock_gbn2, mock_gfaibn, mock_s3):
    mock_gfaibn.return_value = 'ingestion_Bucket', 'filename'
    mock_gbn2.return_value = 'processed_bucket'
    assert mock_gbn2.call_count == 0
    lambda_handler({'Records': 'test'}, {})
    assert mock_gbn2.call_count == 1


@pytest.mark.describe("lambda_handler2")
@pytest.mark.it("""Test lambda_handler2 invokes
                is_bucket_empty_2""")
@patch("src.transform_handler2.transform_handler2."
       "get_file_and_ingestion_bucket_name")
@patch("src.transform_handler2.transform_handler2."
       "get_bucket_name_2")
@patch("src.transform_handler2.transform_handler2."
       "is_bucket_empty_2")
@patch("src.transform_handler2.transform_handler2."
       "get_most_recent_file_2")
@patch("src.transform_handler2.transform_handler2."
       "read_csv_to_df")
@patch("src.transform_handler2.transform_handler2."
       "make_fact_sales_order")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_design")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_location")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_currency")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_staff")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_date")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_counterparty")
@patch("src.transform_handler2.transform_handler2."
       "write_to_parquet")
@mock_aws
def test_lambda_handler2_invokes_ibe2(
        mock_wtp, dim_cp, dim_date, dim_staff, dim_cur, dim_loc,
        dim_design, mock_sales, mock_rcsvdf, mock_gmrf2,
        mock_ibe2, mock_gbn2, mock_gfaibn, mock_s3):
    mock_gfaibn.return_value = 'ingestion_Bucket', 'filename'
    mock_gbn2.return_value = 'processed_bucket'
    mock_ibe2.return_value = True
    assert mock_ibe2.call_count == 0
    lambda_handler({'Records': 'test'}, {})
    assert mock_ibe2.call_count == 1


@pytest.mark.describe("lambda_handler2")
@pytest.mark.it("""Test lambda_handler2 invokes
                get_most_recent_file_2 if boolean is True""")
@patch("src.transform_handler2.transform_handler2."
       "get_file_and_ingestion_bucket_name")
@patch("src.transform_handler2.transform_handler2."
       "get_bucket_name_2")
@patch("src.transform_handler2.transform_handler2."
       "is_bucket_empty_2")
@patch("src.transform_handler2.transform_handler2."
       "get_most_recent_file_2")
@patch("src.transform_handler2.transform_handler2."
       "read_csv_to_df")
@patch("src.transform_handler2.transform_handler2."
       "make_fact_sales_order")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_design")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_location")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_currency")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_staff")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_date")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_counterparty")
@patch("src.transform_handler2.transform_handler2."
       "write_to_parquet")
@mock_aws
def test_lambda_handler2_invokes_gmrf2_if_true(
        mock_wtp, dim_cp, dim_date, dim_staff, dim_cur, dim_loc,
        dim_design, mock_sales, mock_rcsvdf, mock_gmrf2,
        mock_ibe2, mock_gbn2, mock_gfaibn, mock_s3):
    mock_gfaibn.return_value = 'ingestion_Bucket', 'filename'
    mock_gbn2.return_value = 'processed_bucket'
    mock_ibe2.return_value = True
    mock_gmrf2.return_value = 'test/test-2328436473'
    assert mock_gmrf2.call_count == 0
    lambda_handler({'Records': 'test'}, {})
    assert mock_gmrf2.call_count == 7


@pytest.mark.describe("lambda_handler2")
@pytest.mark.it("""Test lambda_handler2 invokes
                read_csv_to_df if boolean is True""")
@patch("src.transform_handler2.transform_handler2."
       "get_file_and_ingestion_bucket_name")
@patch("src.transform_handler2.transform_handler2."
       "get_bucket_name_2")
@patch("src.transform_handler2.transform_handler2."
       "is_bucket_empty_2")
@patch("src.transform_handler2.transform_handler2."
       "get_most_recent_file_2")
@patch("src.transform_handler2.transform_handler2."
       "read_csv_to_df")
@patch("src.transform_handler2.transform_handler2."
       "make_fact_sales_order")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_design")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_location")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_currency")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_staff")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_date")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_counterparty")
@patch("src.transform_handler2.transform_handler2."
       "write_to_parquet")
@mock_aws
def test_lambda_handler2_invokes_rcsvdf_if_true(
        mock_wtp, dim_cp, dim_date, dim_staff, dim_cur, dim_loc,
        dim_design, mock_sales, mock_rcsvdf, mock_gmrf2,
        mock_ibe2, mock_gbn2, mock_gfaibn, mock_s3):
    mock_gfaibn.return_value = 'ingestion_Bucket', 'filename'
    mock_gbn2.return_value = 'processed_bucket'
    mock_ibe2.return_value = True
    mock_gmrf2.return_value = 'test/test-2328436473'
    assert mock_rcsvdf.call_count == 0
    lambda_handler({'Records': 'test'}, {})
    assert mock_rcsvdf.call_count == 7


@pytest.mark.describe("lambda_handler2")
@pytest.mark.it("""Test lambda_handler2 invokes
                format functions if boolean is True""")
@patch("src.transform_handler2.transform_handler2."
       "get_file_and_ingestion_bucket_name")
@patch("src.transform_handler2.transform_handler2."
       "get_bucket_name_2")
@patch("src.transform_handler2.transform_handler2."
       "is_bucket_empty_2")
@patch("src.transform_handler2.transform_handler2."
       "get_most_recent_file_2")
@patch("src.transform_handler2.transform_handler2."
       "read_csv_to_df")
@patch("src.transform_handler2.transform_handler2."
       "make_fact_sales_order")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_design")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_location")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_currency")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_staff")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_date")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_counterparty")
@patch("src.transform_handler2.transform_handler2."
       "write_to_parquet")
@mock_aws
def test_lambda_handler2_invokes_formatting_functions(
        mock_wtp, dim_cp, dim_date, dim_staff, dim_cur, dim_loc,
        dim_design, mock_sales, mock_rcsvdf, mock_gmrf2,
        mock_ibe2, mock_gbn2, mock_gfaibn, mock_s3):
    mock_gfaibn.return_value = 'ingestion_Bucket', 'filename'
    mock_gbn2.return_value = 'processed_bucket'
    mock_ibe2.return_value = True
    mock_gmrf2.return_value = 'test/test-2328436473'
    lambda_handler({'Records': 'test'}, {})
    assert mock_sales.call_count == 1
    assert dim_design.call_count == 1
    assert dim_loc.call_count == 1
    assert dim_cur.call_count == 1
    assert dim_staff.call_count == 1
    assert dim_date.call_count == 1
    assert dim_cp.call_count == 1


@pytest.mark.describe("lambda_handler2")
@pytest.mark.it("""Test lambda_handler2 invokes
                write_to_parquet if boolean is True""")
@patch("src.transform_handler2.transform_handler2."
       "get_file_and_ingestion_bucket_name")
@patch("src.transform_handler2.transform_handler2."
       "get_bucket_name_2")
@patch("src.transform_handler2.transform_handler2."
       "is_bucket_empty_2")
@patch("src.transform_handler2.transform_handler2."
       "get_most_recent_file_2")
@patch("src.transform_handler2.transform_handler2."
       "read_csv_to_df")
@patch("src.transform_handler2.transform_handler2."
       "make_fact_sales_order")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_design")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_location")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_currency")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_staff")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_date")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_counterparty")
@patch("src.transform_handler2.transform_handler2."
       "write_to_parquet")
@mock_aws
def test_lambda_handler2_invokes_mock_wtp(
        mock_wtp, dim_cp, dim_date, dim_staff, dim_cur, dim_loc,
        dim_design, mock_sales, mock_rcsvdf, mock_gmrf2,
        mock_ibe2, mock_gbn2, mock_gfaibn, mock_s3):
    mock_gfaibn.return_value = 'ingestion_Bucket', 'filename'
    mock_ibe2.return_value = True
    lambda_handler({'Records': 'test'}, {})
    assert mock_wtp.call_count == 7


@pytest.mark.describe("lambda_handler2")
@pytest.mark.it("""Test lambda_handler2 invokes
                correct funcs if new sales data and
                if boolean is False""")
@patch("src.transform_handler2.transform_handler2."
       "get_file_and_ingestion_bucket_name")
@patch("src.transform_handler2.transform_handler2."
       "get_bucket_name_2")
@patch("src.transform_handler2.transform_handler2."
       "is_bucket_empty_2")
@patch("src.transform_handler2.transform_handler2."
       "read_csv_to_df")
@patch("src.transform_handler2.transform_handler2."
       "make_fact_sales_order")
@patch("src.transform_handler2.transform_handler2."
       "write_to_parquet")
@mock_aws
def test_lambda_handler2_with_new_sales_data(
        mock_wtp, mock_sales, mock_rcsvdf,
        mock_ibe2, mock_gbn2, mock_gfaibn, mock_s3):
    mock_gfaibn.return_value = 'ingestion_Bucket', 'sales_order'
    mock_ibe2.return_value = False
    lambda_handler({'Records': 'test'}, {})
    assert mock_rcsvdf.call_count == 1
    assert mock_sales.call_count == 1
    assert mock_wtp.call_count == 1


@pytest.mark.describe("lambda_handler2")
@pytest.mark.it("""Test lambda_handler2 invokes
                correct funcs if new design data and
                if boolean is False""")
@patch("src.transform_handler2.transform_handler2."
       "get_file_and_ingestion_bucket_name")
@patch("src.transform_handler2.transform_handler2."
       "get_bucket_name_2")
@patch("src.transform_handler2.transform_handler2."
       "is_bucket_empty_2")
@patch("src.transform_handler2.transform_handler2."
       "read_csv_to_df")
@patch("src.transform_handler2.transform_handler2."
       "make_dim_design")
@patch("src.transform_handler2.transform_handler2."
       "write_to_parquet")
@mock_aws
def test_lambda_handler2_with_new_design_data(
        mock_wtp, mock_design, mock_rcsvdf,
        mock_ibe2, mock_gbn2, mock_gfaibn, mock_s3):
    mock_gfaibn.return_value = 'ingestion_Bucket', 'design/design-4348'
    mock_ibe2.return_value = False
    lambda_handler({'Records': 'test'}, {})
    assert mock_rcsvdf.call_count == 1
    assert mock_design.call_count == 1
    assert mock_wtp.call_count == 1
