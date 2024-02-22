from src.transform_handler2.utils_lambda2.get_file_name import get_file_name
import pytest


@pytest.fixture
def mock_bucket(mock_s3):
    mock_s3.create_bucket(
        Bucket='test-bucket',
        CreateBucketConfiguration={'LocationConstraint': 'eu-west-2'})


@pytest.mark.describe("get_the_file_name")
@pytest.mark.it("Test returns correct str")
def test_get_file_name_return_correct_str():
    s3_object_key = 'testing/testing-2024-02-15-01-01-15.csv'
    expected_file_name = 'testing-2024-02-15-01-01-15'
    result = get_file_name(s3_object_key)
    assert result == expected_file_name


@pytest.mark.describe("get_the_file_name")
@pytest.mark.it("Test returns str")
def test_get_file_name_return_correct_name():
    s3_object_key = 'testing/testing-2024-02-15-01-01-15.csv'
    result = get_file_name(s3_object_key)
    assert type(result) is str
