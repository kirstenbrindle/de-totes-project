import pandas as pd
from io import BytesIO


def read_parquet(s3, bucket_name, file_name):
    """
    This function reads file from the processed bucket
    and transforms data to a dataframe.

    Args:
        `s3`: connection to AWS bucket
        `bucket_name`: processed bucket containing file
        `file_name`: file containing data to be read
    ---------------------------

    Returns:
        `df`: data from file transformed to dataframe
    """
    object = s3.get_object(
        Bucket=bucket_name,
        Key=file_name)

    df = pd.read_parquet(BytesIO(object['Body'].read()))

    return df
