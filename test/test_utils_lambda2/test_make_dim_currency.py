from src.transform_handler2.make_dim_currency import make_dim_currency
import pytest
import pandas as pd


@pytest.mark.describe("make_dim_currency")
@pytest.mark.it("Test returns a dataframe")
def test_returns_a_dataframe():
    """
    Given:
    A currency dataframe

    Returns:
    A dataframe
    """
    data = {
        'currency_id': [1, 2, 3],
        'currency_code': ['ABC', 'DEF', 'GHI'],
        'currency_name': ['British pound sterling',
                          'United States dollar',
                          'Euro'],
    }
    row_labels = [1, 2, 3]
    df = pd.DataFrame(data=data, index=row_labels)
    result = make_dim_currency(df)
    assert isinstance(result, pd.core.frame.DataFrame)


@pytest.mark.describe("make_dim_currency")
@pytest.mark.it("Test adds currency_name column")
def test_returns_df_with_currency_name():
    """
    Given:
    A currency dataframe

    Returns:
    A dataframe with added currency_name column
    """
    data = {
        'currency_id': [1, 2, 3],
        'currency_code': ['ABC', 'DEF', 'GHI'],
        'created_at': ['a', 'b', 'c'],
        'last_updated': ['2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962']
    }
    row_labels = [1, 2, 3]
    df = pd.DataFrame(data=data, index=row_labels)
    result = make_dim_currency(df)
    assert result.__contains__('currency_name')


@pytest.mark.describe("make_dim_currency")
@pytest.mark.it("Test filters correct columns")
def test_returns_correct_filtered_columns():
    """
    Given:
    A currency dataframe

    Returns:
    A correctly formatted dataframe
    """
    data = {
        'rubbish1': ['1', '2', '3'],
        'rubbish2': ['ABC', 'DEF', 'GHI'],
        'currency_id': [1, 2, 3],
        'currency_code': ['ABC', 'DEF', 'GHI'],
        'rubbish3': ['1', '2', '3'],
        'rubbish4': ['ABC', 'DEF', 'GHI'],
        'last_updated': ['2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962']
    }
    row_labels = [1, 2, 3]
    df = pd.DataFrame(data=data, index=row_labels)
    expected = {
        'currency_record_id': [1, 2, 3],
        'currency_id': [1, 2, 3],
        'currency_code': ['ABC', 'DEF', 'GHI'],
        'currency_name': ['British pound sterling',
                          'United States dollar',
                          'Euro'],
        'last_updated_date': ['2022-11-03',
                              '2022-11-03',
                              '2022-11-03'],
        'last_updated_time': ['14:20:49.962',
                              '14:20:49.962',
                              '14:20:49.962'],
    }
    row_labels = [1, 2, 3]
    expected_df = pd.DataFrame(data=expected, index=row_labels)
    result = make_dim_currency(df)
    assert result.equals(expected_df)


@pytest.mark.describe("make_dim_currency")
@pytest.mark.it("Test returns columns in dataframe have correct type")
def test_returns_correct_column_types():
    """
    Given:
    A currency dataframe

    Returns:
    A correctly formatted dataframe
    """
    data = {
        'rubbish1': ['1', '2', '3'],
        'rubbish2': ['ABC', 'DEF', 'GHI'],
        'currency_id': [1, 2, 3],
        'currency_code': ['ABC', 'DEF', 'GHI'],
        'rubbish3': ['1', '2', '3'],
        'rubbish4': ['ABC', 'DEF', 'GHI'],
    }
    row_labels = [1, 2, 3]
    df = pd.DataFrame(data=data, index=row_labels)
    columns_varchar = ['currency_code', 'currency_name']
    result = make_dim_currency(df)
    types = result.dtypes
    for col in columns_varchar:
        assert types[col] == 'object'
    assert types['currency_id'] == 'int64'
