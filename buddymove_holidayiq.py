""" Python SQL queries"""

import pandas as pd
import numpy as np
import sqlite3
import os
from pandas import DataFrame
from sqlalchemy import create_engine

df = pd.read_csv('https://archive.ics.uci.edu/ml/machine-learning-databases/00476/buddymove_holidayiq.csv')
print(df.shape)
#%%
df.isnull().sum()
#%%

# create a connection
DB_FILEPATH = os.path.join(os.path.dirname(__file__), "buddymove_holidayiq.sqlite3")
conn = sqlite3.connect(DB_FILEPATH)
conn.row_factory = sqlite3.Row # allow us to reference rows as dicts

# Inserting Pandas DataFrames into a Database Using the to_sql() Function
df.to_sql(
    name = 'Holiday',
    schema='main',
    con=conn,
    index = False,
    if_exists = 'replace'
)

# commit changes
conn.commit()
#%%

curs = conn.cursor()

# Count how many rows you have - it should be 249!
query = "SELECT count(*) FROM Holiday;"
curs.execute(query).fetchall()
#%%

# How many users who reviewed at least 100 Nature in the category also reviewed at least 100 
# in the Shopping category?
query = "Select count(*) FROM Holiday where Nature >= 100 AND Shopping >= 100;"
curs.execute(query).fetchall()
#%%

# (Stretch) What are the average number of reviews for each category?
query = "SELECT avg(Sports), avg(Religious), avg(Nature), avg(Theatre), avg(Shopping), avg(Picnic) from Holiday ;"
curs.execute(query).fetchall()
#%%

curs.close()
conn.commit()