## Filter growth rate function
# 
# 
## Author: Aksel Buur Christensen
# 
# 
import numpy as np 
from input_number import * 
def filterGrowthrate(data):
    # This function filters the growth rate by a chosen growth rate. 
    # Input: Data from the bacteria 
    # Output: Data from the specified growth rate(s)

    # Find the growthrate from the data
    growth = data[:,1]

    # Make an array of the rows in the growth 
    growth_row_number = np.arange(np.size(growth))

    # Input the lower bound for the growth rate
    lower = inputNumber('Please input the lower bound for the growth rate: ')

    # Setting the upper bound equal to the lower bound 
    upper = lower 

    # Use a while-loop to make sure the upper bound is greater than the lower bound 
    while upper <= lower: 
        upper = inputNumber('Please input the upper bound for the growth rate: ')

    # Using the the growth-row and filter this from the upper and lower bound to find the correct rows. 
    growth_row = growth_row_number[(growth > lower) & (growth < upper)]

    # Take all the data from the rows specified from the bounds to use for statistics/plot etc. 
    filteredData = data[growth_row, :]

    return filteredData
# print(filterGrowthrate(dataLoad('test.txt')))
    

