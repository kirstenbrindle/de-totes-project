import pyarrow as pa
import pyarrow.parquet as papq
import logging
from datetime import datetime
import io

logger = logging.getLogger('lambda2Logger')
logger.setLevel(logging.INFO)


def write_to_parquet(s3_client, bucket_name, olap_table, data):
    """
    This function takes a dataframe and rewrites
    the dataframe to the s3 processed bucket as a parquet file.

    Args:
        `s3_client`: s3 client connection
        `bucket_name`: s3 bucket_name
        `olap_table`: table name
        `data`: dataframe
    ---------------------------

    Returns:
        No return value.
    """
    table = pa.Table.from_pandas(data)
    file = io.BytesIO()
    papq.write_table(table, file)
    s3_client.put_object(
        Bucket=bucket_name,
        Body=file.getvalue(),
        Key=f'{olap_table}/{olap_table}-{datetime.now()}.parquet'
    )
