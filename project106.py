import plotly.express as px
import csv
import numpy as np

def plotFigure(datapath):
    with open(datapath) as csv_file:
        df = csv.DictReader(csv_file) 
        fig = px.scatter(df, x = "Coffee in ml", y = "sleep in hours")
        fig.show()

def getDataSource(datapath):
    coffee = []
    sleep = []
    with open(datapath) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            coffee.append(float(row["Coffee in ml"]))
            sleep.append(float(row["sleep in hours"]))
    return{"x": coffee, "y": sleep}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between cups of coffee and hours of sleep is: \n", correlation[0,1])

def main():
    datapath = "cups of coffee vs hours of sleep.csv"

    plotFigure(datapath)
    datasource = getDataSource(datapath)
    findCorrelation(datasource)

main()