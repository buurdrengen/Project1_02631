# Data-plot function 
# 
# Author: Aksel Buur Christensen, s203947 
# 
import numpy as np 
import matplotlib.pyplot as plt 
from dataLoad import * 
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

    x_bacteria = ['1','2','3','4']

    fig, (ax1, ax2) = plt.subplots(1,2) # Create a figure with subplots, here ax1 is the first plot and ax2 is the second plot.
    width = 0.5 # The width of the bars
    ind = np.arange(4) # The x locations for the groups. 
    # br2 = [x + width for x in br1]
    # br3 = [x + width for x in br2]

    y_bacteria = np.array([y1,y2,y3,y4]) # Create an array with the different types of bacteria. 

    # ax.bar(ind,y_bacteria[0],width,label='Salmonella enterica',color='red')
    # ax.bar(ind,y_bacteria[1],width,label='Bacillus cereus',color='green')
    # ax.bar(ind,y_bacteria[2],width,label='Listeria',color='blue')
    # ax.bar(ind,y_bacteria[3],width,label='Brochothrix thermosphacta',color='yellow')

    ax1.set_title('Number of bacterias')
    ax1.set_ylabel('Number')
    ax1.legend()
    # ax.set_xticks(ind,labels=['1','2','3','4'])
    # ax.bar_label(p1,label_type='center')
    # ax.bar_label(p2,label_type='center')
    # ax.bar_label(p3,label_type='center')
    # ax.bar_label(p4,label_type='center')
    ax1.bar(x_bacteria,y_bacteria,color=['red','green','blue','yellow'])

    # 2) Plot "Growth Rate by Temperature"
    plt.xlim([10,60]) # Limits for the x-axis. 
    # temp_x = data[:,0] # Taking the temperature column for making it the x-axis. 
    bacteria_1row = ( bacteria == 1) 
    bacteria_2row = ( bacteria == 2)
    bacteria_3row = ( bacteria == 3)
    bacteria_4row = ( bacteria == 4)
    bacteria_1 = data[bacteria_1row,:]
    # temp_x_1 = data[bacteria_1row,0]
    bacteria_2 = data[bacteria_2row,:]
    # temp_x_2 = data[bacteria_2row,0]
    bacteria_3 = data[bacteria_3row,:]
    # temp_x_3 = data[bacteria_3row,0]
    bacteria_4 = data[bacteria_4row,:]
    # temp_x_4 = data[bacteria_4row,0]
    # Sort the 
    plt.plot(bacteria_1[:,0],bacteria_1[:,1],label='Salmonella enterica',color='red')
    plt.plot(bacteria_2[:,0],bacteria_2[:,1],label='Bacillus cereus',color='green')
    plt.plot(bacteria_3[:,0],bacteria_3[:,1],label='Listeria',color='blue')
    plt.plot(bacteria_4[:,0],bacteria_4[:,1],label='Brochothrix thermosphacta',color='yellow')
    ax2.legend()
    plt.show()
    print(bacteria_1)
    # print(y_bacteria)
    return fig 
print(dataPlot(dataLoad('Data_files_for_projects/Bacteria/test.txt')))

# Plotting guide used: https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html