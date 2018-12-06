import urllib2

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/"
              "undocumented/connectionist-bench/sonar/sonar.all-data")


def main():
    data = urllib2.urlopen(target_url)
    xlist = []
    for line in data:
        row = line.strip().split(",")
        xlist.append(row)
    print("Number of Rows of Data = " + str(len(xlist)))
    print("Number of Columns of Data = " + str(len(xlist[1])))


if __name__ == '__main__':
    main()
