import pandas as pd
import os
import socket
def is_connected():
    try:
        # connect to the host -- tells us if the host is actually
        # reachable
        socket.create_connection(("1.1.1.1", 53))
        return True
    except OSError:
        pass
    return False
# Get link to the execute .py file -->full_path
full_path = os.path.realpath(__file__)
#Get link to the folder that have the executable file  --> path
path, filename = os.path.split(full_path)
path , dirname= os.path.split(path)
def GetNewData() :
    if not is_connected(): 
        print("NO INTERNET")
        return pd.read_pickle(path+"\\CovidData\\coviddata.pkl",compression='bz2')
    df = pd.read_csv("https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/owid-covid-data.csv")
    #print(len(df))
    #df.to_csv(path+"\\coviddata.csv")
    df.to_pickle(path+"\\CovidData\\coviddata.pkl",compression='bz2')
    return df
def ReadData():
    try:
        return pd.read_pickle(path+"\\CovidData\\coviddata.pkl",compression='bz2')
    except:
        return GetNewData() 