import pandas as pd
import json
import os

pd.set_option('display.max_rows', None)

with open('teams.json') as teams:
    qbdf = rbdf = wrdf = tedf = pd.DataFrame()
    data = json.load(teams)
    for i in data:
        
        #os.makedirs("data/"+i["City"])
        
        team_stats = pd.read_html("https://www.footballguys.com/subscribers/teams/teampage-" + i["abr"] + "-1.php")

        QB = team_stats[1]
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

        qbdf = qbdf.append(QB)
        rbdf = rbdf.append(RB)
        wrdf = wrdf.append(WR)
        tedf = tedf.append(TE)              

qbdf.drop(['YPA', 'FPT', 'Y/R'], axis=1, inplace=True)
qb_cols = ['Name', 'Games played', 'Completions', 'Attempts', 'Passing Yards', 'Passing TDs', 'Interceptions', 'Rushing attempts', 'Rushing Yards', 'Rushing TDs']
qbdf.columns = qb_cols

rbdf.drop(['Y/R', 'Y/R.1', 'FPT'], axis=1, inplace=True)
rb_cols = ['Name', 'Games played', 'Rushing attempts', 'Rushing Yards', 'Rushing TDs', 'Targets', 'Receptions', 'Recieving Yards', 'Recieving TDs']
rbdf.columns = rb_cols

wrdf.drop(['Y/R', 'Y/R.1', 'FPT'], axis=1, inplace=True)
wrdf.columns = rb_cols

tedf.drop(['Y/R', 'FPT'], axis=1, inplace=True)
te_cols = ['Name', 'Games played', 'Targets', 'Receptions', 'Recieving Yards', 'Recieving TDs']
tedf.columns = te_cols

with open('data/QB_stats.txt', 'w') as f:
    f.write(str(qbdf.sort_values('Passing Yards')))
with open('data/RB_stats.txt', 'w') as g:
    g.write(str(rbdf))
with open('data/WR_stats.txt', 'w') as h:
    h.write(str(wrdf.sort_values(['Targets'], ascending=False)))
with open('data/TE_stats.txt', 'w') as i:
    i.write(str(tedf))

        #team_targets = pd.read_html("https://www.footballguys.com/subscribers/teams/teampage-" + i["abr"] + "-2.php")
        #team_rz = pd.read_html("https://www.footballguys.com/subscribers/teams/teampage-" + i["abr"] + "-3.php")
        #team_games = pd.read_html("https://www.footballguys.com/subscribers/teams/teampage-" + i["abr"] + "-4.php")
        #team_def = pd.read_html("https://www.footballguys.com/subscribers/teams/teampage-" + i["abr"] + "-5.php")
        #team_snaps = pd.read_html("https://www.footballguys.com/subscribers/teams/teampage-" + i["abr"] + "-6.php")

