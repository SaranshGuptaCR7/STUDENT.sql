import sqlite3
conn = sqlite3.connect('database.sql')
print("Data opened")
conn.execute('''CREATE TABLE IF NOT EXISTS Class_10 (Name TEXT NOT NULL, Roll_no INTEGER PRIMARY KEY, Adress TEXT NOT NULL, Addmission_no INTEGER NOT NULL, Phone_no INTEGER NOT NULL, Age DEFAULT(14))''')
conn.execute("INSERT INTO Class_10 (Name, Roll_no, Adress, Addmission_no, Phone_no) VALUES ('General Dyer', 911, 'Shivam Nagra, Britain, Europe', 134911, 5551234567)")
conn.commit()
print("Records inserted")
import pandas as pd
table = pd.read_sql_query("SELECT * FROM sqlite_master WHERE type='table';", conn)
print(table)
class_10d = pd.read_sql_query("SELECT * FROM Class_10;", conn)
print(class_10d.head())