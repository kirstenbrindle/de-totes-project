import pandas as pd


def make_dim_date(start='2022-11-01', end='2032-12-31'):
    dim_date_df = pd.DataFrame({"Date": pd.date_range(start, end)})
    dim_date_df.rename(columns={"Date": "date_id"}, inplace=True)
    dim_date_df["year"] = dim_date_df.date_id.dt.year
    dim_date_df["month"] = dim_date_df.date_id.dt.month
    dim_date_df["day"] = dim_date_df.date_id.dt.day
    dim_date_df["day_of_week"] = dim_date_df.date_id.dt.day_of_week
    dim_date_df["day_name"] = dim_date_df.date_id.dt.day_name()
    dim_date_df["month_name"] = dim_date_df.date_id.dt.month_name()
    dim_date_df["quarter"] = dim_date_df.date_id.dt.quarter
    return dim_date_df
