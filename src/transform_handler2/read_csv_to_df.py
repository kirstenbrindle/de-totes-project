import pandas as pd
import logging

logger = logging.getLogger('lambda2Logger')
logger.setLevel(logging.INFO)


def read_csv_to_df(file_name):
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
            df = pd.read_csv(file_name)
            return df
        else:
            raise TypeError
    except FileNotFoundError:
        logger.error("Specified file cannot be found")
    except TypeError:
        logger.error("File type incorrect, must be csv format")
