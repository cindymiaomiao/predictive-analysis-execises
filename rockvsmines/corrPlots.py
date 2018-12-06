import pandas as pd
import matplotlib.pyplot as plot

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/"
              "undocumented/connectionist-bench/sonar/sonar.all-data")


def main():
    # Read rocks versus mines data into pandas data frame
    rock_mines = pd.read_csv(target_url, header=None, prefix="V")

    # calculate correlations between real-valued attributes
    data2 = rock_mines.iloc[1, 0:60]
    data3 = rock_mines.iloc[2, 0:60]

    plot.scatter(data2, data3)
    plot.xlabel("2nd Attribute")
    plot.ylabel("3rd Attribute")

    plot.show()


if __name__ == '__main__':
    main()
