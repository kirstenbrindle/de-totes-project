def make_dim_design(input_df):
    df = input_df.copy()
    dim_design_df = df[['design_id', 'design_name',
                        'file_location', 'file_name']]
    return dim_design_df
