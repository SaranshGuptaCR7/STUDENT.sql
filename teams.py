import sqlite3
conn = sqlite3.connect('database.sql')
print("Data opened")
conn.execute('''CREATE TABLE IF NOT EXISTS Team2 (Name TEXT NOT NULL, Player_id INTEGER PRIMARY KEY, Adress TEXT NOT NULL, Phone_no INTEGER NOT NULL, Age DEFAULT(24))''')
conn.execute("INSERT INTO Team2 (Name, Player_id, Adress, Phone_no) VALUES ('Cristiano Ronaldo', 07, 'Portugese, Europe', 5551234567)")
conn.commit()
print("Records inserted")
import pandas as pd
table = pd.read_sql_query("SELECT * FROM sqlite_master WHERE type='table';", conn)
print(table)
team2 = pd.read_sql_query("SELECT * FROM Team2;", conn)
print(team2.head())