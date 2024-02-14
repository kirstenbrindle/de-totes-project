import pytest
import unittest
from src.write_csv import write_csv


@pytest.mark.describe('writes csv file')
@pytest.mark.it('writes a csv file when passed a tableName')
def test_writes_csv_file():
    data = [
        [1, GBP, ]
    ]
    result = write_csv(tableName="test")
    assert result == "test"
