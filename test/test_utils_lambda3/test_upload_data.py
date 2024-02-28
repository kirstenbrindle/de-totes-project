from src.load_handler3.upload_data import upload_data
from unittest.mock import Mock, call
import pytest
import pandas as pd


@pytest.mark.describe("upload_data")
@pytest.mark.it("test uploads data with mock db_conn")
def test_uploads_data_into_test_db():
    """
    Given:
    an s3 connection, table name and dataframe

    Returns:
    Check correct run query is called to insert
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
    calls = [call("INSERT INTO test_currency "
                  "(currency_id, currency_code, currency_name) "
                  "VALUES (1, 'GBP', 'British pound sterling'), "
                  "(2, 'USD', 'United States dollar');"), call('COMMIT')]
    mock_conn.run.assert_has_calls(calls)
