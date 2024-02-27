from src.transform_handler2.make_dim_date import make_dim_date
import pytest
import pandas as pd
import datetime


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
    columns_varchar = ['day_name', 'month_name','date_id']
    result = make_dim_date(start='2022-11-01', end='2032-12-31')
    types = result.dtypes
    for col in columns_int:
        assert types[col] == 'int32'
    for col in columns_varchar:
        assert types[col] == 'object'



@pytest.mark.describe("make_dim_date")
@pytest.mark.it("Test returns correct contents")
def test_returns_correct_contents():

    result = make_dim_date(start='2024-02-27', end='2024-02-27')
    expected = {'date_id':[datetime.date(2024,2,27)],
                'year':[2024], 
                'month':[2],
                'day':[27],
                'day_of_week':[1],
                'day_name':['Tuesday'],
                'month_name':['February'],
                'quarter':[1]}
    
    expected_df=pd.DataFrame(data=expected)
    assert result['date_id'].equals(expected_df['date_id'])
   