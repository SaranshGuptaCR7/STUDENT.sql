import pandas as pd
import sqlite3
database = 'match.sqlite'
conn = sqlite3.connect(database)
table = pd.read_sql("SELECT * FROM sqlite_master WHERE type='table';", conn)
print(table)
print("All data from match table")
match_details = pd.read_sql('''
                            SELECT
                            m.Season_id
                            m.Match_id
                            v.Venue_name
                            c.City_name
                            t.Team_name as Winner
                            FROM Match AS m
                            INNER JOIN Venue AS v ON m.Venue_id = v.Venue_id
                            INNER JOIN City AS c ON v.City_id = c.City_id
                            INNER JOIN Team AS t ON m.Winner_id = t.Team_id
                            ''', conn)
print("Match Details:\n", match_details)
conn.close()