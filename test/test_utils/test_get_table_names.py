from src.utils.get_table_names import get_table_names
from pg8000.native import Connection
import pytest


@pytest.fixture(scope="function")
def db_conn():
    """Connection to test_database"""
    user = 'kirsten-brindle'
    password = 'password'
    host = 'localhost'
    database = 'test_database'
    return Connection(user=user, password=password,
                      host=host, database=database)


@pytest.mark.describe("get_table_names")
@pytest.mark.it("Test returns correct table names")
def test_correct_table_names_are_returned(db_conn):
    """
    Given:
    a database connection

    Returns:
    list of table names in that database.
    """

    result = get_table_names(db_conn)
    expected = ['addresses', 'counterparty', 'currency', 'department', 'design',
                'payment', 'payment_type', 'purchase_order', 'sales_order', 'staff', 'transactions']
    assert result == expected
