import boto3
import logging
from src.transform_handler2.get_file_and_ingestion_bucket_name import (
    get_file_and_ingestion_bucket_name)
from src.transform_handler2.get_bucket_name_2 import (
    get_bucket_name_2
)
from src.transform_handler2.is_bucket_empty_2 import (
    is_bucket_empty_2
)
from src.transform_handler2.get_most_recent_file_2 import (
    get_most_recent_file_2
)
from src.transform_handler2.read_csv_to_df import (
    read_csv_to_df
)
from src.transform_handler2.make_dim_counterparty import (
    make_dim_counterparty
)
from src.transform_handler2.make_dim_currency import (
    make_dim_currency
)
from src.transform_handler2.make_dim_date import (
    make_dim_date
)
from src.transform_handler2.make_dim_design import (
    make_dim_design
)
from src.transform_handler2.make_dim_location import (
    make_dim_location
)
from src.transform_handler2.make_dim_staff import (
    make_dim_staff
)
from src.transform_handler2.make_fact_sales_order import (
    make_fact_sales_order
)
from src.transform_handler2.write_to_parquet import (
    write_to_parquet
)

logger = logging.getLogger('lambda2Logger')
logger.setLevel(logging.INFO)


def lambda_handler(event, context):
    '''Reads files from the ingestion bucket and
     reformat the data.

    Writes the data as parquet files in the processed bucket.

    Returns:
        None

    Raises:
        RuntimeError: An unexpected error occurred in execution. Other errors
        result in an informative log message.
    '''
    ingestion_bucket, file_name = get_file_and_ingestion_bucket_name(
        event["Records"])
    s3 = boto3.client('s3', region_name='eu-west-2')

    processed_bucket = get_bucket_name_2(s3)
    table_names = ['sales_order', 'design', 'address', 'currency',
                   'staff', 'department', 'counterparty']

    if is_bucket_empty_2(s3, processed_bucket):
        recent_files = [get_most_recent_file_2(
            s3, ingestion_bucket, table) for table in table_names]
        dim_dfs = [read_csv_to_df(s3, ingestion_bucket, file)
                   for file in recent_files]
        dim_counterparty_df = make_dim_counterparty(dim_dfs[6], dim_dfs[2])
        dim_currency_df = make_dim_currency(dim_dfs[3])
        dim_date_df = make_dim_date()
        dim_design_df = make_dim_design(dim_dfs[1])
        dim_location_df = make_dim_location(dim_dfs[2])
        dim_staff_df = make_dim_staff(dim_dfs[4], dim_dfs[5])
        fact_sales_order_df = make_fact_sales_order(dim_dfs[0])

        write_to_parquet(s3, processed_bucket,
                         'dim_counterparty', dim_counterparty_df)
        write_to_parquet(s3, processed_bucket, 'dim_currency', dim_currency_df)
        write_to_parquet(s3, processed_bucket, 'dim_date', dim_date_df)
        write_to_parquet(s3, processed_bucket, 'dim_design', dim_design_df)
        write_to_parquet(s3, processed_bucket, 'dim_location', dim_location_df)
        write_to_parquet(s3, processed_bucket, 'dim_staff', dim_staff_df)
        write_to_parquet(s3, processed_bucket,
                         'fact_sales_order', fact_sales_order_df)
    else:
        df = read_csv_to_df(s3, ingestion_bucket, file_name)
        if 'sales_order' in file_name:
            fact_sales_order_df = make_fact_sales_order(df)
            write_to_parquet(s3, processed_bucket,
                             'fact_sales_order', fact_sales_order_df)
        if 'design' in file_name:
            dim_design_df = make_dim_design(df)
            write_to_parquet(s3, processed_bucket, 'dim_design', dim_design_df)
