import csv
import sys
from datetime import datetime


def write_csv(tableName):
    """
    -> takes the output of SQL query
    -> write to .csv file with file name of "{tableName}-datetime.now()"
    -> uploads csv file to S3 ingestion bucket in folder/file format
    """
    
    current_dateTime = datetime.now()
    file_name = f'("${tableName}-${current_dateTime}")'

# Continue only if there are rows returned.
#     if rows:
# # New empty list called result. This will be written to a file.
#         result = list()

#     # The row name is the first entry for each entity in the description tuple.
#         column_names = list()
#         for i in cur.description:
#             column_names.append(i[0])

#         result.append(column_names)
#         for row in rows:
#             result.append(row)

    # write results to csv
    with open({file_name}.csv, 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        # for row in result:
        csvwriter.writerow('hello')

    # else:
    #     sys.exit("No rows found")