from pg8000.native import identifier


def L1_extract_data(conn, table_name):
    rows = conn.run(f'SELECT * FROM {identifier(table_name)};')
    column_names=conn.columns
    #column_names = [c['name'] for c in conn.columns]
    print('<<<<<<<',column_names,'this is column name')
    if table_name == "payment_type":
        payment_type_list = format_data(rows,column_names)
        return payment_type_list


def format_data(rows,column_names):
    """
    Args:
    takes a tuple of lists (the result of the SELECT\
    query on the payment_type) as the first argument.
    takes a list of column names as the second argument.

    Returns:
    List of dictionaries containing rows of data with column\
    titles as keys.
    """
    print(">>>>>>>", column_names)
    if isinstance(rows, list):
        rows_list = [list(rows)]
    else:
        rows_list = list(rows)
        # ^^we need this here to convert tuple to list^^
    nested_data_list=[]
    for n in range(0,len(column_names)):
        data_list=[]
        for row in rows_list:
            data_list.append(row[n])
            
        nested_data_list.append(data_list)
   
    payment_type_dict=dict(zip(column_names,nested_data_list))
    print(payment_type_dict)
    return payment_type_dict
