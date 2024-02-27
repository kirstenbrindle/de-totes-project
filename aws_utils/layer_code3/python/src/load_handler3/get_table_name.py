import logging

logger = logging.getLogger('lambda1Logger')
logger.setLevel(logging.INFO)


def get_table_name(file_name):
    '''
    Function takes the file path and name used to trigger the lambda3

    Splits at "/" and 1 returns table_name

    Returns:
    "table_name"
    '''
    try:
        split_file_name = file_name.split("/", 1)
        table_name = split_file_name[0]
        return table_name
    except Exception as e:
        logger.info("something has gone wrong in the get_table_name.py")
        logger.warning(e)
