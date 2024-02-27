import logging

logger = logging.getLogger('lambda1Logger')
logger.setLevel(logging.INFO)


def make_fact_sales_order(input_df):
    try:
        df = input_df.copy()
        created_at = df['created_at']
        created_date = [n.split(' ')[0] for n in created_at] #'2024-12-25'
        created_at_time = [t.split(' ')[1] for t in created_at]
        last_updated = df['last_updated']
        last_updated_date = [n.split(' ')[0] for n in last_updated]
        last_updated_at_time = [t.split(' ')[1]for t in last_updated]
        df['sales_record_id'] = range(1, len(created_at) + 1)
        df.rename(columns={'staff_id': 'sales_staff_id'}, inplace=True)
        df['created_date'] = created_date
        df['created_time'] = created_at_time
        df['last_updated_date'] = last_updated_date
        df['last_updated_time'] = last_updated_at_time
        df.drop(columns=['created_at', 'last_updated'], inplace=True)
        filtered_formatted_df = df[['sales_record_id', 'sales_order_id',
                                    'created_date',
                                    'created_time', 'last_updated_date',
                                    'last_updated_time', 'design_id',
                                    'sales_staff_id', 'counterparty_id',
                                    'units_sold',
                                    'unit_price', 'currency_id',
                                    'agreed_delivery_date',
                                    'agreed_payment_date',
                                    'agreed_delivery_location_id']]
        return filtered_formatted_df
    except Exception as e:
        logger.info("something has gone wrong in the make_fact_sales_order.py")
        logger.warning(e)