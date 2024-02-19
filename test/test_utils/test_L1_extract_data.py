from src.utils.L1_extract_data import L1_extract_data
import pytest
from unittest.mock import Mock, patch
from datetime import datetime


@pytest.mark.describe("L1_extract_data")
@pytest.mark.it("Test L1_extract_data select * from table if boolean is True")
def test_L1_extract_data_runs_correct_query_if_boolean_true():
    mock_conn = Mock()
    L1_extract_data(mock_conn, "currency", True)
    mock_conn.run.assert_called_with("SELECT * FROM currency;")


@pytest.mark.describe("L1_extract_data")
@pytest.mark.it("Test L1_extract_data invokes get most recent file if boolean is false")
@patch("src.utils.L1_extract_data.get_most_recent_file")
def test_L1_extract_data_invokes_get_most_recent_file_if_boolean_is_false(mock_recent_file):
    mock_conn = Mock()
    assert mock_recent_file.call_count == 0
    L1_extract_data(mock_conn, "currency", False)
    assert mock_recent_file.call_count == 1
    mock_recent_file.assert_called_with("currency")


@pytest.mark.describe("L1_extract_data")
@pytest.mark.it("Test L1_extract_data invokes get_timestamp if boolean is false")
@patch("src.utils.L1_extract_data.get_timestamp")
@patch("src.utils.L1_extract_data.get_most_recent_file")
def test_L1_extract_data_invokes_get_timestamp_if_boolean_is_false(mock_get_most_recent_file, mock_timestamp):
    mock_conn = Mock()
    assert mock_timestamp.call_count == 0
    L1_extract_data(mock_conn, "currency", False)
    assert mock_timestamp.call_count == 1
    recent_file = mock_get_most_recent_file("currency")
    mock_timestamp.assert_called_with(recent_file)


@pytest.mark.describe("L1_extract_data")
@pytest.mark.it("Test L1_extract_data select * from table with where clause if boolean is False")
@patch("src.utils.L1_extract_data.get_timestamp")
@patch("src.utils.L1_extract_data.get_most_recent_file")
def test_L1_extract_data_runs_correct_query_if_boolean_is_false(mock_get_most_recent_file, mock_timestamp):
    mock_conn = Mock()
    mock_timestamp.return_value = "2022-11-03 14:20:49.962"
    L1_extract_data(mock_conn, "currency", False)
    mock_conn.run.assert_called_with(
        "SELECT * FROM currency WHERE last_updated > '2022-11-03 14:20:49.962';")

# Mock all functions - seems to be confused as we have partially mocked. 
    # test database too.
@pytest.mark.describe("L1_extract_data")
@pytest.mark.it("Test L1_extract_data invokes format data if boolean is false")
@patch("src.utils.L1_extract_data.format_data")
def test_L1_extract_data_invokes_format_data_if_boolean_is_false(mock_format_data):
    mock_conn = Mock()
    mock_conn.run.return_value = [[1, 'GBP', datetime(2022, 11, 3, 14, 20, 49, 962000), datetime(2022, 11, 3, 14, 20, 49, 962000)], [2, 'USD', datetime(
        2022, 11, 3, 14, 20, 49, 962000), datetime(2022, 11, 3, 14, 20, 49, 962000)], [3, 'EUR', datetime(2022, 11, 3, 14, 20, 49, 962000), datetime(2022, 11, 3, 14, 20, 49, 962000)]]
    assert mock_format_data.call_count == 0
    L1_extract_data(mock_conn, "currency", False)
    assert mock_format_data.call_count == 1
    mock_format_data.assert_called_with(mock_conn.run.return_value)


# @pytest.mark.describe("L1_extract_data")
# @pytest.mark.it("Test L1_extract_data invokes format_payment_type")
# @patch("src.utils.L1_extract_data.format_payment_type")
# def test_L1_extract_data_invokes_format_payment_type(mock_payment_type):
#     """
#     Check that L1_extract_data invokes format_payment_type\n
#     when table name is payment_type.

#     """
#     my_mock = Mock()
#     my_mock.run.return_value = ([
#         1, "SALES_RECEIPT",
#         "2022-11-03 14:20:49.962",
#         "2022-11-03 14:20:49.962"
#         ])
#     assert mock_payment_type.call_count == 0
#     L1_extract_data(my_mock, "payment_type")
#     assert mock_payment_type.call_count == 1
