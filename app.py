from flask import Flask
from flask_cors import CORS, cross_origin
import finnhub
import csv
import pandas as pd 
import warnings
import numpy as np
import sklearn
from sklearn.ensemble import IsolationForest
import os
import sys

warnings.filterwarnings("ignore")

finnhub_client = finnhub.Client(api_key="c2fdbl2ad3ien4444lpg")

app = Flask(__name__)
CORS(app)

@app.route("/percent_change/<ticker>")
def percent_change(ticker):
	quote = finnhub_client.quote(ticker)
	return { 'percent_change': ((quote['c'] - quote['o']) / quote['o']) * 100}

@app.route("/get_sensitivity_range/<ticker>/<sensitivity>")
def get_sensitivity_range(ticker, sensitivity):
	medium_range = getRange(ticker)

	final_range = [-1 * medium_range, medium_range]
	if sensitivity == "LOW":
		print("YO YO")
		sens_adjusted_range = medium_range * 2
		final_range = [-1 * sens_adjusted_range, sens_adjusted_range]
	elif sensitivity == "HIGH":
		sens_adjusted_range = medium_range / 2
		final_range = [-1 * sens_adjusted_range, sens_adjusted_range]

	return { 'range': final_range }

def getRange(tickr):
    if(tickr=="AAPL"):
        data = pd.read_csv(open(os.path.join(sys.path[0], "data/AAPL.csv"), "r"))
    elif(tickr == "PANW"):
        data = pd.read_csv(open(os.path.join(sys.path[0], "data/PANW.csv"), "r"))
    elif(tickr == "AMZN"):
        data = pd.read_csv(open(os.path.join(sys.path[0], "data/AMZN.csv"), "r"))
    elif(tickr == "BABA"):
        data = pd.read_csv(open(os.path.join(sys.path[0], "data/BABA.csv"), "r"))
    elif(tickr == "FB"):
        data = pd.read_csv(open(os.path.join(sys.path[0], "data/FB.csv"), "r"))
    elif(tickr == "MSFT"):
        data = pd.read_csv(open(os.path.join(sys.path[0], "data/MSFT.csv"), "r"))
    elif(tickr == "NFLX"):
        data = pd.read_csv(open(os.path.join(sys.path[0], "data/NFLX.csv"), "r"))
    elif(tickr == "NVDA"):
        data = pd.read_csv(open(os.path.join(sys.path[0], "data/NVDA.csv"), "r"))
    elif(tickr == "SQ"):
        data = pd.read_csv(open(os.path.join(sys.path[0], "data/SQ.csv"), "r"))
    elif(tickr == "TSLA"):
        data = pd.read_csv(open(os.path.join(sys.path[0], "data/TSLA.csv"), "r"))
    else:
        return "Coming Soon"

    data['Percentage_Change'] = (data['Close']-data['Open'])/data['Open']
    data = data['Percentage_Change']
    data = data.abs()
    data = 100*data
    data = data.to_numpy()
    data = data.reshape(-1,1)
    clf = IsolationForest(random_state=0,n_jobs=-1).fit(data)
    i=0
    a_range = []
    while(i<=100):
        if(clf.predict([[i]])==1):
            a_range.append(i)
        i = i+0.1
    final = a_range[-1]
    return round(final, 2)