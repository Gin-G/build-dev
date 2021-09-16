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

print(jq(get_teams()))
