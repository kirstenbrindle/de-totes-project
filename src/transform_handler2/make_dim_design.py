def make_dim_design(input_df):
    """
    This function takes a dataframes of design \n
    and returns filtered dataframe with columns \n
    `design_id`, `design_name`, `file_location`, \n
    `file_name`.

    Args:
    `input_df`: design dataframe
    ---------------------------

    Returns:
    Formatted dataframe.
    """
    df = input_df.copy()
    last_updated = df['last_updated']
    last_updated_date = [n.split(' ')[0] for n in last_updated]
    last_updated_at_time = [t.split(' ')[1]for t in last_updated]
    df['last_updated_date'] = last_updated_date
    df['last_updated_time'] = last_updated_at_time
    df['design_record_id'] = df['design_id']
    dim_design_df = df[['design_record_id','design_id', 'design_name',
                        'file_location', 'file_name', 'last_updated_date', 'last_updated_time']]
    return dim_design_df
