"""
Problem Statement :
Find the variance for the following set of data representing trees in California (heights in
feet):
3,21,98,203,17,9
"""

arr = [3,21,98,203,17,9]

print("Calculation using statistics library")
import statistics as stat
print(str("Mean " + str(stat.mean(arr))))
print(str("Variance " + str(stat.variance(arr))))
print(str("std_dev " + str(stat.stdev(arr))))



