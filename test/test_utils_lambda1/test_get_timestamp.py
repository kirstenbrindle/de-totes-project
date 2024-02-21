from src.utils_lambda1.get_timestamp import get_timestamp
import pytest


@pytest.mark.describe("get_timestamp")
@pytest.mark.it("Test returns a string")
def test_returns_a_string():
    input = "currency-2022-11-03 14:20:49.962.csv"
    actual = get_timestamp(input)
    assert isinstance(actual, str)


@pytest.mark.describe("get_timestamp")
@pytest.mark.it("Test returns the correct timestamp")
def test_returns_correct_timestamp():
    input = "currency-2022-11-03 14:20:49.962.csv"
    expected = "2022-11-03 14:20:49.962"
    actual = get_timestamp(input)
    assert actual == expected


@pytest.mark.describe("get_timestamp")
@pytest.mark.it("Test returns correct timestamp when underscore in file name")
def test_returns_correct_timestamp_underscore_in_file_name():
    input = "sales_order-2022-11-03 14:20:49.962.csv"
    expected = "2022-11-03 14:20:49.962"
    actual = get_timestamp(input)
    assert actual == expected
