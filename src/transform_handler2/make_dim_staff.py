import pandas as pd 
def make_dim_staff(df, df2):
    '''Function takes 2 dataframes of staff and department and returns dataframe '''
    concat = pd.concat([df,df2], axis=1, join='inner')
    dim_staff = concat[['staff_id', 'first_name', 'last_name', 'department_name',
                          'location', 'email_address']]
    print(dim_staff)
    return dim_staff