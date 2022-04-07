# -*- coding: utf-8 -*-
"""
Created on Thu Mar 24 09:40:38 2022

@author: cglitz
"""
#data statistics of data matrix 
#input: matrix; output: result: A scalar containing the calculated statistic.

#statistic Description:
#Mean Temperature: Mean (average) Temperature.
#Mean Growth rate: Mean (average) Growth rate.
#Std Temperature: Standard deviation of Temperature.
#Std Growth rate: Standard deviation of Growth rate.
#Rows: The total number of rows in the data.
#Mean Cold Growth rate: Mean (average) Growth rate when Temperature is less than 20 degrees.
#Mean Hot Growth rate: Mean (average) Growth rate when Temperature is greater than 50 degrees

import numpy as np
from dataLoad import dataLoad

data_file = dataLoad("test.txt")
statistic_test = "mean cold growth rate"

def dataStatistics(data, statistic):
    
    if statistic == "mean temperature":
        result = np.mean(data[:,0])
    
    elif statistic == "mean growth rate":
        result = np.mean(data[:,1])
    
    elif statistic == "std temperature":
        result = np.std(data[:,0])
    
    elif statistic == "std growth rate":
        result = np.std(data[:,1])
    
    elif statistic == "rows":
        result = len(data)
        
    elif statistic == "mean cold growth rate":
        temp_under_20 = data[:,0] < 20
        cold_matrix = data[temp_under_20,:]
        result = np.mean(cold_matrix[:,1])
    
    elif statistic == "mean hot growth rate":
        temp_over_50 = data[:,0] > 50
        hot_matrix = data[temp_over_50,:]
        result = np.mean(hot_matrix[:,1])
        
    else:
        result = "please enter a valid input for statistics"
    
    print(statistic + ' = {:.2f}'.format(dataStatistics(data, statistic)))

    return result
print(dataStatistics(data_file, statistic_test))


#datastatistics with filter 
# if filter is turned on, only statistics of those are calculated because inout file (data) has changed.
#No change in function required but: description of filter has to be shown while ca 
