def make_dim_design(df):
    dim_design_df = df[['design_id', 'design_name',
                        'file_location', 'file_name']]
    return dim_design_df
