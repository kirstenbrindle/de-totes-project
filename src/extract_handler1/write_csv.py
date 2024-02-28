import pandas as pd
from datetime import datetime
import io


def write_csv(table_name, bucket, s3, data):
    """
     This function takes data from an sql query and writes it to csv.

     Args:
        `table_name` the name of the table the data is from
        `bucket` the name of the s3 bucket to write to
        `s3` the aws connection
        `data` the data from the query

     ---------------------------
     Returns:
        no return
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
