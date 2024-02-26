import boto3
import logging
from botocore.exceptions import ClientError
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
    try:
        ingestion_bucket, file_name = get_file_and_ingestion_bucket_name(
            event['Records'])
        s3 = boto3.client('s3', region_name='eu-west-2')

        processed_bucket = get_bucket_name_2(s3)
        logger.info(f'Reading {file_name} currently ...')


        if 'sales_order' in file_name:
            df = read_csv_to_df(s3, ingestion_bucket, file_name)
            fact_sales_order_df = make_fact_sales_order(df)
            write_to_parquet(s3, processed_bucket,
                             'fact_sales_order', fact_sales_order_df)
            
        elif 'design' in file_name:
            df = read_csv_to_df(s3, ingestion_bucket, file_name)
            dim_design_df = make_dim_design(df)
            write_to_parquet(s3, processed_bucket,
                             'dim_design', dim_design_df)
            
        elif 'currency' in file_name:
            dim_date_df = make_dim_date()
            write_to_parquet(s3, processed_bucket,
                             'dim_date', dim_date_df)
            df = read_csv_to_df(s3, ingestion_bucket, file_name)
            dim_currency_df = make_dim_currency(df)
            write_to_parquet(s3, processed_bucket,
                             'dim_currency', dim_currency_df)
            
            
        elif 'address' in file_name:
            df = read_csv_to_df(s3, ingestion_bucket, file_name)
            dim_location_df = make_dim_location(df)
            write_to_parquet(s3, processed_bucket,
                             'dim_location', dim_location_df)
            
        elif 'sales_order' in file_name:
            df = read_csv_to_df(s3, ingestion_bucket, file_name)
            fact_sales_order_df = make_fact_sales_order(df)
            write_to_parquet(s3, processed_bucket,
                             'fact_sales_order', fact_sales_order_df)
            
        elif 'counterparty' in file_name:
            df = read_csv_to_df(s3, ingestion_bucket, file_name)
            address_file = get_most_recent_file_2(
                s3, ingestion_bucket, 'address')
            address_df = read_csv_to_df(s3, ingestion_bucket, address_file)
            dim_counterparty_df = make_dim_counterparty(df, address_df)
            write_to_parquet(s3, processed_bucket,
                             'dim_counterparty', dim_counterparty_df)
        elif 'staff' in file_name:
            df = read_csv_to_df(s3, ingestion_bucket, file_name)
            department_file = get_most_recent_file_2(
                s3, ingestion_bucket, 'department')
            department_df = read_csv_to_df(
                s3, ingestion_bucket, department_file)
            dim_staff_df = make_dim_staff(df, department_df)
            write_to_parquet(s3, processed_bucket,
                             'dim_staff', dim_staff_df)
        else:
            logger.info("Non-MVP data: update not needed")
    except ValueError as v:
        logger.error(v)
        logger.error("There is no processed bucket ...")

    except ClientError as c:
        if c.response['Error']['Code'] == 'NoSuchBucket':
            logger.error(f'No such bucket - {processed_bucket}')
        else:
            logger.info(c)
            logger.error("A ClientError has occurred")

    except Exception as e:
        logger.error(e)
        raise RuntimeError
