from src.transform_handler2.make_dim_staff import make_dim_staff
import pytest
import pandas as pd


@pytest.mark.describe("make_dim_staff")
@pytest.mark.it("Test returns a dataframe")
def test_returns_a_dataframe():
    data_staff = {
        'staff_id': ['1', '2', '3'],
        'first_name': ['a', 'b', 'c'],
        'last_name': ['a', 'b', 'c'],
        'department_id': ['a', 'b', 'c'],
        'email_address': ['a', 'b', 'c'],
        'created_at': ['a', 'b', 'c'],
        'last_updated': ['a', 'b', 'c']
    }
    df = pd.DataFrame(data=data_staff)
    data_department = {
        'department_id': ['1', '2', '3'],
        'department_name': ['a', 'b', 'c'],
        'location': ['a', 'b', 'c'],
        'manager': ['a', 'b', 'c'],
        'created_at': ['a', 'b', 'c'],
        'last_updated': ['a', 'b', 'c']
    }
    df_2 = pd.DataFrame(data=data_department)
    data_dim_staff = {
        'staff_id': ['1', '2', '3'],
        'first_name': ['a', 'b', 'c'],
        'last_name': ['a', 'b', 'c'],
        'department_name': ['a', 'b', 'c'],
        'location': ['a', 'b', 'c'],
        'email_address': ['a', 'b', 'c']
    }
    pd.DataFrame(data=data_dim_staff)
    result = make_dim_staff(df, df_2)
    assert isinstance(result, pd.core.frame.DataFrame)


@pytest.mark.describe("make_dim_staff")
@pytest.mark.it("Test returns a filtered and merged dataframe")
def test_returns_a_filtered_and_merged_dataframe():
    data_staff = {
        'staff_id': ['1', '2', '3'],
        'first_name': ['Tom', 'Kirsten', 'Cinthya'],
        'last_name': ['Roberts', 'Robertson', 'Jones'],
        'department_id': ['d1', 'd2', 'd3'],
        'email_address': ['a', 'b', 'c'],
        'created_at': ['3', '6', '9'],
        'last_updated': ['10', '11', '12']
    }
    df = pd.DataFrame(data=data_staff)
    data_department = {
        'department_id': ['d1', 'd2', 'd3'],
        'department_name': ['health', 'food', 'tech'],
        'location': ['Manchester', 'Chester', 'Liverpool'],
        'manager': ['Manager', 'Manager1', 'Manager2'],
        'created_at': ['3', '6', '9'],
        'last_updated': ['10', '11', '12']
    }
    df_2 = pd.DataFrame(data=data_department)
    data_dim_staff = {
        'staff_id': ['1', '2', '3'],
        'first_name': ['Tom', 'Kirsten', 'Cinthya'],
        'last_name': ['Roberts', 'Robertson', 'Jones'],
        'department_name': ['health', 'food', 'tech'],
        'location': ['Manchester', 'Chester', 'Liverpool'],
        'email_address': ['a', 'b', 'c']
    }
    df_dim_staff = pd.DataFrame(data=data_dim_staff)

    result = make_dim_staff(df, df_2)
    assert result.equals(df_dim_staff)


# Row labels on tests need to be zero indexed to mimic SQL.

@pytest.mark.describe("make_dim_staff")
@pytest.mark.it("""Test returns a filtered and merged dataframe
                when table order is irregular""")
def test_returns_a_filtered_and_merged_df_when_order_is_irregular():
    data_staff = {
        'staff_id': ['1', '2', '3'],
        'first_name': ['Tom', 'Kirsten', 'Cinthya'],
        'last_name': ['Roberts', 'Robertson', 'Jones'],
        'department_id': ['3', '2', '1'],
        'email_address': ['a', 'b', 'c'],
        'created_at': ['3', '6', '9'],
        'last_updated': ['10', '11', '12']
    }

    df = pd.DataFrame(data=data_staff)
    data_department = {
        'department_id': ['1', '2', '3'],
        'department_name': ['z', 'f', 'g'],
        'location': ['Manchester', 'Chester', 'Liverpool'],
        'manager': ['Manager', 'Manager1', 'Manager2'],
        'created_at': ['3', '6', '9'],
        'last_updated': ['10', '11', '12']
    }
    df_2 = pd.DataFrame(data=data_department)
    data_dim_staff = {
        'staff_id': ['1', '2', '3'],
        'first_name': ['Tom', 'Kirsten', 'Cinthya'],
        'last_name': ['Roberts', 'Robertson', 'Jones'],
        'department_name': ['g', 'f', 'z'],
        'location': ['Liverpool', 'Chester', 'Manchester'],
        'email_address': ['a', 'b', 'c']
    }

    df_dim_staff = pd.DataFrame(data=data_dim_staff)

    result = make_dim_staff(df, df_2)
    assert result.equals(df_dim_staff)
