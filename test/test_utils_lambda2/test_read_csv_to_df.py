from src.transform_handler2.read_csv_to_df import read_csv_to_df
from unittest.mock import patch
import pytest
import pandas as pd
import logging

logger = logging.getLogger('test')
logger.setLevel(logging.INFO)
logger.propagate = True


@pytest.mark.describe("read_csv_to_df")
@pytest.mark.it("test pandas read method is invoked")
@patch("src.transform_handler2.read_csv_to_df.pd")
def test_reads_method_is_invoked(mock_pd):
    assert mock_pd.read_csv.call_count == 0
    read_csv_to_df("test1.csv")
    assert mock_pd.read_csv.call_count == 1


@pytest.mark.describe("read_csv_to_df")
@pytest.mark.it("test pandas returns dataframe with file contents")
def test_returns_dataframe():
    data = {
        'column1': ['r1c1', 'r2c1', 'r3c1'],
        'column2': ['r1c2', 'r2c2', 'r3c2'],
        'column3': ['r1c3', 'r2c3', 'r3c3'],
    }
    row_labels = [0, 1, 2]
    expected = pd.DataFrame(data=data, index=row_labels)
    result = read_csv_to_df("test/test_csv_files/test1.csv")
    assert result.equals(expected)


@pytest.mark.describe("read_csv_to_df")
@pytest.mark.it("test error output when given incorrect file path to read")
def test_logs_error_when_passed_incorrect_file_path(caplog):
    with caplog.at_level(logging.INFO):
        read_csv_to_df("test/test_csv_files/test4.csv")
        assert "Specified file cannot be found" in caplog.text


@pytest.mark.describe("read_csv_to_df")
@pytest.mark.it("test error output when given incorrect file type")
def test_logs_error_when_passed_incorrect_file_type(caplog):
    with caplog.at_level(logging.INFO):
        read_csv_to_df("requirements.txt")
        assert "File type incorrect, must be csv format" in caplog.text
