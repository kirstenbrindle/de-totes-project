def make_dim_design(input_df):
    """
    This function takes a dataframes of design
    and returns filtered dataframe with columns
    `design_id`, `design_name`, `file_location`, `file_name`.

    Args:
        `input_df`: design dataframe
    ---------------------------

    Returns:
        Formatted dataframe.
    """
    df = input_df.copy()
    dim_design_df = df[['design_id', 'design_name',
                        'file_location', 'file_name']]
    return dim_design_df
