import pandas as pd


def make_dim_staff(input_df, input_df2):
    """
    This function takes 2 dataframes of staff\n
    and department and returns dataframe with\n
    columns `staff_id`, `first_name`, `last_name`,\n
    `department_name`, `location`, `email_address`.

    Args:
    `input_df`: staff dataframe
    `input_df2`: department dataframe
    ---------------------------

    Returns:
    Formatted filtered dataframe.
    """
    df = input_df.copy()
    df2 = input_df2.copy()
    last_updated = df['last_updated']
    last_updated_date = [n.split(' ')[0] for n in last_updated]
    last_updated_at_time = [t.split(' ')[1]for t in last_updated]
    df['last_updated_date'] = last_updated_date
    df['last_updated_time'] = last_updated_at_time
    df_merge = pd.merge(df, df2, how='inner', on='department_id')
    filtered_merge = df_merge[['staff_id', 'first_name',
                               'last_name', 'department_name',
                               'location', 'email_address', 'last_updated_date', 'last_updated_time']]
    return filtered_merge
