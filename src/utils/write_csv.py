import pandas as pd
from datetime import datetime
import io


def write_csv(table_name, bucket, s3, data):
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
    bucket_name = bucket
    key = (f'{table_name}/{file_name}.csv')

    # write data frame result to csv using filename declared above
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer)
    # upload straight to S3 bucket
    s3.put_object(Body=csv_buffer.getvalue(), Bucket=bucket_name, Key=key)
