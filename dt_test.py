from datetime import datetime

# example from database table, last_updated column
db_date = '2022-11-03 14:20:52.186'
print(db_date, 'database last_updated format')

# example of datetime.now() format
print(datetime.now(), 'datetime.now() format')

# need to chop off last 2 digits to make formats match
timestamp = str(datetime.now())[:-3]
print(timestamp, 'datetime.now() formatted to match db')


