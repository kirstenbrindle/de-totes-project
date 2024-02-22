import pyarrow as pa
import pyarrow.parquet as papq
import logging
from datetime import datetime
import io

logger = logging.getLogger('lambda2Logger')
logger.setLevel(logging.INFO)

def csv_parquet_converter(s3_client, bucket_name, table_name, data):
    table = pa.Table.from_pandas(data)
    file = io.BytesIO()
    papq.write_table(table, file)
    s3_client.put_object(
        Bucket= bucket_name,
        Body= file.getvalue(),
        Key= f'{table_name}/{table_name}-{datetime.now()}.parquet'
    )
    
'''
takes 4 arguments:
the s3 conenction,
the name of the bucket you want it to save in,
the name of the table you're converting
and the dataframe as a variable

converts 
'''
