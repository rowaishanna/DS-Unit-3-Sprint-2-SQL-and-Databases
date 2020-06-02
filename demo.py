# importing sqlite 3 module

import sqlite3
# connecting to the database
connection = sqlite3.connect("demo_data.db")

#cursor
cursor = connection.cursor()

# CREATE A TABLE

sql = """
CREATE TABLE IF NOT EXISTS demo (s TEXT, x INTEGER, y INTEGER);
"""
cursor.execute(sql)

#
# INSERT DATA INTO THE PASSENGERS TABLE
#

insertion_query = """INSERT INTO demo VALUES ("'g'", 3, 9), ("'v'", 5, 7), ("'f'", 8,7);"""
cursor.execute(insertion_query)

# COMMIT
connection.commit() # actually save the records / run the transaction to insert rows

# QUERY


query1 = """
SELECT * from demo;
"""

cursor = connection.cursor()
result1 = cursor.execute(query1).fetchall()
print("Table contents", result1[0:][0:])
connection.commit()

############################################

query2 = """
SELECT COUNT( * ) as "Number of Rows" from demo;
"""
cursor = connection.cursor()
result2 = cursor.execute(query2).fetchall()
print("Number of rows", result2[0])
connection.commit()


###################
query3 = """
SELECT COUNT( * ) as "Number of Rows where both x and y are at least 5" from demo WHERE x>4 AND y>4;
"""

cursor = connection.cursor()
result3 = cursor.execute(query3).fetchall()
print("Number of rows where both x and y are at least 5", result3[0])
connection.commit()


######################################
query4 = """
SELECT COUNT (DISTINCT y) as "Unique values of y" from demo;
"""
cursor = connection.cursor()
result4 = cursor.execute(query4).fetchall()
print("Unique Values in 'y'", result4[0])
connection.commit()




# close
cursor.close()
connection.close()