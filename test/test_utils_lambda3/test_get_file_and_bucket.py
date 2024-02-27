from src.load_handler3.get_file_and_bucket import (
    get_file_and_bucket)
import pytest


@pytest.mark.describe("get_the_file_name")
@pytest.mark.it("Test returns correct processed bucket name")
def test_get_file_name_return_bucket_name_from_processed_bucket():
    event = {
        "Records": [
            {
                "s3": {
                    "bucket": {
                        "name": "test-bucket"
                    },
                    "object": {
                        "key": "testtable/currency/2022-2-27+11%3A00.parquet"
                    }
                }
            }
        ],
    }
    expected = 'test-bucket'
    result = get_file_and_bucket(event['Records'])
    assert result[0] == expected


@pytest.mark.describe("get_the_file_name")
@pytest.mark.it("Test returns correct file name")
def test_get_file_name_returns_correct_processed_file_name():
    event = {
        "Records": [
            {
                "s3": {
                    "bucket": {
                        "name": "test-bucket"
                    },
                    "object": {
                        "key": "testtable/currency/2022-2-27+11%3A00.parquet"
                    }
                }
            }
        ],
    }
    expected = 'testtable/currency/2022-2-27 11:00.parquet'
    result = get_file_and_bucket(event['Records'])
    assert result[1] == expected
