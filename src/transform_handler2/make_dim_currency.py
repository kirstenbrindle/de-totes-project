def make_dim_currency(input_df):
    df = input_df.copy()
    df['currency_name'] = [
        'British pound sterling',
        'United States dollar',
        'Euro']
    dim_currency_df = df[['currency_id', 'currency_code', 'currency_name']]
    return dim_currency_df
