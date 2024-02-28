import logging

logger = logging.getLogger('lambda2Logger')
logger.setLevel(logging.INFO)


def make_dim_location(input_df):
    """
    This function takes a dataframe of address.
    Renames `address_id` column to `location_id`
    and returns filtered dataframe with columns
    `location_id`, `address_line_1`, `address_line_2`,
    `district`, `city`, `postal_code`, `country`, `phone`.

    Args:
        `input_df`: address dataframe
    ---------------------------

    Returns:
        Formatted dataframe.
    """
    try:
        df = input_df.copy()
        last_updated = df['last_updated']
        last_updated_date = [n.split(' ')[0] for n in last_updated]
        last_updated_at_time = [t.split(' ')[1]for t in last_updated]
        df['last_updated_date'] = last_updated_date
        df['last_updated_time'] = last_updated_at_time
        dim_location_df = df[['address_id','address_line_1',
                              'address_line_2', 'district', 'city',
                              'postal_code', 'country', 'phone', 'last_updated_date', 'last_updated_time' ]]
        return dim_location_df
    except Exception as e:
        logger.info(e)
        logger.info(f'{df.columns}')
