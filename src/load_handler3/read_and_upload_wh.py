import pandas as pd
import os


def read_and_upload(s3, bucket_name, table_name, wh_conn, file_name):
    # read pq file from processed bucket that was triggered and save to df
    print(os.environ["AWS_ACCESS_KEY_ID"])
    path = f's3://{bucket_name}/{file_name}'

    df = pd.read_parquet(path)

    # loads to db and if table exists (which they do) inserts new values
    # do not want the DF index as a table column
    df.to_sql(name=table_name, con=wh_conn, if_exists='append', index=False)


# needs testing completing
