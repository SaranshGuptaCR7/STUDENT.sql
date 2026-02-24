import pandas as pd
import numpy as np
import sqlite3
databse = 'database.sqlite'
conn = sqlite3.connect('database.sqlite')
print("Data opened")
tables = pd.read_sql_query("SELECT name FROM sqlite_master WHERE type='table';", conn)
print("Tables in the database:")
print(tables)
player_match = pd.read_sql_query("SELECT * FROM Player_Match;", conn)
print("\nFirst 5 rows of player_match table:")
print(player_match.head())
null_player_match = pd.read_sql_query("SELECT * FROM Player_Match WHERE Player_Id IS NULL;", conn)
print("\nRows in player_match table with NULL Player_Id:")  
print(null_player_match.head())
match_table = pd.read_sql_query("SELECT * FROM Match;", conn)
print("\nFirst 5 rows of Match table:")
print(match_table.head())
null_match = pd.read_sql_query("SELECT * FROM Match WHERE Match_Id IS NULL;", conn)
print("\nRows in Match table with NULL Match_Id:")
print(null_match.head())
conn.close()
print("\nDatabase connection closed.")