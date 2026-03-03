import pandas as pd
import sqlite3
database = 'match2.sqlite'
conn = sqlite3.connect(database)
table = pd.read_sql("SELECT * FROM sqlite_master WHERE type='table';", conn)
print(table)
print("All data from match table")
teams =pd.read_sql("SELECT * FROM Team;", conn)
print("Teams:\n", teams)
season = pd.read_sql("SELECT * FROM Season;", conn)
print("Season:\n", season)
CSK_matche_2015 = pd.read_sql('''
                            SELECT Match_id, Team_2 AS Away_team, Toss_Winner, Match_Winner
                              FROM Match
                              WHERE(Team_1 = 3 OR Team_2 = 3) AND Season_id = 8;
                              ''', conn)
print("CSK matches in 2015:\n", CSK_matche_2015)
CSK_wins = pd.read_sql('''
                       SELECT * FROM Match
                       WHERE Match_Winner = 3 AND Season_id = 8;
                       ''', conn)
print("CSK wins in 2015:\n", CSK_wins)
match_runs = pd.read_sql('''
                          SELECT Match_id, Runs_scored, Innings_No
                         FROM Batsman_Scored
                         Where Runs_scored > 5
                         AND Match_id IN(
                         SELECT Match_id
                         FROM Match
                         WHERE Season_id = 8);
                          ''', conn)
print("Matches with runs scored greater tha 5 in 2015:\n", match_runs)
avg_runs = pd.read_sql('''
                        SELECT Match_id, Runs_scored, Innings_No
                        FROM Batsman_Scored
                       WHERE Innings_No = 1
                       AND Runs_scored >(
                       SELECT AVG(Runs_scored)
                       FROM Batsman_Scored);
                        ''', conn)
print("Matches with runs scored greater than average in 2015:\n", avg_runs)
conn.close()