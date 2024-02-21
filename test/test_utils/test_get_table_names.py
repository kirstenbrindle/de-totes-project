from src.utils.get_table_names import get_table_names
from pg8000.native import Connection, DatabaseError
import pytest
from unittest.mock import MagicMock, Mock
import pg8000


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

    pg8000.exceptions.DatabaseError: {'S': 'FATAL',\
    'V': 'FATAL', 'C': '28P01', 'M': 'password authentication failed \
    for user "helloooo"', 'F': 'auth.c', 'L': '335', 'R': 'auth_failed'}
    Returns:
    Raises 
    """
    
    with pytest.raises(ValueError):
        my_mock = MagicMock()
        my_mock.run.side_effect = pg8000.exceptions.DatabaseError
        get_table_names(my_mock)
    


@pytest.mark.describe("get_table_names")
@pytest.mark.it("Test returns contents of Database error")
def test_get_table_names_database_error():
    """
    Given:
    A database error
    -> WRONG USERNAME
    pg8000.exceptions.DatabaseError: {'S': 'FATAL',\
    'V': 'FATAL', 'C': '28P01', 'M': 'password authentication failed \
    for user "helloooo"', 'F': 'auth.c', 'L': '335', 'R': 'auth_failed'}

    -> WRONG DB NAME
    pg8000.exceptions.DatabaseError: {'S': 'FATAL', 'V': 'FATAL', 'C': '3D000',\
    'M': 'database "test_database90000" does not exist', 'F': 'postinit.c', 'L':\
    '885', 'R': 'InitPostgres'}

    
    -> WRONG HOST ERROR
     pg8000.exceptions.InterfaceError: Can't create a connection to host localhost9000\
    and port 5432 (timeout is None and source_address is None).
    Returns:
    Raises 
    """
    try:
        """Connection to test_database"""
        user = 'minnie'
        password = 'password'
        host = 'localhost'
        database = 'test_database90000'
        conn = Connection(user=user, password=password,
                        host=host, database=database)
        get_table_names(conn)
    except Exception as e:
        print(e, "<<<<<<----- error!!!")
        assert False
    # with pytest.raises(ValueError):
    #     my_mock = MagicMock()
    #     my_mock.run.side_effect = pg8000.exceptions.DatabaseError
    #     get_table_names(my_mock)
    