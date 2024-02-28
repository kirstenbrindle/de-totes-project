def make_dim_currency(input_df):
    """
    This function takes a dataframe of currency \n
    as input and returns dataframe filtered by \n
    columns: 'currency_id', 'currency_code', 'currency_name'.

    Args:
    `input_df`: currency dataframe
    ---------------------------

    Returns:
    Formatted filtered dataframe.

    Errors:
    Raises no errors.
    """
    df = input_df.copy()
    df['currency_name'] = [
        'British pound sterling',
        'United States dollar',
        'Euro']
    last_updated = df['last_updated']
    last_updated_date = [n.split(' ')[0] for n in last_updated]
    last_updated_at_time = [t.split(' ')[1]for t in last_updated]
    df['last_updated_date'] = last_updated_date
    df['last_updated_time'] = last_updated_at_time
    df['currency_record_id'] = df['currency_id']
    dim_currency_df = df[['currency_record_id','currency_id', 'currency_code', 'currency_name', 'last_updated_date', 'last_updated_time']]
    return dim_currency_df
