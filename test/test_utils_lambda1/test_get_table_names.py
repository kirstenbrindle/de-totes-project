from src.utils_lambda1.get_table_names import get_table_names
import pytest
from unittest.mock import MagicMock


@pytest.mark.describe("get_table_names")
@pytest.mark.it("Test returns correct table names")
def test_correct_table_names_are_returned():
    """
    Given:
    a database connection

    Returns:
    list of table names in that database.
    """
    mock_conn = MagicMock()
    mock_conn.run.return_value = [
        ['counterparty'], ['addresses'], ['currency']]
    result = get_table_names(mock_conn)
    expected = ['addresses', 'counterparty', 'currency']
    assert result == expected
