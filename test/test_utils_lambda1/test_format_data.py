from src.extract_handler1.format_data import format_data
import pytest


@pytest.mark.describe("format_data")
@pytest.mark.it("Test format_data returns formatted "
                "query data for single row")
def test_format_data_returns_formatted_single_row():
    """
    Given:
    A single row from payment_type table once L1_extract_data is invoked

    Returns:
    List of dictionaries with column names(keys)
    """
    data = [[1, "SALES_RECEIPT", "2022-11-03 14:20:49.962",
            "2022-11-03 14:20:49.962"]]
    columns = ['payment_type_id', 'payment_type_name',
               'created_at', 'last_updated']
    result = format_data(data, columns)
    assert result == {
        'payment_type_id': [1],
        'payment_type_name': ['SALES_RECEIPT'],
        'created_at': ["2022-11-03 14:20:49.962"],
        'last_updated': ["2022-11-03 14:20:49.962"]
    }


@pytest.mark.describe("format_data")
@pytest.mark.it("Test format_data returns formatted "
                "query data for multiple rows")
def test_format_data_returns_formatted_multiple_rows():
    """
    Given:
    Multiple rows from payment_type table once L1_extract_data is invoked

    Returns:
    List of dictionaries with column names(keys)
    """
    columns = ['payment_type_id', 'payment_type_name',
               'created_at', 'last_updated']
    data = [[1, "SALES_RECEIPT", "2022-11-03 14:20:49.962",
            "2022-11-03 14:20:49.962"],
            [2, "SALES_REFUND", "2022-11-03 14:20:49.962",
            "2022-11-03 14:20:49.962"]]
    result = format_data(data, columns)

    assert result == {
        'payment_type_id': [1, 2],
        'payment_type_name': ['SALES_RECEIPT', 'SALES_REFUND'],
        'created_at': ["2022-11-03 14:20:49.962", '2022-11-03 14:20:49.962'],
        'last_updated': ["2022-11-03 14:20:49.962", '2022-11-03 14:20:49.962']
    }
