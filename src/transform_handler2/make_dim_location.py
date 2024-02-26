import logging

logger = logging.getLogger('lambda2Logger')
logger.setLevel(logging.INFO)

def make_dim_location(df):
    try:
        df.rename(columns={"address_id": "location_id"}, inplace=True)
        dim_location_df = df[['location_id', 'address_line_1',
                            'address_line_2', 'district', 'city',
                            'postal_code', 'country', 'phone']]
        return dim_location_df
    except Exception as e:
        logger.info(e)
        logger.info(f'{df.columns}')
    
