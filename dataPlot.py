# Data-plot function 
# 
# Author: Aksel Buur Christensen, s023947 
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

    # Collecting them into an array for plotting. 
    fig,ax = plt.subplots() 
    ind = np.arange(4) # The x locations for the groups. 
    width = 0.5 # The width of the bars
    y_bacteria = np.array([y1,y2,y3,y4])
    p1 = ax.bar(ind,y_bacteria[0],width,label='Salmonella enterica',color='red')
    p2 = ax.bar(ind,y_bacteria[1],width,label='Bacillus cereus',color='green')
    p3 = ax.bar(ind,y_bacteria[2],width,label='Listeria',color='blue')
    p4 = ax.bar(ind,y_bacteria[3],width,label='Brochothrix thermosphacta',color='yellow')
    ax.set_title('Number of bacterias')
    ax.set_ylabel('Number')
    ax.legend()
    ax.set_xticks(ind,labels=['1','2','3','4'])
    ax.bar_label(p1,label_type='center')
    ax.bar_label(p2,label_type='center')
    ax.bar_label(p3,label_type='center')
    ax.bar_label(p4,label_type='center')
    # ax.bar(x_bacteria,y_bacteria)
    plt.show()

    # print(y_bacteria)
    return fig 
print(dataPlot(dataLoad('Data_files_for_projects/Bacteria/test.txt')))

# Plotting guide used: https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_label_demo.html