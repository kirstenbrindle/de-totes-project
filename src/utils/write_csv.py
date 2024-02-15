import pandas as pd
from datetime import datetime
from pathlib import Path
from src.utils.L1_extract_data import L1_extract_data
import boto3
import io
import botocore

# data = L1_extract_data(conn, table_name)
# ^^ data is the end result of the extract function
# poss add write csv to func????


def write_csv(table_name, bucket, data):
    """
    -> takes the output of SQL query
    -> write to .csv file with file name of "{tableName}-datetime.now()"
    -> uploads csv file to S3 ingestion bucket in folder/file format
    """

    # the file name
    current_dateTime = datetime.now()
    file_name = f'{table_name}-{current_dateTime}'

    # convert to a data frame
    df = pd.DataFrame.from_dict(data)

    # connect to s3 bucket
    s3 = boto3.client('s3')
    bucket_name = bucket
    key = (f'{table_name}/{file_name}.csv')

    # write data frame result to csv using filename declared above
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer)
    s3.put_object(Body=csv_buffer.getvalue(), Bucket=bucket_name, Key=key)

    # upload the file to the s3 ingestion bucket
    # s3.upload_file(key, bucket_name, f'{table_name}/{file_name}')
    # ^^ poss delete
