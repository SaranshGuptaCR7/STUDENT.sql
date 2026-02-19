import sqlite3
database = 'database.sqlite'
conn = sqlite3.connect(database)    
print("Opened database successfully")
import pandas as pd
tables = pd.read_sql("SELECT * FROM sqlite_master WHERE type='table';", conn)
print(tables)
matches = pd.read_sql("SELECT * FROM matches;", conn)
print(matches)
matches.head()
result = pd.read_sql("SELECT * FROM matches WHERE Season_id = 7 GROUP BY Match_Winner ORDER BY AVG(Win_Margin);", conn)
print(result)
result2 = pd.read_sql("SELECT COUNT(DISTINCT Venue_id) FROM Matches WHERE Season_id = 7;", conn)
print(result2)
result3 = pd.read_sql("SELECT MIN(Win_Margin), MAX(Win_Margin), AVG(Win_Margin), COUNT(DISTINCT Man_of_the_Match) FROM Matches;", conn)
print(result3)
result4 = pd.read_sql("SELECT SUM(Win_Margin) FROM Matches WHERE Season_id = 7;", conn)
print(result4)
