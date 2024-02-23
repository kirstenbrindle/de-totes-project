from src.transform_handler2.make_dim_date import make_dim_date
import pytest
import pandas as pd
from datetime import datetime as dt

@pytest.mark.describe("make_dim_date")
@pytest.mark.it("Test returns a dataframe")
def test_returns_a_dataframe():
    result = make_dim_date(start='2022-11-01', end='2032-12-31')
    assert isinstance(result, pd.core.frame.DataFrame)


@pytest.mark.describe("make_dim_date")
@pytest.mark.it("Test returns dataframe with correct columns")
def test_returns_correct_columns():
    columns = ['date_id', 'year', 'month', 'day',
               'day_of_week', 'day_name', 'month_name', 'quarter']
    result = make_dim_date(start='2022-11-01', end='2032-12-31')
    assert all(col in result.columns for col in columns)


@pytest.mark.describe("make_dim_date")
@pytest.mark.it("Test returns columns in dataframe have correct type")
def test_returns_correct_column_types():
    columns_int = ['year', 'month', 'day',
                   'day_of_week', 'quarter']
    columns_varchar = ['day_name', 'month_name']
    result = make_dim_date(start='2022-11-01', end='2032-12-31')
    types = result.dtypes
    for col in columns_int:
        assert types[col] == 'int32'
    for col in columns_varchar:
        assert types[col] == 'object'
    assert types['date_id'] == 'datetime64[ns]'
