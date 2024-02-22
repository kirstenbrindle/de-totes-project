from src.transform_handler2.get_file_and_ingestion_bucket_name import get_file_and_ingestion_bucket_name
import pytest


@pytest.mark.describe("get_the_file_name")
@pytest.mark.it("Test returns correct bucket name")
def test_get_file_name_return_bucket_name():
    event = {
        "Records": [
            {
                "s3": {
                    "bucket": {
                        "name": "test-bucket"
                    },
                    "object": {
                        "key": "test.csv"
                    }
                }
            }
        ],
    }
    expected = 'test-bucket'
    result = get_file_and_ingestion_bucket_name(event['Records'])
    assert result[0] == expected


@pytest.mark.describe("get_the_file_name")
@pytest.mark.it("Test returns correct file name")
def test_get_file_name_return_correct_file_name():
    event = {
        "Records": [
            {
                "s3": {
                    "bucket": {
                        "name": "test-bucket"
                    },
                    "object": {
                        "key": "test.csv"
                    }
                }
            }
        ],
    }
    expected = 'test.csv'
    result = get_file_and_ingestion_bucket_name(event['Records'])
    assert result[1] == expected
