import io
import pandas as pd


def read_parquet(s3, bucket_name, table_name, wh_conn, file_name):
    # read pq file from processed bucket that was triggered and save to df
    
    response = s3.get_object(Bucket=bucket_name, Key=file_name)
    pq_content = response['Body'].read().decode('utf-8')
    df = pd.read_parquet(io.StringIO(pq_content))

    # loads to db and if table exists (which they do) inserts new values
    # do not want the DF index as a table column
    df.to_sql(name=table_name, con=wh_conn, if_exists='append', index=False)


# needs testing completing