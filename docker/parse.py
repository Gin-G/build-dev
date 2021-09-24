import pandas as pd
import requests
import json

url = "https://www.footballguys.com/subscribers/teams/teampage-rav-1.php"
team_stats = pd.read_html(url)

QB = team_stats[1]
QB.drop(['YPA', 'FPT', 'Y/R'], axis=1, inplace=True)
qb_cols = ['Name', 'Games played', 'Completions', 'Attempts', 'Passing Yards', 'Passing Touchdowns', 'Interceptions', 'Rushing attempts', 'Rushing Yards', 'Rushing TDs']
QB.columns = qb_cols
print(QB)

RB = team_stats[2]
WR = team_stats[3]
TE = team_stats[4]
DT = team_stats[5]
DE = team_stats[6]
ILB = team_stats[7]
OLB = team_stats[8]
CB = team_stats[9]
S = team_stats[10]
K = team_stats[11]

'''
qbjson = {
    'Name' : QB.NAME,
    'Games played' : QB.G,
    'Attempts' : QB.ATT,
    'Completions' : QB.CMP,
    'Yards' : QB.PYD,
    'Touchdowns' : QB.PTD,
    'Interceptions' : QB.INT,
    'Rushing attempts' : QB.RSH,
    'Rushing Yards' : QB.YD,
    'Rushing TDs' : QB.TD
    }
'''
    


