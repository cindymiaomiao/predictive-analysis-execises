import pandas as pd
from pandas import DataFrame
import matplotlib.pyplot as plot

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/"
              "undocumented/connectionist-bench/sonar/sonar.all-data")

# Read rocks versus mines data into pandas data frame
rockVMines = pd.read_csv(target_url, header=None, prefix = "V")

print(rockVMines.head())