import csv 
import pandas as pd
from datetime import datetime
from pathlib import Path
from src.utils import L1_extract_data
import boto3
import botocore


def checkPath(table_name):
        result = s3.list_objects(Bucket=bucket_name, Prefix=table_name )
        exists=False
        if 'Contents' in result:
            exists=True
        return exists


def write_csv(table_name,L1_extract_data,conn):
    """
    -> takes the output of SQL query
    -> write to .csv file with file name of "{tableName}-datetime.now()"
    -> uploads csv file to S3 ingestion bucket in folder/file format
    """
    #collect data output from query sql function
    data=L1_extract_data(conn,table_name)

    #the file name 
    current_dateTime = datetime.now()
    file_name = f'"${table_name}-${current_dateTime}"'

   # convert to a data frame
    df=pd.DataFrame.from_dict(data,orient='index')
    

    #connect to s3 bucket
    s3=boto3.client('s3')
    bucket_name=f"{aws_s3_bucket.ingestion_bucket.bucket_prefix}"

    #list filenames in s3 bucket 
    #object_read_list=s3.list_objects(bucket_name)
    #bucket_filenames=[]
    #if 'Content' in object_read_list:
    #   for file in object_read_list['Content']:
    #       bucket_filenames.append(file['key'])
    #   return bucket_filenames
    
    #check if folder exist
     =checkPath(table_name):
        

        'we will go to s3 bucket table_name'
        #if true return file path
        'filepath={file_name}.csv'
    #if false create file path
    else:filepath=Path(f'{table_name}/{file_name}.csv')


    # write data frame result to csv
    df.to_csv(filepath)

    #upload the file to the s3 ingestion bucket

    s3.upload_file(filepath,bucket_name)