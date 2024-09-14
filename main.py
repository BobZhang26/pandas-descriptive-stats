"""
Main cli or app entry point
"""

import pandas as pd
import matplotlib.pyplot as plt
from mylib import plotScatter

# define a function to provide descriptive statistics of a dataset


def desripStats(dataframe):
    return dataframe.describe()


def findMin(data):
    min_ind = 0
    for i in range(len(data)):
        if data[i] < data[min_ind]:
            min_ind = i
    return data[min_ind]


def findMax(data):
    max_ind = 0
    for i in range(len(data)):
        if data[i] > data[max_ind]:
            max_ind = i
    return data[max_ind]


def calcMean(data):
    total = 0
    for ele in data:
        total += ele
    return round(total / len(data), 3)


if __name__ == "__main__":
    file = "https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv"
    data = pd.read_csv(file)

    # descriptive statistics
    desripStats(data)

    # run some test cases: mean, min and max of the 'mpg'
    # minimum
    min_mpg = findMin(data["mpg"])
    print("minimum of 'mpg': ", min_mpg)

    # maximum
    max_mpg = findMax(data["mpg"])
    print("maximum of 'mpg': ", max_mpg)

    # mean
    mean_mpg = calcMean(data["mpg"])
    print("mean of 'mpg': ", mean_mpg)

    print(desripStats(data))
    # ensure that the data contains 'wt' and 'mpg' columns
    if "wt" in data.columns and "mpg" in data.columns:
        plotScatter(data["wt"], data["mpg"])
        plt.show()  # 添加这一行来显示图表
        # save the plot
        # plt.savefig("scatter.png")
    else:
        print("Data does not contain 'wt' or 'mpg' columns")
