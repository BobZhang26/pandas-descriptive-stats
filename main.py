"""
Main cli or app entry point
"""

import pandas as pd
import matplotlib.pyplot as plt
from mylib import plotScatter, desripStats, findMin, findMax, calcMean


if __name__ == "__main__":
    # load from csv file from url
    file = (
        "https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b"
        "/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv"
    )
    # read the data
    data = pd.read_csv(file)

    # descriptive statistics
    desripStats(data)

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
