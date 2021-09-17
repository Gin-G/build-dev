import sqlite3
from flask import Flask, escape, request, render_template
from werkzeug.exceptions import abort
from ESPNAPIs import *

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/NFLScores')
def NFLData():
    return get_scores()

@app.route('/NFLTeams')
def NFLTeams():
    return get_teams()

@app.route('/NFLStats')
def NFLStats():
    return get_stats()

@app.route('/ATL')
def ATL():
    return get_ATL()

@app.route('/BUF')
def BUF():
    return get_BUF()

@app.route('/CHI')
def CHI():
    return get_CHI()

@app.route('/CIN')
def CIN():
    return get_CIN()

@app.route('/Athletes')
def Athletes():
    return all_athletes()

if __name__ == '__main__':
    app.debug = True
    app.run()