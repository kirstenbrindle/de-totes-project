from src.utils.flexible_formater import format_data, L1_extract_data
import pytest
from unittest.mock import Mock, patch
from pg8000.native import Connection
import datetime
#hello
@pytest.fixture(scope="function")
def db_conn():
    """Connection to test_database"""
    user = 'minnie'
    password = 'password'
    host = 'localhost'
    database = 'test_database'
    return Connection(user=user, password=password,
                      host=host, database=database)

@pytest.mark.describe("format_data")
@pytest.mark.it("Test format_data returns formatted "
                "query data for single row")
def test_format_data_returns_formatted_single_row():
    """
    Given:
    a single row from payment_type table once L1_extract_data is invoked

    Returns:
    List of dictionaries with column names(keys)
    """
    data = [[1, "SALES_RECEIPT", "2022-11-03 14:20:49.962",
            "2022-11-03 14:20:49.962"]]
    columns=['payment_type_id','payment_type_name','created_at','last_updated']
    result = format_data(data,columns)
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
    rows from payment_type table once L1_extract_data is invoked

    Returns:
    List of dictionaries with column names(keys)
    """
    columns=['payment_type_id','payment_type_name','created_at','last_updated']
    data = [[1, "SALES_RECEIPT", "2022-11-03 14:20:49.962",
            "2022-11-03 14:20:49.962"],
            [2, "SALES_REFUND", "2022-11-03 14:20:49.962",
            "2022-11-03 14:20:49.962"]]
    result = format_data(data,columns)
    
    assert result == {
        'payment_type_id': [1, 2],
        'payment_type_name': ['SALES_RECEIPT', 'SALES_REFUND'],
        'created_at': ["2022-11-03 14:20:49.962", '2022-11-03 14:20:49.962'],
        'last_updated': ["2022-11-03 14:20:49.962", '2022-11-03 14:20:49.962']
    }


@pytest.mark.describe("L1_extract_data")
@pytest.mark.it("Test L1_extract_data runs a Select "
                "query from the given table")
def test_L1_extract_data_return_mock(db_conn):
    """
    checks returns value with a mock
    """
    expected={
        'payment_type_id': [1, 2,3,4],
        'payment_type_name': ['SALES_RECEIPT', 'SALES_REFUND','PURCHASE_PAYMENT','PURCHASE_REFUND'],
        'created_at': [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000),datetime.datetime(2022, 11, 3, 14, 20, 49, 962000),datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)],
        'last_updated': [datetime.datetime(2022, 11, 3, 14, 20, 49, 962000), datetime.datetime(2022, 11, 3, 14, 20, 49, 962000),datetime.datetime(2022, 11, 3, 14, 20, 49, 962000),datetime.datetime(2022, 11, 3, 14, 20, 49, 962000)]
    }
    
    result=L1_extract_data(db_conn, "payment_type")
    assert result == expected
    

