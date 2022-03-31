## Remove bacteria function ## 
#
# 
# Author: Aksel Buur Christensen, s203947
#
# 
##
from dataLoad import * 
def filterBacteria(data,type):
    # This function removes one of the four bacteria types 
    # Input: Data from the bacterias and a type, where: 
    # 1 = 'Salmonella enterica'
    # 2 = 'Bacillus cereus'
    # 3 = 'Listeria'
    # 4 = 'Brochothrix thermosphacta'

    # Make an bacteria-array: 

    bacteria = data[:,2]

    # Remove all but the chosen type bacteria: 
    chosenRow = (bacteria == type) 

    # The filtered data without the chosen row becomes:
    datafiltered = data[chosenRow,:]
    print(datafiltered[:,0])
    return datafiltered
print(filterBacteria(dataLoad('Data_files_for_projects/Bacteria/test.txt'),2))
