import plotly_express as px
import csv
import numpy as np

def getDataSource(datapath):
    temp=[]
    icecreamSell=[]
    with open(datapath)as f:
        allData=csv.DictReader(f)

        for i in allData:
            temp.append(float(i["temp"]))
            icecreamSell.append(float(i["Icecream"]))

    return{"x":temp,"y":icecreamSell}
    


def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Temperature vs Ice Cream Sales :- \n--->",correlation[0,1])


def setup():
    datapath="tempeture.csv"
    data_source=getDataSource(datapath)
    findCorrelation(data_source)
    
    