# Load data function 
#
# Author: Aksel Buur Christensen, s203947
# 
import numpy as np
def dataLoad(filename):
    # This function reads a N x 3 text file 
    # The function uses space as a separator between the data. 
    # If the load-function detects an incomplete line, it gives an error-message, skip the line and continues. 
    # The function filters 10 < Temperature < 60, Growth Rate > 0, 1 <= Bacteria <= 4. 
    
    # The unfiltered data is loaded 
    unfiltered = np.loadtxt(filename, delimiter = ' ')
    #print(unfiltered)

    # The variables are loaded into different functions 
    temp = unfiltered[:,0]
    growth = unfiltered[:,1]
    bacteria = unfiltered[:,2]

    # Use the filters for temperature, growth rate, bacteria
    indexTemp = (temp > 10) & (60 > temp)
    indexGrowth = growth > 0
    indexBacteria = (bacteria == 1) | (bacteria == 2) | (bacteria == 3) | (bacteria == 4)

    # Merging the indexes into a filtered index
    indexMerg = indexTemp * indexGrowth * indexBacteria

    # The filtered data then becomes
    data = unfiltered[indexMerg,:]
    
    # Now we must return error-messages when a line is incomplete/missing data. 
    # Creating a list for all lines - REMEMBER 0-index. 
    lines = np.arange(np.size(temp))
    # print(lines)
    # Using if any() statements, using the indexes from before that are an 'true'/'false'-array, if there is any false statements, it is saved into a new index, which can be accesed from the lines.
    if any(indexTemp == False):
        falseindexTemp = (indexTemp == False)
        print('There is temperatures that does not fit our filters. The problems is in the following line(s), remember 0-index:')
        print(lines[falseindexTemp])

    if any(indexGrowth == False):
        falseindexGrowth = (indexGrowth == False)
        print('There is growth rates that does not fit our filters. The problems is in the following line(s), remember 0-index:')
        print(lines[falseindexGrowth])
    
    if any(indexBacteria == False):
        falseindexBacteria = (indexBacteria == False)
        print('There is bacteria-numbers that does not fit our filters. The problems is in the following line(s), remember 0-index:')
        print(lines[falseindexBacteria])
        print("")

    return data 
# print(dataLoad('test.txt'))