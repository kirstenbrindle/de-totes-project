import pytest
import unittest
from src.write_csv import write_csv


@pytest.mark.describe('writes csv file')
@pytest.mark.it('writes a csv file when passed a tableName')
def test_writes_csv_file():
    
    data = {
    'payment_type_id': [1],
    'payment_type_name': ['SALES_RECEIPT'],
    'created_at': ["2022-11-03 14:20:49.962"],
    'last_updated': ["2022-11-03 14:20:49.962"]
    }
    result = write_csv(tableName="test")
    assert result == "test"
   

