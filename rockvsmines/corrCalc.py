import pandas as pd
import numpy as np

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/"
              "undocumented/connectionist-bench/sonar/sonar.all-data")

def main():
    # Read rocks versus mines data into pandas data frame
    rock_mines = pd.read_csv(target_url, header=None, prefix="V")

    data2 = rock_mines.iloc[1, 0:60]
    data3 = rock_mines.iloc[2, 0:60]
    data21 = rock_mines.iloc[21, 0:60]

    mean2 = np.mean(data2)
    mean3 = np.mean(data3)
    mean21 = np.mean(data21)

    var2 = np.std(data2)
    var3 = np.std(data3)
    var21 = np.std(data21)

    nums = len(data2)
    corr23 = 0.0
    corr221 = 0.0
    for i in range(nums):
        corr23 += (data2[i] - mean2) * (data3[i] - mean3) / (var2 * var3 * nums)
        corr221 += (data2[i] - mean2) * (data21[i] - mean21) / (var2 * var21 * nums)

    print("Correlation between attribute 2 and attribute 3 = " + str(corr23))
    print("Correlation between attribute 2 and attribute 21 = " + str(corr221))


if __name__ == '__main__':
    main()
