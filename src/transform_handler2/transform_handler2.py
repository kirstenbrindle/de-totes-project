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
    # setup s3 client = s3
    # ingestion_bucket, file_name = get_key_name(event["Records"])
    # process_bucket_name = get_bucket_name(s3)
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

    pass
