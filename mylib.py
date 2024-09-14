## define functions that to be imported into main.py
import matplotlib.pyplot as plt


def plotScatter(x, y):
    # plot a scatter graph
    plt.figure(figsize=(10, 6))
    plt.scatter(x, y)
    plt.xlabel("Weight, lbs")
    plt.ylabel("Miles per Gallon, miles")
    plt.title("Miles per gallon changes with automible weight")
    plt.show()
