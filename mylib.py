## define functions that to be imported into main.py
import matplotlib.pyplot as plt


def desripStats(dataframe):
    return dataframe.describe()


def plotScatter(x, y):
    # plot a scatter graph
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y)
    plt.xlabel("Weight, lbs")
    plt.ylabel("Miles per Gallon, miles")
    plt.title("Miles per gallon changes with automible weight")
    plt.show()


def findMin(dt):
    min_ind = 0
    for i in range(len(dt)):
        if dt[i] < dt[min_ind]:
            min_ind = i
    return dt[min_ind]


def findMax(dt):
    max_ind = 0
    for i in range(len(dt)):
        if dt[i] > dt[max_ind]:
            max_ind = i
    return dt[max_ind]


def calcMean(dt):
    total = 0
    for ele in dt:
        total += ele
    return round(total / len(dt), 3)
