import pandas as pd
import logging
import io

logger = logging.getLogger('lambda2Logger')
logger.setLevel(logging.INFO)


def read_csv_to_df(s3, bucket_name, file_name):
    """
This function reads a csv file and returns the contents as a dataframe.

Arg:

`file_name`: string of the csv file name

---------------------------
Returns:

`dataframe`: a dataframe


"""
    try:
        if file_name.endswith(".csv"):
            file_name = file_name.replace('+', ' ')
            file_name = file_name.replace('%3A', ':')
            logger.info(f'currently reading from csv {file_name}')
            response = s3.get_object(
                Bucket=bucket_name,
                Key=file_name
            )
            csv_content = response['Body'].read().decode('utf-8')
            df = pd.read_csv(io.StringIO(csv_content))
            return df
        else:
            raise TypeError
    except FileNotFoundError:
        logger.error("Specified file cannot be found")
    except TypeError:
        logger.error("File type incorrect, must be csv format")
    except Exception as error:
        if error.response['Error']['Code'] == 'NoSuchKey':
            logger.error(error.response['Error']['Message'])
            logger.info(error)
            logger.info(file_name)
