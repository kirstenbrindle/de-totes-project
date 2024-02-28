from src.transform_handler2.make_dim_location import make_dim_location
import pytest
import pandas as pd


@pytest.mark.describe("make_dim_location")
@pytest.mark.it("Test returns a dataframe")
def test_returns_a_dataframe():
    """
    Given:
    An address dataframe

    Returns:
    A dataframe
    """
    data = {
        'address_id': [1, 2, 3],
        'address_line_1': ['a', 'b', 'c'],
        'address_line_2': ['a', 'b', 'c'],
        'district': ['a', 'b', 'c'],
        'city': ['a', 'b', 'c'],
        'postal_code': ['a', 'b', 'c'],
        'country': ['a', 'b', 'c'],
        'phone': ['a', 'b', 'c'],
        'last_updated': ['2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962']
    }
    row_labels = [1, 2, 3]
    df = pd.DataFrame(data=data, index=row_labels)
    result = make_dim_location(df)
    assert isinstance(result, pd.core.frame.DataFrame)


@pytest.mark.describe("make_dim_location")
@pytest.mark.it("Test filters the correct columns")
def test_returns_the_correct_columns_only():
    """
    Given:
    An address dataframe

    Returns:
    A dataframe with the correct columns
    """
    data = {
        'column1': ['a', 'b', 'c'],
        'address_id': ['1', '2', '3'],
        'address_line_1': ['a', 'b', 'c'],
        'address_line_2': ['a', 'b', 'c'],
        'district': ['a', 'b', 'c'],
        'city': ['a', 'b', 'c'],
        'postal_code': ['a', 'b', 'c'],
        'country': ['a', 'b', 'c'],
        'phone': ['a', 'b', 'c'],
        'last_updated': ['2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962']
    }
    row_labels = [1, 2, 3]
    df = pd.DataFrame(data=data, index=row_labels)
    expected_df = {
        'address_id': ['1', '2', '3'],
        'address_line_1': ['a', 'b', 'c'],
        'address_line_2': ['a', 'b', 'c'],
        'district': ['a', 'b', 'c'],
        'city': ['a', 'b', 'c'],
        'postal_code': ['a', 'b', 'c'],
        'country': ['a', 'b', 'c'],
        'phone': ['a', 'b', 'c'],
        'last_updated_date': ['2022-11-03', '2022-11-03', '2022-11-03'],
        'last_updated_time': ['14:20:49.962', '14:20:49.962', '14:20:49.962']
    }
    row_labels = [1, 2, 3]
    expected_df = pd.DataFrame(data=expected_df, index=row_labels)
    result = make_dim_location(df)
    assert result.equals(expected_df)
