from pg8000.native import identifier, literal, Connection
from src.utils.get_most_recent_file import get_most_recent_file
from src.utils.flexible_formater import format_data
from src.utils.get_timestamp import get_timestamp
import boto3 
import json 

def L1_extract_data(conn, table_name, boolean):
    query_string = f'SELECT * FROM {identifier(table_name)}'
    if boolean is True:
        conn.run(f'{query_string};')
    else:
        latest_file = get_most_recent_file(table_name)
        timestamp = get_timestamp(latest_file)
        query_string += f' WHERE last_updated > {literal(timestamp)};'
        response = conn.run(query_string)
        metadata = conn.columns
        column_names = [c['name'] for c in metadata]
        format_data(response, column_names)
    # if table_name == "payment_type":
    #     payment_type_list = format_payment_type(rows)
    #     return payment_type_list

# extract data function takes connection, table name and boolean
#  variable called query string - select * from table nam. If boolean is true we run full query.
#  if false we invoke get most recent file with table name
    # then get timestamp is invoked with result of most recent file. 
    # Add WHERE clause to query string with timestamp. Then we run conn.run with query string. 
    # if query response is empty, we use logger.info(message)
    # else, we invoke format data 
    # then we invoke write to csv and write to object.

# testing - queries are pulling out valid data. 
    # other functions have been invoked

# flexible formatter created and format payment type no longer required:

# def format_payment_type(payment_type_rows):
#     """
#     Args:
#     takes a tuple of lists (the result of the SELECT\
#     query on the payment_type).

#     Returns:
#     List of dictionaries containing rows of data with column\
#     titles as keys.
#     """
#     if isinstance(payment_type_rows, list):
#         payment_type_rows_list = [list(payment_type_rows)]
#     else:
#         payment_type_rows_list = list(payment_type_rows)
#         # ^^we need this here to convert tuple to list^^
#     payment_type_dict = {
#         'payment_type_id': [],
#         'payment_type_name': [],
#         'created_at': [],
#         'last_updated': []
#     }
#     for row in payment_type_rows_list:
#         payment_type_dict['payment_type_id'].append(row[0])
#         payment_type_dict['payment_type_name'].append(row[1])
#         payment_type_dict['created_at'].append(row[2])
#         payment_type_dict['last_updated'].append(row[3])
#     return payment_type_dict
