import urllib2
import numpy as np

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/"
              "undocumented/connectionist-bench/sonar/sonar.all-data")
delimiter = '\t'
d_delimiter = '\t\t'


def main():
    data = urllib2.urlopen(target_url)
    xlist = []
    for line in data:
        row = line.strip().split(",")
        xlist.append(row)
    nrow = len(xlist)
    ncol = len(xlist[0])

    t = [0] * 3
    col_counts = []

    col = 3
    col_data = []
    for row in xlist:
        col_data.append(float(row[col]))

    col_array = np.array(col_data)


if __name__ == '__main__':
    main()
