import pandas as pd
from pandas import DataFrame

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/"
              "undocumented/connectionist-bench/sonar/sonar.all-data")


def main():
    # Read rocks versus mines data into pandas data frame
    rock_mines = pd.read_csv(target_url, header=None, prefix="V")

    print(rock_mines.head())

    print(rock_mines.tail())

    summary = rock_mines.describe()
    print(summary)


if __name__ == '__main__':
    main()
