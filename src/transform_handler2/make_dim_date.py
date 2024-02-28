import pandas as pd
from datetime import datetime

def make_dim_date(start='2022-11-01', end='2032-12-31'):
    """
    This function takes 2 strings as default date values \n
    and returns a dataframe with columns 'year', 'month', \n
    'day', 'day_of_week', 'day_name', 'month_name', 'quarter'.


    Args:
    `start`: start date of range
    `end`: end date of range
    ---------------------------

    Returns:
    Dataframe of date values with columns 'year', 'month',
    'day', 'day_of_week', 'day_name', 'month_name', 'quarter'.

    Errors:
    Raises no errors.
    """
    dim_date_df = pd.DataFrame({"Date": pd.date_range(start, end)})
    dim_date_df.rename(columns={"Date": "date_id"}, inplace=True)
    dim_date_df["year"] = dim_date_df.date_id.dt.year
    dim_date_df["month"] = dim_date_df.date_id.dt.month
    dim_date_df["day"] = dim_date_df.date_id.dt.day
    dim_date_df["day_of_week"] = dim_date_df.date_id.dt.day_of_week
    dim_date_df["day_name"] = dim_date_df.date_id.dt.day_name()
    dim_date_df["month_name"] = dim_date_df.date_id.dt.month_name()
    dim_date_df["quarter"] = dim_date_df.date_id.dt.quarter
    date_time = dim_date_df["date_id"]
    date=[str(n).split(' ')[0] for n in date_time]
    dim_date_df["date_id"] = date

    dim_date_df['last_updated'] = str(datetime.now())
    last_updated = dim_date_df['last_updated']
    last_updated_date = [n.split(' ')[0] for n in last_updated]
    last_updated_at_time = [t.split(' ')[1]for t in last_updated]
    dim_date_df['last_updated_date'] = last_updated_date
    dim_date_df['last_updated_time'] = last_updated_at_time
    dim_date_df.drop(columns=['last_updated'], inplace=True)
    return dim_date_df


#str(n).split(' ')[0]