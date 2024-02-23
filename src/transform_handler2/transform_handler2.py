import boto3
import logging
from src.transform_handler2.get_file_and_ingestion_bucket_name import (
    get_file_and_ingestion_bucket_name)
from src.transform_handler2.get_bucket_name_2 import (
    get_bucket_name_2
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

    get_bucket_name_2(s3)

    # boolean = is_bucket_empty(s3, process_bucket_name)
    # if boolean is true - get_most_recent_file() -
    # Variables for each - sales_order, design, address, currency,
    # staff, department, counterparty and should be saved as variables.
    # dataframes = read_csv_to_df(Variables for each - sales_order, design,
    # address, currency, staff, department, counterparty)
    # Invoke each make_dim format function and pass in needed dataframes.
    # Output of dim format functions are passed into write_to_parquet function

    # If boolean is False
    # Use filename from get_key_name - read file with read_csv_to_df(file_name)
    # - saved as a dataframe.
    # if file_name contains sales_order - invoke make_dim_sales_order().
    #  if file_name contains design - invoke make_dim_design() formatter func.
    # Output of dim sales order or dim design passed into write_to_parquet.
