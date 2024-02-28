from src.transform_handler2.make_dim_counterparty import make_dim_counterparty
import pytest
import pandas as pd


@pytest.mark.describe("make_dim_counterparty")
@pytest.mark.it("Test returns a dataframe")
def test_returns_a_dataframe():
    """
    Given:
    An address dataframe and counterparty dataframe

    Returns:
    A dataframe
    """
    data_cp = {
        'counterparty_id': ['1', '2', '3'],
        'counterparty_legal_name': ['cp1', 'cp2', 'cp3'],
        'legal_address_id': ['2', '1', '3'],
        'commercial_contract': ['a', 'b', 'c'],
        'delivery_contract': ['d', 'e', 'f'],
        'created_at': ['a', 'b', 'c'],
        'last_updated': ['2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962']
    }
    df1 = pd.DataFrame(data=data_cp)

    data_address = {
        'address_id': ['1', '2', '3'],
        'address_line_1': ['abc', 'bcd', 'cde'],
        'address_line_2': ['c3', 'c4', 'c6'],
        'district': ['stockport', 'tameside', 'oldham'],
        'city': ['manchester', 'liverpool', 'chester'],
        'postal_code': ['cf1', 'sk14', 'np8'],
        'country': ['u.k', 'spain', 'italy'],
        'phone': ['014', '919', '587'],
        'created_at': ['a', 'b', 'c'],
        'last_updated': ['2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962']
    }
    df2 = pd.DataFrame(data=data_address)

    result = make_dim_counterparty(df1, df2)
    assert isinstance(result, pd.core.frame.DataFrame)


@pytest.mark.describe("make_dim_counterparty")
@pytest.mark.it("Test returns correctly renamed column")
def test_returns_a_correctly_renamed_column():
    """
    Given:
    An address dataframe and counterparty dataframe

    Returns:
    A dataframe with correctly renamed
    counterparty_legal_district column
    """
    data_cp = {
        'counterparty_id': ['1', '2', '3'],
        'counterparty_legal_name': ['cp1', 'cp2', 'cp3'],
        'legal_address_id': ['2', '1', '3'],
        'commercial_contract': ['a', 'b', 'c'],
        'delivery_contract': ['d', 'e', 'f'],
        'created_at': ['a', 'b', 'c'],
        'last_updated': ['2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962']
    }
    df1 = pd.DataFrame(data=data_cp)

    data_address = {
        'legal_address_id': ['1', '2', '3'],
        'address_line_1': ['abc', 'bcd', 'cde'],
        'address_line_2': ['c3', 'c4', 'c6'],
        'district': ['stockport', 'tameside', 'oldham'],
        'city': ['manchester', 'liverpool', 'chester'],
        'postal_code': ['cf1', 'sk14', 'np8'],
        'country': ['u.k', 'spain', 'italy'],
        'phone': ['014', '919', '587'],
        'created_at': ['a', 'b', 'c'],
        'last_updated': ['2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962']
    }
    df2 = pd.DataFrame(data=data_address)

    result = make_dim_counterparty(df1, df2)
    assert result.__contains__('counterparty_legal_district')


@pytest.mark.describe("make_dim_counterparty")
@pytest.mark.it("Test returns a correctly merged and filtered dataframe")
def test_returns_a_correctly_merged_dataframe():
    """
    Given:
    An address dataframe and counterparty dataframe

    Returns:
    A correctly formatted dataframe
    """
    data_cp = {
        'counterparty_id': ['1', '2', '3'],
        'counterparty_legal_name': ['cp1', 'cp2', 'cp3'],
        'legal_address_id': ['2', '1', '3'],
        'commercial_contract': ['a', 'b', 'c'],
        'delivery_contract': ['d', 'e', 'f'],
        'created_at': ['a', 'b', 'c'],
        'last_updated': ['2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962']
    }
    df1 = pd.DataFrame(data=data_cp)

    data_address = {
        'legal_address_id': ['1', '2', '3'],
        'address_line_1': ['abc', 'bcd', 'cde'],
        'address_line_2': ['c3', 'c4', 'c6'],
        'district': ['stockport', 'tameside', 'oldham'],
        'city': ['manchester', 'liverpool', 'chester'],
        'postal_code': ['cf1', 'sk14', 'np8'],
        'country': ['u.k', 'spain', 'italy'],
        'phone': ['014', '919', '587'],
        'created_at': ['a', 'b', 'c'],
        'last_updated': ['2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962',
                         '2022-11-03 14:20:49.962']
    }
    df2 = pd.DataFrame(data=data_address)

    data_dim_counterparty = {
        'counterparty_record_id': ['1', '2', '3'],
        'counterparty_id': ['1', '2', '3'],
        'counterparty_legal_name': ['cp1', 'cp2', 'cp3'],
        'counterparty_legal_address_line_1': ['bcd', 'abc', 'cde'],
        'counterparty_legal_address_line_2': ['c4', 'c3', 'c6'],
        'counterparty_legal_district': ['tameside', 'stockport', 'oldham'],
        'counterparty_legal_city': ['liverpool', 'manchester', 'chester'],
        'counterparty_legal_postal_code': ['sk14', 'cf1', 'np8'],
        'counterparty_legal_country': ['spain', 'u.k', 'italy'],
        'counterparty_legal_phone_number': ['919', '014', '587'],
        'last_updated_date': ['2022-11-03',
                              '2022-11-03',
                              '2022-11-03'],
        'last_updated_time': ['14:20:49.962',
                              '14:20:49.962',
                              '14:20:49.962'],
    }
    df_dim_counterparty = pd.DataFrame(data=data_dim_counterparty)

    result = make_dim_counterparty(df1, df2)
    assert result.equals(df_dim_counterparty)
