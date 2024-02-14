import csv 
import pandas as pd
from datetime import datetime
from pathlib import Path

def write_csv():
    """
    -> takes the output of SQL query
    -> write to .csv file with file name of "{tableName}-datetime.now()"
    -> uploads csv file to S3 ingestion bucket in folder/file format
    """
    #collect data output from query sql function
    data=QUERYFUNCTIONPATH

    #the file name 
    tableName=
    current_dateTime = datetime.now()
    file_name = f'("${tableName}-${current_dateTime}")'

   # convert to a data frame
    df=pd.DataFrame.from_dict(data,orient='index')
    # write data frame result to csv
    df.to_csv(f'{file_name}.csv')