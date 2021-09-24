import pandas as pd
import json
import os

pd.set_option('display.max_rows', None)

def get_qb_data():
    with open('teams.json') as teams:
        qbdf = pd.DataFrame()
        data = json.load(teams)
        for i in data:
            team_stats = pd.read_html("https://www.footballguys.com/subscribers/teams/teampage-" + i["abr"] + "-1.php")
            QB = team_stats[1]
            qbdf = qbdf.append(QB)
    qbdf.drop(['YPA', 'FPT', 'Y/R'], axis=1, inplace=True)
    qb_cols = ['Name', 'Games played', 'Completions', 'Attempts', 'Passing Yards', 'Passing TDs', 'Interceptions', 'Rushing attempts', 'Rushing Yards', 'Rushing TDs']
    qbdf.columns = qb_cols
    return qbdf.to_dict(orient='records')

def get_rb_data():
    with open('teams.json') as teams:
        rbdf = pd.DataFrame()
        data = json.load(teams)
        for i in data:
            team_stats = pd.read_html("https://www.footballguys.com/subscribers/teams/teampage-" + i["abr"] + "-1.php")
            RB = team_stats[2]
            rbdf = rbdf.append(RB)
    rbdf.drop(['Y/R', 'Y/R.1', 'FPT'], axis=1, inplace=True)
    rb_cols = ['Name', 'Games played', 'Rushing attempts', 'Rushing Yards', 'Rushing TDs', 'Targets', 'Receptions', 'Recieving Yards', 'Recieving TDs']
    rbdf.columns = rb_cols
    return str(rbdf.sort_values(['Rushing attemps'], ascending=True)) 

def get_wr_data():
    with open('teams.json') as teams:
        wrdf = pd.DataFrame()
        data = json.load(teams)
        for i in data:
            team_stats = pd.read_html("https://www.footballguys.com/subscribers/teams/teampage-" + i["abr"] + "-1.php")
            WR = team_stats[3]
            wrdf = wrdf.append(WR)
    wrdf.drop(['Y/R', 'Y/R.1', 'FPT'], axis=1, inplace=True)
    wr_cols = ['Name', 'Games played', 'Rushing attempts', 'Rushing Yards', 'Rushing TDs', 'Targets', 'Receptions', 'Recieving Yards', 'Recieving TDs']
    wrdf.columns = wr_cols
    return str(wrdf.sort_values(['Targets'], ascending=True))

def get_te_data():
    with open('teams.json') as teams:
        tedf = pd.DataFrame()
        data = json.load(teams)
        for i in data:
            team_stats = pd.read_html("https://www.footballguys.com/subscribers/teams/teampage-" + i["abr"] + "-1.php")
            TE = team_stats[4]
            tedf = tedf.append(TE)
    tedf.drop(['Y/R', 'FPT'], axis=1, inplace=True)
    te_cols = ['Name', 'Games played', 'Targets', 'Receptions', 'Recieving Yards', 'Recieving TDs']
    tedf.columns = te_cols
    return str(tedf.sort_values(['Targets'], ascending=True)) 

