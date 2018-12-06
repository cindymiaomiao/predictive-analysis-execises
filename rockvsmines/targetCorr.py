import pandas as pd
import matplotlib.pyplot as plot
import random as rand

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/"
              "undocumented/connectionist-bench/sonar/sonar.all-data")


def method1(rock_mines):
    target = []
    for i in range(208):
        if rock_mines.iat[i, 60] == 'M':
            target.append(1.0)
        else:
            target.append(0.0)

    data_row = rock_mines.iloc[0:208, 35]
    plot.scatter(data_row, target)

    plot.xlabel("Attribute Value")
    plot.ylabel("Target Value")
    plot.show()


def method2(rock_mines):
    target = []
    for i in range(208):
        if rock_mines.iat[i, 60] == 'M':
            target.append(1.0 + rand.uniform(-0.1, 0.1))
        else:
            target.append(0.0 + rand.uniform(-0.1, 0.1))

    data_row = rock_mines.iloc[0:208, 35]
    plot.scatter(data_row, target, alpha=0.5, s=120)

    plot.xlabel("Attribute Value")
    plot.ylabel("Target Value")
    plot.show()


def main():
    # Read rocks versus mines data into pandas data frame
    rock_mines = pd.read_csv(target_url, header=None, prefix="V")
    method2(rock_mines)


if __name__ == '__main__':
    main()
