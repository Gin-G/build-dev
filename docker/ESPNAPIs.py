import requests
import json
from jq import jq
from variables import *

def get_scores():
    data = requests.get(scores_url)
    return data.json()

def get_teams():
    data = requests.get(teams_url)
    return data.json()

def get_team():
    data = requests.get(team_url)
    return data.json()

def get_stats():
    data = requests.get(stats_url)
    return data.json()

def get_ATL():
    data = requests.get(ATL_url)
    return data.json()

def get_BUF():
    data = requests.get(BUF_url)
    return data.json()

def get_CHI():
    data = requests.get(CHI_url)
    return data.json()

def get_CIN():
    data = requests.get(CIN_url)
    return data.json()

def get_athletes():
    data = requests.get(athletes_url)
    return data.json()

def all_athletes():
    dict = []
    data = requests.get(athletes_url)
    jdata = data.json()
    players = jdata["items"]
    for links in players:
        player_url = links['$ref']
        player_info = requests.get(player_url)
        player_json = player_info.json()
        dict.append(player_json)
    done = json.dumps(dict)
    return done
