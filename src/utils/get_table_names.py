from pg8000.native import DatabaseError
import pg8000

def get_table_names(conn):
    """
    This function retrieves the table names from the database.

    Args:
    `conn`: database connection

    ---------------------------
    Returns:

    `table_names`: a List of table names sorted in alphabetical \n
    order.

    """
    try:
        query = conn.run("SELECT table_name "
                        "FROM information_schema.tables "
                        "WHERE table_schema='public' "
                        "AND table_type='BASE TABLE';")
        table_names = [table[0] for table in query]
        table_names.sort()

        # potential errors -
        # database error when query returns no information.
        # database error would only happen if no tables existed.
        return table_names

    except pg8000.exceptions.DatabaseError as DB:
        raise ValueError(DB)


