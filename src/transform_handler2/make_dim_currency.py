def make_dim_currency(df):
    df['currency_name'] = [
        'British pound sterling',
        'United States dollar',
        'Euro']
    dim_currency_df = df[['currency_id', 'currency_code', 'currency_name']]
    return dim_currency_df
