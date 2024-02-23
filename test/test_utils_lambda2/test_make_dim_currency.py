from src.transform_handler2.make_dim_currency import make_dim_currency
import pytest
import pandas as pd


@pytest.mark.describe("make_dim_currency")
@pytest.mark.it("Test returns a dataframe")
def test_returns_a_dataframe():
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
    assert result.equals(df)


@pytest.mark.describe("make_dim_currency")
@pytest.mark.it("Test adds currency_name column")
def test_returns_df_with_currency_name():
    data = {
        'currency_id': [1, 2, 3],
        'currency_code': ['ABC', 'DEF', 'GHI'],
    }
    row_labels = [1, 2, 3]
    df = pd.DataFrame(data=data, index=row_labels)
    expected = {
        'currency_id': [1, 2, 3],
        'currency_code': ['ABC', 'DEF', 'GHI'],
        'currency_name': ['British pound sterling',
                          'United States dollar',
                          'Euro'],
    }
    row_labels = [1, 2, 3]
    expected_df = pd.DataFrame(data=expected, index=row_labels)
    result = make_dim_currency(df)
    assert result.equals(expected_df)


@pytest.mark.describe("make_dim_currency")
@pytest.mark.it("Test filters correct column")
def test_returns_correct_filtered_columns():
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
    expected = {
        'currency_id': [1, 2, 3],
        'currency_code': ['ABC', 'DEF', 'GHI'],
        'currency_name': ['British pound sterling',
                          'United States dollar',
                          'Euro'],
    }
    row_labels = [1, 2, 3]
    expected_df = pd.DataFrame(data=expected, index=row_labels)
    result = make_dim_currency(df)
    assert result.equals(expected_df)
