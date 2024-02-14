from src.utils.L1_extract_data import format_payment_type, L1_extract_data
import pytest
from unittest.mock import Mock, patch


@pytest.mark.describe("format_payment_type")
@pytest.mark.it("Test format_payment_type returns formatted "
                "query data for single row")
def test_format_payment_type_returns_formatted_single_row():
    """
    Given:
    a single row from payment_type table once L1_extract_data is invoked

    Returns:
    List of dictionaries with column names(keys)
    """
    data = ([1, "SALES_RECEIPT", "2022-11-03 14:20:49.962",
            "2022-11-03 14:20:49.962"])
    result = format_payment_type(data)
    assert result == {
        'payment_type_id': [1],
        'payment_type_name': ['SALES_RECEIPT'],
        'created_at': ["2022-11-03 14:20:49.962"],
        'last_updated': ["2022-11-03 14:20:49.962"]
    }


@pytest.mark.describe("format_payment_type")
@pytest.mark.it("Test format_payment_type returns formatted "
                "query data for multiple rows")
def test_format_payment_type_returns_formatted_multiple_rows():
    """
    Given:
    rows from payment_type table once L1_extract_data is invoked

    Returns:
    List of dictionaries with column names(keys)
    """
    data = ([1, "SALES_RECEIPT", "2022-11-03 14:20:49.962",
            "2022-11-03 14:20:49.962"],
            [2, "SALES_REFUND", "2022-11-03 14:20:49.962",
            "2022-11-03 14:20:49.962"])
    result = format_payment_type(data)
    assert result == {
        'payment_type_id': [1, 2],
        'payment_type_name': ['SALES_RECEIPT', 'SALES_REFUND'],
        'created_at': ["2022-11-03 14:20:49.962", '2022-11-03 14:20:49.962'],
        'last_updated': ["2022-11-03 14:20:49.962", '2022-11-03 14:20:49.962']
    }


@pytest.mark.describe("L1_extract_data")
@pytest.mark.it("Test L1_extract_data runs a Select "
                "query from the given table")
def test_L1_extract_data_return_mock():
    """
    checks returns value with a mock
    """
    my_mock = Mock()
    my_mock.run.return_value = ([
        1, "SALES_RECEIPT",
        "2022-11-03 14:20:49.962",
        "2022-11-03 14:20:49.962"
        ])
    L1_extract_data(my_mock, "payment_type")
    my_mock.run.assert_called_with("SELECT * FROM payment_type;")


@pytest.mark.describe("L1_extract_data")
@pytest.mark.it("Test L1_extract_data invokes format_payment_type")
@patch("src.utils.L1_extract_data.format_payment_type")
def test_L1_extract_data_invokes_format_payment_type(mock_payment_type):
    """
    Check that L1_extract_data invokes format_payment_type\n
    when table name is payment_type.

    """
    my_mock = Mock()
    my_mock.run.return_value = ([
        1, "SALES_RECEIPT",
        "2022-11-03 14:20:49.962",
        "2022-11-03 14:20:49.962"
        ])
    assert mock_payment_type.call_count == 0
    L1_extract_data(my_mock, "payment_type")
    assert mock_payment_type.call_count == 1
