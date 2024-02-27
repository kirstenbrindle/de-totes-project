import pandas as pd
from io import BytesIO


def read_parquet(s3, bucket_name, file_name):
    object = s3.get_object(
        Bucket=bucket_name,
        Key=file_name)

    df = pd.read_parquet(BytesIO(object['Body'].read()))

    return df

