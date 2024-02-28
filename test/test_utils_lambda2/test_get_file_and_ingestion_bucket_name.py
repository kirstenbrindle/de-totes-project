from src.transform_handler2.get_file_and_ingestion_bucket_name import (
    get_file_and_ingestion_bucket_name)
import pytest


@pytest.mark.describe("get_file_and_ingestion_bucket_name")
@pytest.mark.it("Test returns correct bucket name")
def test_get_file_bucket_returns_bucket_name():
    """
    Given:
    the Records key from an AWS lambda event

    Returns:
    Correct bucket name associated with the event
    """
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


@pytest.mark.describe("get_file_and_ingestion_bucket_name")
@pytest.mark.it("Test returns correct file name")
def test_get_file_bucket_returns_correct_file_name():
    """
    Given:
    the Records key from an AWS lambda event

    Returns:
    Correct file name that triggered the event
    """
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
