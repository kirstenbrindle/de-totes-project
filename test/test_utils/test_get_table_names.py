from src.utils.get_table_names import get_table_names
from pg8000.native import Connection, DatabaseError
import pytest
from unittest.mock import MagicMock, Mock

@pytest.fixture(scope="function")
def db_conn():
    """Connection to test_database"""
    user = 'minnie'
    password = 'password'
    host = 'localhost'
    database = 'test_database'
    return Connection(user=user, password=password,
                      host=host, database=database)


@pytest.fixture(scope="function")
def db_conn_error():
    """Connection to test_database"""
    user = 'helloooo'
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
    expected = ['addresses', 'counterparty', 'currency', 'department',
                'design', 'payment', 'payment_type', 'purchase_order',
                'sales_order', 'staff', 'transactions']
    assert result == expected


@pytest.mark.describe("get_table_names")
@pytest.mark.it("Test returns error")
def test_get_table_names_error():
    """
    Given:
    A database error

    Returns:
    Raises 
    """

    # query = conn.run("SELECT table_name "
    #                     "FROM information_schema.tables "
    #                     "WHERE table_schema='public' "
    #                     "AND table_type='BASE TABLE';")
    
    my_mock = MagicMock()
    my_mock.run.side_effect = DatabaseError("Issue with Connection")
    my_mock.run()
    with pytest.raises(ValueError):
        get_table_names(my_mock)
    
    # try:
    #     get_table_names(db_conn_error)
    # except Exception:
    #     print(Exception, "<<<<<<----- exception")
    #     assert False
