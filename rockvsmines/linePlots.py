import pandas as pd
import matplotlib.pyplot as plot

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/"
              "undocumented/connectionist-bench/sonar/sonar.all-data")


def main():
    # Read rocks versus mines data into pandas data frame
    rock_mines = pd.read_csv(target_url, header=None, prefix="V")

    for i in range(208):
        if rock_mines.iat[i, 60] == 'M':
            pcolor = "red"
        else:
            pcolor = "blue"

        # plot rows of data as if they were series data
        data_row = rock_mines.iloc[i, 0:60]
        data_row.plot(color=pcolor)
    plot.xlabel("Attribute Index")
    plot.ylabel("Attribute Value")
    plot.show()


if __name__ == '__main__':
    main()
