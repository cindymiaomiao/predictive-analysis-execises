import pandas as pd
import matplotlib.pyplot as plot

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/"
              "undocumented/connectionist-bench/sonar/sonar.all-data")


def main():
    # Read rocks versus mines data into pandas data frame
    rock_mines = pd.read_csv(target_url, header=None, prefix="V")

    cor_matrix = pd.DataFrame(rock_mines.corr())

    plot.pcolor(cor_matrix)
    plot.show()


if __name__ == '__main__':
    main()
