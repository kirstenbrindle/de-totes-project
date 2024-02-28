from src.load_handler3.get_table_name import get_table_name
import pytest


@pytest.mark.describe("get_table_name")
@pytest.mark.it("Test returns a string")
def test_returns_a_string():
    """
    Given:
    A test filename including key (table name).

    Returns:
    A string
    """
    input = "dim_currency/dim_currency-2022-11-03 14:20:49.962.parquet"
    actual = get_table_name(input)
    assert isinstance(actual, str)


@pytest.mark.describe("get_table_name")
@pytest.mark.it("Test returns the correct table_name")
def test_returns_correct_table_name():
    """
    Given:
    A test filename including key (table name).

    Returns:
    A string containing the name of table to which the file belongs.
    """
    input = "dim_currency/dim_currency-2022-11-03 14:20:49.962.parquet"
    expected = "dim_currency"
    actual = get_table_name(input)
    assert actual == expected


@pytest.mark.describe("get_table_name")
@pytest.mark.it("Test returns correct table_name with multiple underscores")
def test_returns_correct_table_name_with_multiple_underscores():
    """
    Given:
    A test filename including key (table name) \
    which includes multiple underscores.

    Returns:
    A string containing the name of table to which the file belongs.
    """
    input = "fact_sales_order/fact_sales_order-2022-11-03 14:20:49.962.parquet"
    expected = "fact_sales_order"
    actual = get_table_name(input)
    assert actual == expected
