def make_dim_currency(input_df):
    """
    This function takes a dataframe of currency
    as input and returns dataframe filtered by
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
    dim_currency_df = df[['currency_id', 'currency_code', 'currency_name']]
    return dim_currency_df
