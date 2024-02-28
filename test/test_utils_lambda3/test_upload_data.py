from src.load_handler3.upload_data import upload_data
from unittest.mock import Mock
import pytest
import pandas as pd


@pytest.mark.describe("upload_data")
@pytest.mark.it("test uses correct SQL query")
def test_uploads_data_sql_query():
    """
    Given:
    A dataframe, table and connection.

    Returns:
    Assertion of being called with correct query.
    """
    mock_conn = Mock()
    data = {
        'currency_id': [1, 2],
        'currency_code': ['GBP', 'USD'],
        'currency_name': ['British pound sterling',
                          'United States dollar']
    }
    row_labels = [0, 1]
    test_df = pd.DataFrame(data=data, index=row_labels)
    upload_data(mock_conn, 'test_currency', test_df)
    mock_conn.run.assert_called_with(
        "INSERT INTO test_currency "
        "(currency_id, currency_code, currency_name) "
        "VALUES (1, 'GBP', 'British pound sterling'), "
        "(2, 'USD', 'United States dollar');")
