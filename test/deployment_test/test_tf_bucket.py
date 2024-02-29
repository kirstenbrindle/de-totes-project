from src.setup.tf_bucket import bucket_maker
from moto import mock_aws
from unittest.mock import patch
import pytest
import boto3


@pytest.mark.describe('bucket_maker')
@pytest.mark.it('test it creates a new bucket')
@mock_aws
@patch('builtins.input', return_value="test_bucket_43754852")
def test_a_new_bucket_is_created(mock_input):
    """
    Given:
    bucket_maker is invoked

    Returns:
    No return. Check a bucket has been created using a mock s3 connection.
    """
    s3 = boto3.client("s3")
    response_before_function = s3.list_buckets()
    assert len(response_before_function['Buckets']) == 0
    bucket_maker()
    response_after_function = s3.list_buckets()
    assert len(response_after_function['Buckets']) == 1


@pytest.mark.describe('bucket_maker')
@pytest.mark.it('test it creates a new bucket with correct name')
@mock_aws
@patch('builtins.input', return_value="test_bucket_43754852")
def test_a_new_bucket_is_created_with_input_name(mock_input):
    """
    Given:
    bucket_maker is invoked

    Returns:
    No return. Check a bucket with the correct name has been
    created using a mock s3 connection.
    """
    s3 = boto3.client("s3")
    bucket_maker()
    response = s3.list_buckets()
    assert response['Buckets'][0]['Name'] == mock_input.return_value
