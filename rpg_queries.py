import os
import sqlite3
# construct a path to wherever your database exists

DB_FILEPATH = os.path.join(os.path.dirname(__file__), "RPG_ASSIGNMENT.sqlite3")
connection = sqlite3.connect(DB_FILEPATH)
connection.row_factory = sqlite3.Row # allow us to reference rows as dicts
#print("CONNECTION:", connection)
cursor = connection.cursor()
print("CURSOR", cursor)


query = """
SELECT 
	count(distinct name) as Total_Character_Count
	FROM charactercreator_character;
"""


#print("RESULT", result) #> returns cursor object w/o results (need to fetch the results)
result = cursor.execute(query).fetchall()
for row in result:
	print(row["Total_Character_Count"])

connection.commit()
connection.close()



query2 = """

SELECT 
	count(distinct character_ptr_id) as Mage_Count
	FROM charactercreator_mage;
SELECT 
	count(distinct character_ptr_id) as cleric_Count
	FROM charactercreator_cleric;
SELECT 
	count(distinct character_ptr_id) as Fighter_Count
	FROM charactercreator_fighter;
SELECT 
	count(distinct mage_ptr_id) as necromancer_Count
	FROM charactercreator_necromancer;
SELECT 
	count(distinct character_ptr_id) as thief_Count
	FROM charactercreator_thief;
"""

query3 = """
SELECT 
	count(distinct name) as Total_Item_Count
	FROM armory_item;
"""

query4 = """
SELECT 
	count(distinct item_ptr_id) as Weapon_Count
	FROM armory_weapon;
"""
query5 = """
SELECT
	character_id
	,COUNT(DISTINCT item_id) as Items_per_Character
	FROM charactercreator_character_inventory
GROUP BY character_id
LIMIT 20;
"""
query6 = """
SELECT
	charactercreator_character_inventory.character_id
	,charactercreator_character_inventory.item_id
	,count(distinct armory_weapon.item_ptr_id) as Weapon_Count
FROM charactercreator_character_inventory
JOIN armory_weapon 
on charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
GROUP BY charactercreator_character_inventory.character_id
LIMIT 20;
"""

query7= """
SELECT 
  avg(Items_per_Character) as avg_items_per_character
FROM (
    SELECT
	character_id
	,COUNT(DISTINCT item_id) as Items_per_Character
	FROM charactercreator_character_inventory
GROUP BY character_id
) subq;
"""

query8= """
SELECT
	avg(Weapon_Count) as avg_weapon_per_character
FROM (
	SELECT
		charactercreator_character_inventory.character_id
		,charactercreator_character_inventory.item_id
		,count(distinct armory_weapon.item_ptr_id) as Weapon_Count
	FROM charactercreator_character_inventory
	JOIN armory_weapon 
	on charactercreator_character_inventory.item_id = armory_weapon.item_ptr_id
	GROUP BY charactercreator_character_inventory.character_id
) subq;
"""

'''
result2 = cursor.execute(query2).fetchall()
print("RESULT 2", result2)
result3 = cursor.execute(query3).fetchall()
result4 = cursor.execute(query4).fetchall()
result5 = cursor.execute(query5).fetchall()
result6 = cursor.execute(query6).fetchall()
result7 = cursor.execute(query7).fetchall()
result8 = cursor.execute(query8).fetchall()
'''


