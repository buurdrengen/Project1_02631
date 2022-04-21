# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 09:18:44 2022

@author: cglitz
"""

import numpy as np
# imports matrix with filtered bacteria data 
from dataLoad import dataLoad

#makes sure that valid number is chosen, if not, returns 
from input_number import inputNumber
from displayMenu import displayMenu
from statistics_2 import dataStatistics
from sortBacteria import filterBacteria
from filterGrowthrate import filterGrowthrate
from dataPlot import dataPlot
from inputFilename import inputFilename

filter_bacteria = str()
filter_growth_rate = str()

# Define menu items
menuItems = np.array(["Load data", "Filter data", "Display statistics", "Generate plots", "Quit"])

# Start
while True:
    # Display menu options and ask user to choose a menu item
    choice = displayMenu(menuItems)
    # Menu item chosen
    # ------------------------------------------------------------------
    # 1. Load data
    if choice == 1:
    # Ask user to input file name
        # function file input 
        filename = inputFilename()
        data = dataLoad(filename)

    # ------------------------------------------------------------------
    # 2. Filter data
    elif choice == 2:
        # verifies that data has been loaded before 
        try:
            data
        except:
            print("You need to load a dataset first\n")
            continue
    # display filter options
        filter_menuItems = np.array(["Bacteria type", "Growth rate","Reset all filters", "Quit filter"])
        # Display menu options for filtering and ask user to choose a menu item
        print(filter_bacteria)
        print(filter_growth_rate)
        choice_filter = displayMenu(filter_menuItems)
        # Menu item chosen
        # filters data for bacteria type
        if choice_filter == 1:
            bacteriatypes_menuItems = np.array(["Salmonella interica", "Bacillus cereus","Listeria", "Brochotrix thermosphacta"])
            # display options for bacteria to filter
            choice_bacteriafilter = displayMenu(bacteriatypes_menuItems)
            # returns filtered data set depending on which bacteria type was chosen 
            if choice_bacteriafilter == 1:
                data = filterBacteria(data, 1)
                
            elif choice_bacteriafilter == 2:
                data = filterBacteria(data, 2)
                # filter = f"Filtered for {bacteriatypes_menuItems[int(choice_bacteriafilter-1)]}"

            elif choice_bacteriafilter == 3:
                data = filterBacteria(data, 3)

            elif choice_bacteriafilter == 4:
                data = filterBacteria(data, 4)
            
            filter_bacteria = f"Filtered for {bacteriatypes_menuItems[int(choice_bacteriafilter-1)]}"
            #calls function to filter data for growth rate and returns that data
        elif choice_filter == 2:
            data = filterGrowthrate(data)
            filter = "Filtered for growth rate." 
        elif choice_filter == 3:
            print('You chosen to reload the original data, check for sample errors again:')
            print("")
            data = dataLoad(filename)
            filter_growth_rate = str()
            filter_bacteria = str()
        elif choice_filter == 4:
            continue
    # ------------------------------------------------------------------
    # 3. Display statistics
    elif choice == 3:
        try:
            data
        except:
            print('You need to load a dataset first')
            continue
        # display statistics options and shows applied filter (if a filter is active) 
        statistics_menuItems = np.array(["Mean temperature", "Mean growth rate","Std temperature", "Std growth rate", "Rows", "Mean cold growth rate", "Mean hot growth rate", "Quit statistics"])
        print("")
        print(filter_bacteria, filter_growth_rate, sep = "\n")
        print("")

        # Display menu options for statistics and ask user to choose a menu item
        while True:
            choice_statistics = displayMenu(statistics_menuItems)
            if choice_statistics == 8:
                break
        #compute statistics via dataStatistics function 
        # test = dataStatistics(data, statistics_menuItems[choice_statistics-1])
        # print(test)
            if choice_statistics == 1:
                dataStatistics(data,"mean temperature")
                print('Mean temperature = {:.2f} °C'.format(dataStatistics(data, 'mean temperature')),"\n")
                continue
            elif choice_statistics == 2:
                dataStatistics(data, "mean growth rate")
                print('Mean growth rate = {:.2f}'.format(dataStatistics(data, 'mean growth rate')),"\n")
                continue
            elif choice_statistics ==3:
                dataStatistics(data, "std temperature")
                print('Standard temperature = {:.2f}'.format(dataStatistics(data, 'std temperature')),"\n")
                continue
            elif choice_statistics == 4:
                dataStatistics(data, "std growth rate")
                print('Standard growth rate = {:.2f}'.format(dataStatistics(data, 'std growth rate')),"\n")
                continue
            elif choice_statistics == 5:
                dataStatistics(data, "rows")
                print('Rows = {:.2f}'.format(dataStatistics(data, 'rows')),"\n")
                continue
            elif choice_statistics == 6:
                dataStatistics(data, "mean cold growth rate")
                print('Mean cold growth rate = {:.2f}'.format(dataStatistics(data, 'mean cold growth rate')),"\n")
                continue
            elif choice_statistics == 7:
                dataStatistics(data, "mean hot growth rate")
                print('Mean hot growth rate = {:.2f}'.format(dataStatistics(data, 'mean hot growth rate')),"\n")
                continue
                           
    # ------------------------------------------------------------------
    # 4. Display plots 
    elif choice == 4: 
        # Check if the data is loaded.
        try:
            data 
        except: 
            print("You need to load a dataset first")
            continue
        print("")
        print(filter_bacteria, filter_growth_rate, sep = "\n")
        print("")
        # Plot the data 
        dataPlot(data)
    # 5. Quit
    elif choice == 5:
        break
    # End
    