# from src.load_handler3.upload_data import upload_data
# from unittest.mock import Mock
# import pytest
# import psycopg2
# import pandas as pd


# @pytest.fixture(scope='function')
# def db_conn():
#     """Connection to test_warehouse"""
#     user = 'kirsten-brindle'
#     password = 'password'
#     host = 'localhost'
#     database = 'test_warehouse'
#     return psycopg2.connect(user=user, password=password,
#                             host=host, database=database)


# @pytest.mark.describe("upload_data")
# @pytest.mark.it("test uploads data with test_db")
# def test_uploads_data_into_test_db(db_conn):
#     data = {
#         'currency_id': [3, 4],
#         'currency_code': ['GBP', 'USD'],
#         'currency_name': ['British pound sterling',
#                         'United States dollar']
#     }
#     row_labels = [0, 1]
#     test_df = pd.DataFrame(data=data, index=row_labels)
#     upload_data(db_conn, 'test_currency', test_df)
#     query = db_conn.cursor('SELECT * FROM test_currency;')
#     assert query == [[1, 'GBP', 'British pound sterling',],
#                     [2, 'USD', 'United States dollar',]]
