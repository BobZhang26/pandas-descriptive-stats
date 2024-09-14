"""
Test goes here
"""

# Path: test_main.py

# test read data
from mylib import desripStats, findMin, findMax, calcMean
import pandas as pd

# load from csv file from url
file = (
    "https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b"
    "/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv"
)
data = pd.read_csv(file)


# test whether this file exists
def test_read_data():
    dataframe = pd.read_csv(file)
    assert dataframe is not None


def test_min():
    assert desripStats(data)["mpg"]["min"] == findMin(data["mpg"])


def test_max():
    assert desripStats(data)["mpg"]["max"] == findMax(data["mpg"])


def test_mean():
    assert round(desripStats(data)["mpg"]["mean"], 3) == round(calcMean(data["mpg"]), 3)


if __name__ == "__main__":
    file = (
        "https://gist.githubusercontent.com/seankross/a412dfbd88b3db70b74b"
        "/raw/5f23f993cd87c283ce766e7ac6b329ee7cc2e1d1/mtcars.csv"
    )
    test_read_data()
    print("file exists")

    # test descriptive statistics
    # test minimum
    test_min()
    print("minimum passed")

    # test maximum
    test_max()
    print("maximum passed")

    # test mean
    test_mean()
    print("mean passed")
