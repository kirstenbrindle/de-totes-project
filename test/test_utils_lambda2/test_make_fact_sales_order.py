from src.transform_handler2.make_fact_sales_order import make_fact_sales_order
import pytest
import pandas as pd
from datetime import datetime, date, time


@pytest.mark.describe("make_fact_sales_order")
@pytest.mark.it("Test returns a dataframe")
def test_returns_a_dataframe():
    data_sales_order = {
        'sales_order_id': ['1', '2', '3'],
        'created_at': [datetime.now(), datetime.now(), datetime.now()],
        'last_updated': [datetime.now(), datetime.now(), datetime.now()],
        'design_id': ['d1', 'd2', 'd3'],
        'staff_id': ['s4', 's5', 's6'],
        'counterparty_id': ['c1', 'c2', 'c3'],
        'units_sold': ['10', '20', '30'],
        'unit_price': [1.23, 1.25, 1.26],
        'currency_id': ['c1', 'c2', 'c3'],
        'agreed_delivery_date': ['2023-12-06', '2023-12-06', '2023-12-06'],
        'agreed_payment_date': ['2023-12-06', '2023-12-06', '2023-12-06'],
        'agreed_delivery_location_id': ['l1', 'l2', 'l3']
    }
    df = pd.DataFrame(data=data_sales_order)
    result = make_fact_sales_order(df)
    assert isinstance(result, pd.core.frame.DataFrame)


@pytest.mark.describe("make_fact_sales_order")
@pytest.mark.it("Test returns a formatted dataframe")
def test_returns_a_formatted_dataframe():
    data_sales_order = {
        'sales_order_id': ['1', '2', '3'],
        'created_at': [datetime(2023, 12, 22, 11, 0, 0),
                       datetime(2022, 11, 22, 11, 0, 0),
                       datetime(2021, 10, 22, 11, 0, 0)],
        'last_updated': [datetime(2023, 12, 22, 11, 0, 0),
                         datetime(2022, 11, 22, 11, 0, 0),
                         datetime(2021, 10, 22, 11, 0, 0)],
        'design_id': ['d1', 'd2', 'd3'],
        'staff_id': ['s4', 's5', 's6'],
        'counterparty_id': ['c1', 'c2', 'c3'],
        'units_sold': ['10', '20', '30'],
        'unit_price': [1.23, 1.25, 1.26],
        'currency_id': ['c1', 'c2', 'c3'],
        'agreed_delivery_date': ['2023-12-06', '2023-12-06', '2023-12-06'],
        'agreed_payment_date': ['2023-12-06', '2023-12-06', '2023-12-06'],
        'agreed_delivery_location_id': ['l1', 'l2', 'l3']
    }
    df = pd.DataFrame(data=data_sales_order)
    expected = {
        'sales_record_id': [1, 2, 3],
        'sales_order_id': ['1', '2', '3'],
        'created_date': [date(2023, 12, 22),
                         date(2022, 11, 22),
                         date(2021, 10, 22)],
        'created_time': [time(11, 0, 0),
                         time(11, 0, 0),
                         time(11, 0, 0)],
        'last_updated_date': [date(2023, 12, 22),
                              date(2022, 11, 22),
                              date(2021, 10, 22)],
        'last_updated_time': [time(11, 0, 0),
                              time(11, 0, 0),
                              time(11, 0, 0)],
        'design_id': ['d1', 'd2', 'd3'],
        'sales_staff_id': ['s4', 's5', 's6'],
        'counterparty_id': ['c1', 'c2', 'c3'],
        'units_sold': ['10', '20', '30'],
        'unit_price': [1.23, 1.25, 1.26],
        'currency_id': ['c1', 'c2', 'c3'],
        'agreed_delivery_date': ['2023-12-06', '2023-12-06', '2023-12-06'],
        'agreed_payment_date': ['2023-12-06', '2023-12-06', '2023-12-06'],
        'agreed_delivery_location_id': ['l1', 'l2', 'l3']
    }
    expected_df = pd.DataFrame(data=expected)
    result = make_fact_sales_order(df)
    assert result.equals(expected_df)
