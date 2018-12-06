import pylab
import scipy.stats as stats
import urllib2

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/"
              "undocumented/connectionist-bench/sonar/sonar.all-data")


def main():
    
    data = urllib2.urlopen(target_url)
    xlist = []
    for line in data:
        row = line.strip().split(",")
        xlist.append(row)
    ncol = len(xlist[0])
    nrow = len(xlist)
    
    col = 3
    col_data = []
    for row in xlist:
        col_data.append(float(row[col]))
        
    stats.probplot(col_data, dist="norm", plot=pylab)
    pylab.show()



if __name__ == '__main__':
    main()
