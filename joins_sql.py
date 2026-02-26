import numpy as np
import sqlite3
import pandas as pd
database = 'database.sqlite'
conn = sqlite3.connect(database)
table = pd.read_sql("SELECT * FROM sqlite_master WHERE type='table';", conn)
print(table)
joined_city = pd.read_sql("SELECT c.Country_ID, c.City_Name, ci.City_Name FROM country c INNER JOIN city ci ON c.Country_ID == ci.Country_ID;", conn)
print(joined_city)
joined_left = pd.read_sql('''SELECT *
                          FROM player
                          LEFT JOIN season
                          ON player.Player_Id = season.Player_Id;''', conn)
print(joined_left)
joined_cross = pd.read_sql('''SELECT c.Country_ID, c.Country_Name, ci.City_Name
                           FROM country c
                           CROSS JOIN city ci''', conn)
print(joined_cross)
joined_union = pd.read_sql('''SELECT Player_Name
                           FROM Player
                           UNION
                           SELECT Team_Name
                            FROM Team''', conn)
print(joined_union)