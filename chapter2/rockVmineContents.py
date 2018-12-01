import urllib2

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
    ncol = len(xlist[0])

    t = [0] * 3
    col_counts = []
    for col in range(ncol):
        for row in xlist:
            try:
                a = float(row[col])
                if isinstance(a, float):
                    t[0] += 1
            except ValueError:
                if len(row[col]) > 0:
                    t[1] += 1
                else:
                    t[2] += 1
        col_counts.append(t)
        t = [0] * 3
    print("Col#" + delimiter + "Number" + delimiter + "String" + delimiter + "Other")

    index = 0
    for col in col_counts:
        print(str(index) + d_delimiter + str(col[0]) + d_delimiter + str(col[1]) + d_delimiter + str(col[2]))
        index += 1


if __name__ == '__main__':
    main()
