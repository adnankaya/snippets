import os
from psycopg2 import sql, connect
from dotenv import load_dotenv
from pathlib import Path

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / '.env')


db_name = os.environ.get('DB_NAME')
db_host = os.environ.get('DB_HOST')
db_user = os.environ.get('DB_USER')
db_pass = os.environ.get('DB_PASSWORD')

import pdb; pdb.set_trace()

try:
    conn = connect(dbname=db_name,
                   host=db_host,
                   user=db_user,
                   password=db_pass)

    print("psycopg2 connection:", conn)


except Exception as err:
    print("psycopg2 connect() ERROR:", err)
    conn = None


def get_columns_names(table):
    columns = []
    col_cursor = conn.cursor()
    col_names_queryset = f"SELECT column_name FROM INFORMATION_SCHEMA.COLUMNS WHERE table_name='{table}';"

    try:
        sql_object = sql.SQL(col_names_queryset).format(sql.Identifier(table))
        col_cursor.execute(sql_object)
        col_names = (col_cursor.fetchall())
        print("\ncol_names:", col_names)

        for tup in col_names:
            columns.append(tup[0])

        col_cursor.close()

    except Exception as err:
        print("get_columns_names ERROR:", err)

    return columns


if conn != None:
    my_db_table = "t_item"
    columns = get_columns_names(my_db_table)

    print("columns:", columns)
    print("columns TYPE:", type(columns))
