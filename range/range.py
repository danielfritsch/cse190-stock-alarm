import csv
import pandas as pd 
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import sklearn
from sklearn.ensemble import IsolationForest
import os
import sys
data = pd.read_csv(open(os.path.join(sys.path[0], "AAPL.csv"), "r"))
def getRange(tickr):
    if(tickr=="AAPL"):
        data = pd.read_csv(open(os.path.join(sys.path[0], "AAPL.csv"), "r"))
    elif(tickr == "PANW"):
        data = pd.read_csv(open(os.path.join(sys.path[0], "PANW.csv"), "r"))
    elif(tickr == "AMZN"):
        data = pd.read_csv(open(os.path.join(sys.path[0], "AMZN.csv"), "r"))
    elif(tickr == "BABA"):
        data = pd.read_csv(open(os.path.join(sys.path[0], "BABA.csv"), "r"))
    elif(tickr == "FB"):
        data = pd.read_csv(open(os.path.join(sys.path[0], "FB.csv"), "r"))
    elif(tickr == "MSFT"):
        data = pd.read_csv(open(os.path.join(sys.path[0], "MSFT.csv"), "r"))
    elif(tickr == "NFLX"):
        data = pd.read_csv(open(os.path.join(sys.path[0], "NFLX.csv"), "r"))
    elif(tickr == "NVDA"):
        data = pd.read_csv(open(os.path.join(sys.path[0], "NVDA.csv"), "r"))
    elif(tickr == "SQ"):
        data = pd.read_csv(open(os.path.join(sys.path[0], "SQ.csv"), "r"))
    elif(tickr == "TSLA"):
        data = pd.read_csv(open(os.path.join(sys.path[0], "TSLA.csv"), "r"))
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
    return final