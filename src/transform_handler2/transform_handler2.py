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
    pass
