from pg8000.native import identifier
import logging

logger = logging.getLogger('lambda3Logger')
logger.setLevel(logging.INFO)


def upload_data(conn, table_name, df):
    df_tuples = [tuple(x) for x in df.to_numpy()]

    cols = ", ".join(df.columns)
    logger.info(f'Columns: {cols}')

    values = ''
    for item in df_tuples:
        if "O\'Keefe" in item:
            item = list(item)
            item[2] = 'O''Keefe'
            item = tuple(item)
        values += f"{item}, "
    values = values[:-2]

    insert_str = f"INSERT INTO {identifier(table_name)} "
    insert_str += f"({cols}) "
    insert_str += f"VALUES {values};"

    conn.run(insert_str)
