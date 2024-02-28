from pg8000.native import identifier
import logging
import pandas as pd

logger = logging.getLogger('lambda3Logger')
logger.setLevel(logging.INFO)


def upload_data(conn, table_name, df):
    """
    This function takes extracted file data from read_parquet,
    transforms to suitable SQL format and inputs
    data into correct table in warehouse database

    Args:
        `conn`: connection to warehouse database
        `table_name`: table for data input
        `df`: data for input
    ---------------------------

    Returns:
        Nothing to return
    """
    try:
        input_df.fillna(value='NULL', inplace=True)
        df1 = input_df.replace("Democratic People\'s Republic of Korea", 'Democratic People''s Republic of Korea')
        df2 = df1.replace("O\'Keefe",'O''Keefe')
        df = df2.replace("irving.o\'keefe@terrifictotes.com",'irving.o''keefe@terrifictotes.com')
        # df = input_df.replace("\'", "''", regex=True)
        df_tuples = [tuple(x) for x in df.to_numpy()]
        cols = ", ".join(df.columns)
        logger.info(f'Columns: {cols}')

        values = ''
        for item in df_tuples:
            values += f"{item}, "
        values = values[:-2]

        insert_str = f"INSERT INTO {identifier(table_name)} "
        insert_str += f"({cols}) "
        insert_str += f"VALUES {values};"

        conn.run(insert_str)
        conn.run('COMMIT')
    except Exception as e:
        logger.error(e)
        logger.warning(f'Something has gone wrong in upload_data.py with {table_name}')
