import urllib2
import numpy as np
from numpy import percentile
from locale import getpreferredencoding

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-databases/"
              "undocumented/connectionist-bench/sonar/sonar.all-data")
delimiter = '\t'
d_delimiter = '\t\t'

def getMeanAndStandardDevition(col, xlist):
    col_data = []
    for row in xlist:
        col_data.append(float(row[col]))

    col_array = np.array(col_data)
    col_mean = np.mean(col_array)
    col_std = np.std(col_array)
    
    print("Mean = " + str(col_mean))
    print("Standard Deviation = " + str(col_std))
    
    getPercentBoundary(4, col_array)
    
    getPercentBoundary(10, col_array)
    

def getPercentBoundary(ntiles, col_array):
    
    percentBoundary = []
     
    for i in range(ntiles + 1):
        percentBoundary.append(np.percentile(col_array, i * 100/ntiles))

    print("Boundaries for " + str(ntiles) + " Equal Percentiles " + str(percentBoundary))

def getCategoricalVariables(col, xlist):
    col_data = []
    for row in xlist:
        col_data.append(row[col])
    
    unique = set(col_data)
    
    print("Unique Label Values " + str(unique))
    
    count(unique, col_data)
    
    
def count(unique, col_data):
    catDict = dict(zip(list(unique), range(len(unique))))
    print("catDict" + str(catDict))
    
    
    catCount = [0]*2
    for elt in col_data:
        catCount[catDict[elt]] += 1
    print("Count for Each Value of Categorical Label" + str(list(unique)) + " " + str(catCount))

def main():
    data = urllib2.urlopen(target_url)
    xlist = []
    for line in data:
        row = line.strip().split(",")
        xlist.append(row)
    nrow = len(xlist)
    ncol = len(xlist[0])


    getMeanAndStandardDevition(3, xlist)
    
    # The last column contains categorical variables
    getCategoricalVariables(60, xlist)
    
    

if __name__ == '__main__':
    main()
