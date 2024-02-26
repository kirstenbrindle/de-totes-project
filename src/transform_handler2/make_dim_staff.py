import pandas as pd


def make_dim_staff(input_df, input_df2):
    '''Function takes 2 dataframes of staff and department
    and returns dataframe '''
    df = input_df.copy()
    df2 = input_df2.copy()
    df_merge = pd.merge(df, df2, how='inner', on='department_id')
    filtered_merge = df_merge[['staff_id', 'first_name',
                               'last_name', 'department_name',
                               'location', 'email_address']]
    return filtered_merge
