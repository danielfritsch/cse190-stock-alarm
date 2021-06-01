import csv
import pandas as pd 
import warnings
warnings.filterwarnings("ignore")
import numpy as np
import sklearn
from sklearn.ensemble import IsolationForest
#degree "low", "medium","high"
data = pd.read_csv("./AAPL.csv")
def machine_learning(tickr):
    if(tickr=="AAPL"):
        data = pd.read_csv("./AAPL.csv")
    elif(tickr == "PANW"):
        data = pd.read_csv("./PANW.csv")
    elif(tickr == "AMZN"):
        data = pd.read_csv("./AMZN.csv")
    elif(tickr == "BABA"):
        data = pd.read_csv("./BABA.csv")
    elif(tickr == "FB"):
        data = pd.read_csv("./FB.csv")
    elif(tickr == "MSFT"):
        data = pd.read_csv("./MSFT.csv")
    elif(tickr == "NFLX"):
        data = pd.read_csv("./NFLX.csv")
    elif(tickr == "NVDA"):
        data = pd.read_csv("./NVDA.csv")
    elif(tickr == "SQ"):
        data = pd.read_csv("./SQ.csv")
    elif(tickr == "TSLA"):
        data = pd.read_csv("./TSLA.csv")
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
    final = []
    while(i<=100):
        if(clf.predict([[i]])==1):
            a_range.append(i)
        i = i+0.1
    final = [a_range[0],a_range[-1]]
    return final
