# Data-plot function 
# 
# Author: Aksel Buur Christensen, s203947 
# 
import numpy as np 
import matplotlib.pyplot as plt 
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
    
    # Create an array of bacteria names for the x-axis on the plot. 
    bacnames = ['Salmonella\nenterica','Bacillus cereus','Listeria','Brochothrix\nthermosphacta'] 

    fig, (ax1, ax2) = plt.subplots(1,2) # Create a figure with subplots, here ax1 is the first plot and ax2 is the second plot.

    ax1.set_title('Number of bacterias') # Title for the first subplot
    ax1.set_ylabel('Number of samples') # y-label for the first subplot
    ax1.set_xlabel('Bacteria type') # x-label for the first subplot
    ax1.bar(bacnames,[y1, y2, y3, y4]) # Plotting the histogram in the first subplot

    # 2) Plot "Growth Rate by Temperature"
    plt.xlim([10,60]) # Limits for the x-axis. 

    # Sorting for the temperature by np.argsort.  
    temp = data[np.argsort(data[:,0])]

    # Plot each bacteria type present with points and graphs
    # The for loop tries from 0-3 with the temperature as x (first plot argument) and growth rate as y (second plot argument).
    # np.where documentation: https://numpy.org/doc/stable/reference/generated/numpy.where.html
    for i in range(4):
        ax2.plot(temp[np.where(temp[:,2] == i+1)][:,0], temp[np.where(temp[:,2] == i+1)][:,1],marker = 'o',label =str(bacnames[i]))

    ax2.set_title('Growth rate by temperature') # Title for the second subplot
    ax2.set_ylabel('Growth rate') # y-label for the second subplot 
    ax2.set_xlabel('Temperature') # x-label for the second subplot 

    # Setting the figure's height, width and legend
    fig.set_figheight(7) 
    fig.set_figwidth(14)
    fig.legend(bbox_to_anchor = (0.6,1)) #bbox_to_anchor is used to place a legend from x- and y-coordinates 
    plt.show()

    return fig 
