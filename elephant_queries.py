import psycopg2
from psycopg2.extras import DictCursor
from dotenv import load_dotenv

load_dotenv()

import os 

# for Pipenv users:
#pipenv install python-dotenv psycopg2-binary # NOTE: the "-binary"

# for conda users:
# pip install pandas python-dotenv psycopg2

DB_NAME = os.getenv("DB_NAME", default="PLEASE SET ENV file")
DB_USER = os.getenv("DB_USER", default="PLEASE SET ENV file")
DB_PASSWORD = os.getenv("DB_PASSWORD", default="PLEASE SET ENV file")
DB_HOST = os.getenv("DB_HOST", default="PLEASE SET ENV file")

### Connect to ElephantSQL-hosted PostgreSQL
conn = psycopg2.connect(dbname=DB_NAME, user=DB_USER,
                        password=DB_PASSWORD, host=DB_HOST)
print("connection", type(conn))
### A "cursor", a structure to iterate over db records to perform queries
cur = conn.cursor()
print("cursor", type(cur))
### An example query
cur.execute('SELECT * from test_table;')


### Note - nothing happened yet! We need to actually *fetch* from the cursor
result = cur.fetchone()

result2 = cur.fetchall()
for row in result2:
    print(type(row))
    print(row)

#alternative cursor to return dictionary:
#cursor = connection.cursor(cursor_factory=psycopg2.extras.DictCursor)