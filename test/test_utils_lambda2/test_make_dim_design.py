from src.transform_handler2.make_dim_design import make_dim_design
import pytest
import pandas as pd


@pytest.mark.describe("make_dim_design")
@pytest.mark.it("Test returns a dataframe")
def test_returns_a_dataframe():
    """
    Given:
    A design dataframe

    Returns:
    A dataframe
    """
    data = {
        'col1': ['a', 'b', 'c'],
        'design_id': [1, 2, 3],
        'design_name': ['a', 'b', 'c'],
        'file_location': ['a', 'b', 'c'],
        'file_name': ['a', 'b', 'c'],
        'last_updated': ['2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962']
    }
    row_labels = [1, 2, 3]
    df = pd.DataFrame(data=data, index=row_labels)
    result = make_dim_design(df)
    assert isinstance(result, pd.core.frame.DataFrame)


@pytest.mark.describe("make_dim_design")
@pytest.mark.it("Test filters the correct columns")
def test_returns_the_correct_columns_only():
    """
    Given:
    A design dataframe

    Returns:
    A dataframe with the correct columns
    """
    data = {
        'col1': ['a', 'b', 'c'],
        'design_id': [1, 2, 3],
        'design_name': ['a', 'b', 'c'],
        'file_location': ['a', 'b', 'c'],
        'file_name': ['a', 'b', 'c'],
        'last_updated': ['2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962']
    }
    row_labels = [1, 2, 3]
    df = pd.DataFrame(data=data, index=row_labels)
    expected = {
        'design_record_id': [1, 2, 3],
        'design_id': [1, 2, 3],
        'design_name': ['a', 'b', 'c'],
        'file_location': ['a', 'b', 'c'],
        'file_name': ['a', 'b', 'c'],
        'last_updated_date': ['2022-11-03', '2022-11-03', '2022-11-03'],
        'last_updated_time': ['14:20:49.962', '14:20:49.962', '14:20:49.962']
    }
    row_labels = [1, 2, 3]
    expected_df = pd.DataFrame(data=expected, index=row_labels)
    result = make_dim_design(df)
    assert result.equals(expected_df)
