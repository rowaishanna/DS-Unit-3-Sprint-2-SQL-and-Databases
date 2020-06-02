import os
import sqlite3
# construct a path to wherever your database exists

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "northwind_small.sqlite3")
connection = sqlite3.connect(DB_FILEPATH)
#connection.row_factory = sqlite3.Row # allow us to reference rows as dicts
#print("CONNECTION:", connection)
cursor = connection.cursor()
#print("CURSOR", cursor)

# 10 most expensive items per unit price Query:
query = """
SELECT ProductName, UnitPrice FROM Product ORDER by UnitPrice DESC LIMIT 10;
"""


result = cursor.execute(query).fetchall()
print ("10 most expensive items per unit price", result[0:][0:])
connection.commit()



# Employees' Average Age at time of hiring:
query2 = """

SELECT avg("Age at time of hire") as "Avg Age at time of hire" FROM 
(SELECT Id, BirthDate, HireDate
, datetime(HireDate) - datetime(BirthDate) AS "Age at time of hire" from Employee) subq;
"""

cursor = connection.cursor()
result2 = cursor.execute(query2).fetchall()
print("Employees' Average Age at time of hiring", result2[0:][0:])
connection.commit()

############################################

# 10 most expensive items per unit price and their suppliers:
query3 = """

SELECT Product.ProductName, Product.SupplierID, Product.UnitPrice FROM Product 
JOIN Supplier on Product.SupplierId = Supplier.ID  
ORDER by UnitPrice DESC LIMIT 10;

"""

cursor = connection.cursor()
result3 = cursor.execute(query3).fetchall()
print("10 most expensive items per unit price and their suppliers", result3[0:][0:])
connection.commit()

###############

# largest category number of unique products: 

query4 = """
SELECT max("Products_per_Category") as 'largest_category' 
FROM (
SELECT Product.CategoryId, COUNT (DISTINCT Product.Id) as Products_per_Category
FROM Product
JOIN Category on PRODUCT.CategoryId = Category.Id 
GROUP BY CategoryId) subq;

"""

cursor = connection.cursor()
result4 = cursor.execute(query4).fetchall()
print("largest category by number of unique products", result4[0:][0:])
connection.commit()


# close
cursor.close()
connection.close()