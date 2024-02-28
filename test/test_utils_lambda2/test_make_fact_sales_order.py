from src.transform_handler2.make_fact_sales_order import make_fact_sales_order
import pytest
import pandas as pd


@pytest.mark.describe("make_fact_sales_order")
@pytest.mark.it("Test returns a dataframe")
def test_returns_a_dataframe():
    """
    Given:
    A sales dataframe

    Returns:
    A dataframe
    """
    data_sales_order = {
        'sales_order_id': ['1', '2', '3'],
        'created_at': ["2022-11-03 14:20:49.962",
                       "2022-11-03 14:20:49.962",
                       "2022-11-03 14:20:49.962"],
        'last_updated': ["2022-11-03 14:20:49.962",
                         "2022-11-03 14:20:49.962",
                         "2022-11-03 14:20:49.962"],
        'design_id': ['d1', 'd2', 'd3'],
        'staff_id': ['s4', 's5', 's6'],
        'counterparty_id': ['c1', 'c2', 'c3'],
        'units_sold': ['10', '20', '30'],
        'unit_price': [1.23, 1.25, 1.26],
        'currency_id': ['c1', 'c2', 'c3'],
        'agreed_delivery_date': ['2023-12-06',
                                 '2023-12-06',
                                 '2023-12-06'],
        'agreed_payment_date': ['2023-12-06',
                                '2023-12-06',
                                '2023-12-06'],
        'agreed_delivery_location_id': ['l1', 'l2', 'l3']
    }
    df = pd.DataFrame(data=data_sales_order)
    result = make_fact_sales_order(df)
    assert isinstance(result, pd.core.frame.DataFrame)


@pytest.mark.describe("make_fact_sales_order")
@pytest.mark.it("Test returns a formatted dataframe")
def test_returns_a_formatted_dataframe():
    """
    Given:
    A sales dataframe

    Returns:
    A dataframe formatted with the correct columns
    """
    data_sales_order = {
        'sales_order_id': ['1', '2', '3'],
        'created_at': ["2022-11-03 14:20:49.962",
                       "2022-11-03 14:20:49.962",
                       "2022-11-03 14:20:49.962"],
        'last_updated': ["2022-11-03 14:20:49.962",
                         "2022-11-03 14:20:49.962",
                         "2022-11-03 14:20:49.962"],
        'design_id': ['d1', 'd2', 'd3'],
        'staff_id': ['s4', 's5', 's6'],
        'counterparty_id': ['c1', 'c2', 'c3'],
        'units_sold': ['10', '20', '30'],
        'unit_price': [1.23, 1.25, 1.26],
        'currency_id': ['c1', 'c2', 'c3'],
        'agreed_delivery_date': ['2023-12-06',
                                 '2023-12-06',
                                 '2023-12-06'],
        'agreed_payment_date': ['2023-12-06',
                                '2023-12-06',
                                '2023-12-06'],
        'agreed_delivery_location_id': ['l1', 'l2', 'l3']
    }
    df = pd.DataFrame(data=data_sales_order)
    expected = {
        'sales_order_id': ['1', '2', '3'],
        'created_date': ['2022-11-03',
                         '2022-11-03',
                         '2022-11-03'],
        'created_time': ['14:20:49.962',
                         '14:20:49.962',
                         '14:20:49.962'],
        'last_updated_date': ['2022-11-03',
                              '2022-11-03',
                              '2022-11-03'],
        'last_updated_time': ['14:20:49.962',
                              '14:20:49.962',
                              '14:20:49.962'],
        'design_record_id': ['d1', 'd2', 'd3'],
        'sales_staff_id': ['s4', 's5', 's6'],
        'counterparty_record_id': ['c1', 'c2', 'c3'],
        'units_sold': ['10', '20', '30'],
        'unit_price': [1.23, 1.25, 1.26],
        'currency_record_id': ['c1', 'c2', 'c3'],
        'agreed_delivery_date': ['2023-12-06', '2023-12-06', '2023-12-06'],
        'agreed_payment_date': ['2023-12-06', '2023-12-06', '2023-12-06'],
        'agreed_delivery_location_id': ['l1', 'l2', 'l3']
    }
    expected_df = pd.DataFrame(data=expected)
    result = make_fact_sales_order(df)
    assert result.equals(expected_df)
