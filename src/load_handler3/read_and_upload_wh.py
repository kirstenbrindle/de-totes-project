import pandas as pd
import os
import logging

logger = logging.getLogger('lambda3Logger')
logger.setLevel(logging.INFO)
# need to update file!!
def read_and_upload(s3, bucket_name, table_name, wh_conn, file_name):
    try:
        # read pq file from processed bucket that was triggered and save to df
        print(os.environ["AWS_ACCESS_KEY_ID"])
        path = f's3://{bucket_name}/{file_name}'

        df = pd.read_parquet(path)

        # loads to db and if table exists (which they do) inserts new values
        # do not want the DF index as a table column
        df.to_sql(name=table_name, con=wh_conn, if_exists='append', index=False)
    except Exception as e:
        logger.error(e)
        logger.info("Something has happened in the read_and_upload_wh.py...")

# needs testing completing
