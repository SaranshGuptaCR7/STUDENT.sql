import sqlite3
conn = sqlite3.connect('database.sql')
conn.execute('''CREATE TABLE IF NOT EXISTS Team3 (Name TEXT NOT NULL, Player_id INTEGER PRIMARY KEY, Address TEXT NOT NULL, Phone_no INTEGER , Age DEFAULT(24)), State TEXT NOT NULL)''')
conn.execute("INSERT INTO Team3 (Name, Player_id, Address, Phone_no, State) VALUES ('Micheal Jordan', 7, 'Portuguese, Europe', 5551234567, 'California')")
conn.commit()
import pandas as pd
table = pd.read_sql_query("SELECT * FROM sqlite_master WHERE type='table';", conn)
print(table)
team3 = pd.read_sql_query("SELECT * FROM Team3;", conn)
print(team3.head())