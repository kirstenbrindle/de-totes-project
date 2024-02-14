from pg8000.native import identifier


def L1_extract_data(conn, table_name):
    rows = conn.run(f'SELECT * FROM {identifier(table_name)};')

    if table_name == "payment_type":
        payment_type_list = format_payment_type(rows)
        return payment_type_list


def format_payment_type(payment_type_rows):
    """
    Args:
    takes a tuple of lists (the result of the SELECT\
    query on the payment_type).

    Returns:
    List of dictionaries containing rows of data with column\
    titles as keys.
    """
    if isinstance(payment_type_rows, list):
        payment_type_rows_list = [list(payment_type_rows)]
    else:
        payment_type_rows_list = list(payment_type_rows)
        # ^^we need this here to convert tuple to list^^
    payment_type_dict = {
        'payment_type_id': [],
        'payment_type_name': [],
        'created_at': [],
        'last_updated': []
    }
    for row in payment_type_rows_list:
        payment_type_dict['payment_type_id'].append(row[0])
        payment_type_dict['payment_type_name'].append(row[1])
        payment_type_dict['created_at'].append(row[2])
        payment_type_dict['last_updated'].append(row[3])
    return payment_type_dict
