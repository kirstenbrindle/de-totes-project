from src.transform_handler2.make_dim_location import make_dim_location
import pytest
import pandas as pd


@pytest.mark.describe("make_dim_location")
@pytest.mark.it("Test returns a dataframe")
def test_returns_a_dataframe():
    data = {
        'location_id': ['1', '2', '3'],
        'address_line_1': ['a', 'b', 'c'],
        'address_line_2': ['a', 'b', 'c'],
        'district': ['a', 'b', 'c'],
        'city': ['a', 'b', 'c'],
        'postal_code': ['a', 'b', 'c'],
        'country': ['a', 'b', 'c'],
        'phone': ['a', 'b', 'c']
    }
    row_labels = [1, 2, 3]
    df = pd.DataFrame(data=data, index=row_labels)
    result = make_dim_location(df)
    assert result.equals(df)


# @pytest.mark.describe("make_dim_design")
# @pytest.mark.it("Test filters the correct columns")
# def test_returns_the_correct_columns_only():
#     data = {
#         'col1': ['a', 'b', 'c'],
#         'design_id': ['1', '2', '3'],
#         'design_name': ['a', 'b', 'c'],
#         'file_location': ['a', 'b', 'c'],
#         'file_name': ['a', 'b', 'c']
#     }
#     row_labels = [1, 2, 3]
#     df = pd.DataFrame(data=data, index=row_labels)
#     expected = {
#         'design_id': ['1', '2', '3'],
#         'design_name': ['a', 'b', 'c'],
#         'file_location': ['a', 'b', 'c'],
#         'file_name': ['a', 'b', 'c']
#     }
#     row_labels = [1, 2, 3]
#     expected_df = pd.DataFrame(data=expected, index=row_labels)
#     result = make_dim_design(df)
#     assert result.equals(expected_df)
