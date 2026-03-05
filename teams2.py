import sqlite3
conn = sqlite3.connect('database.sql')
conn.execute('''CREATE TABLE IF NOT EXISTS Team2 (Name TEXT NOT NULL, Player_id INTEGER PRIMARY KEY, Address TEXT NOT NULL, Phone_no INTEGER , Age DEFAULT(24))''')
conn.execute("INSERT INTO Team2 (Name, Player_id, Address, Phone_no) VALUES ('Cristiano Ronaldo', 7, 'Portuguese, Europe', 5551234567)")
conn.commit()
import pandas as pd
table = pd.read_sql_query("SELECT * FROM sqlite_master WHERE type='table';", conn)
print(table)
team2 = pd.read_sql_query("SELECT * FROM Team2;", conn)
print(team2.head())