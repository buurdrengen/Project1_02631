# Data-plot function 
# 
# Author: Aksel Buur Christensen, s203947 
# 
import numpy as np 
import matplotlib.pyplot as plt 
# from dataLoad import * 
def dataPlot(data):
    # This function makes two plots.
    # 1) A histogram of the numbers of each the four bacterias in the data-file. 
    # 2) A plot of growth-rate by temperature, to see whether the growth is temperature dependent. 
    
    # Making a list of the bacteria-types
    bacteria = data[:,2]

    # Counting the different types of bacteria
    y1 = np.count_nonzero(bacteria == 1)
    y2 = np.count_nonzero(bacteria == 2)
    y3 = np.count_nonzero(bacteria == 3)
    y4 = np.count_nonzero(bacteria == 4)
    
    bacnames = ['Salmonella enterica','Bacillus cereus','Listeria','Brochothrix thermosphacta']
    # x_bacteria = ['1','2','3','4'] # Array for the x-axis. 

    fig, (ax1, ax2) = plt.subplots(1,2) # Create a figure with subplots, here ax1 is the first plot and ax2 is the second plot.

    y_bacteria = np.array([y1,y2,y3,y4]) # Create an array with the different types of bacteria. 

    ax1.set_title('Number of bacterias') # Title for the first subplot
    ax1.set_ylabel('Number') # y-label for the first subplot
    ax1.set_xlabel('Bacteria type') # x-label for the first subplot
    ax1.bar(x_bacteria,y_bacteria,color=['red','green','blue','yellow']) # Plotting the histogram in the first subplot

    # 2) Plot "Growth Rate by Temperature"
    plt.xlim([10,60]) # Limits for the x-axis. 

    # Sorting for the temperature 
    temp = np.argsort(data[:,0])
    
    # bacteria_1row = ( bacteria == 1) 
    # bacteria_2row = ( bacteria == 2)
    # bacteria_3row = ( bacteria == 3)
    # bacteria_4row = ( bacteria == 4)
    # bacteria_1 = data[bacteria_1row,:]
    # bacteria_2 = data[bacteria_2row,:]
    # bacteria_3 = data[bacteria_3row,:]
    # bacteria_4 = data[bacteria_4row,:]

    # Sort the temperature/growth rate, by x, y = zip(*sorted(zip(x,y))) documentation: https://docs.python.org/3.5/library/functions.html#zip
    # Bacteria 1
    # temp_x_1 = np.array([])
    # growth_y_1 = np.array([])
    # temp_x_1 = bacteria_1[:,0]
    # growth_y_1 = bacteria_1[:,1]
    # # temp_x_1 , growth_y_1 = np.argsort(temp_x_1,growth_y_1)
    # # growth_y_1 = np.argsort(growth_y_1)
    # temp_x_1 , growth_y_1 = zip(*sorted(zip(temp_x_1,growth_y_1)))

    # # Bacteria 2 
    # temp_x_2 = np.array([])
    # growth_y_2 = np.array([])
    # temp_x_2 = bacteria_2[:,0]
    # growth_y_2 = bacteria_2[:,1]
    # # temp_x_2 , growth_y_2 = np.argsort(temp_x_2,growth_y_2)
    # # growth_y_2 = np.argsort(growth_y_2)
    # temp_x_2 , growth_y_2 = zip(*sorted(zip(temp_x_2,growth_y_2)))

    # # Bacteria 3
    # temp_x_3 = np.array([])
    # growth_y_3 = np.array([])
    # temp_x_3 = bacteria_3[:,0]
    # growth_y_3 = bacteria_3[:,1]
    # # temp_x_3 , growth_y_3 = np.argsort(temp_x_3,growth_y_3)
    
    # # growth_y_3 = np.argsort(growth_y_3)
    # temp_x_3 , growth_y_3 = zip(*sorted(zip(temp_x_3, growth_y_3)))

    # # Bacteria 4
    # temp_x_4 = np.array([])
    # growth_y_4 = np.array([])
    # temp_x_4 = bacteria_4[:,0]
    # growth_y_4 = bacteria_4[:,1]
    # # temp_x_4 , growth_y_4 = np.argsort(temp_x_4,growth_y_4)
    # # growth_y_4 = np.argsort(growth_y_4)
    # temp_x_4 , growth_y_4 = zip(*sorted(zip(temp_x_4,growth_y_4)))

    # Four different plots 
    # plt.plot(temp_x_1,growth_y_1,label='Salmonella enterica',color='red',linewidth=3)
    # plt.plot(temp_x_2,growth_y_2,label='Bacillus cereus',color='green',linewidth=3)
    # plt.plot(temp_x_3,growth_y_3,label='Listeria',color='blue',linewidth=3)
    # plt.plot(temp_x_4,growth_y_4,label='Brochothrix thermosphacta',color='yellow',linewidth=3)

    ax2.set_title('Growth rate by temperature') # Title for the second subplot
    ax2.set_ylabel('Growth rate') # y-label for the second subplot 
    ax2.set_xlabel('Temperature') # x-label for the second subplot 

    # Setting the figure's height, width and legend
    fig.set_figheight(7) 
    fig.set_figwidth(14)
    fig.legend(bbox_to_anchor = (0.6,1)) #bbox_to_anchor is used to place a legend from x- and y-coordinates 
    plt.show()

    return fig 
# print(dataPlot(dataLoad('Data_files_for_projects/Bacteria/test.txt')))
