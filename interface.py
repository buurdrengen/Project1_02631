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
from statistics import dataStatistics
from sortBacteria import filterBacteria
from filterGrowthrate import filterGrowthrate
from dataPlot import dataPlot


# Define menu items
menuItems = np.array(["Load data", "Filter data", "Display statistics", "Generate plots", "Quit"])
# display filter options
# filter_menuItems = np.array(["Bacteria type", "Growth rate","Quit"])
# Bacteria types menu
# bacteriatypes_menuItems = np.array(["Salmonella interica", "Bacillus cereus","Listeria", "Brochotrix thermosphacta"])
# Statistics menu 
# statistics_menuItems = np.array(["mean temperature", "mean growth rate","std temperature", "std growth rate", "rows", "mean cold growth rate", "mean hot growth rate", "Quit"])
filter = str()
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
        filename = input("Please enter the name of the file you want to load: ")
        data = dataLoad(filename)
    # ------------------------------------------------------------------
    # 2. Filter data
    elif choice == 2:
        # verifies that data has been loaded before 
        try:
            data
        except:
            print("You need to load a dataset first")
            continue
    # display filter options
        filter_menuItems = np.array(["Bacteria type", "Growth rate","Reset all filters", "Quit"])
        # Display menu options for filtering and ask user to choose a menu item
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
                #filter = f"Filtered for {bacteriatypes_menuItems[choice_bacteriafilter-1]}"
                # filter = f"Filtered for {bacteriatypes_menuItems[int(choice_bacteriafilter-1)]}"
                
            elif choice_bacteriafilter == 2:
                data = filterBacteria(data, 2)
                # filter = f"Filtered for {bacteriatypes_menuItems[int(choice_bacteriafilter-1)]}"

            elif choice_bacteriafilter == 3:
                data = filterBacteria(data, 3)

            elif choice_bacteriafilter == 4:
                data = filterBacteria(data, 4)
            
            filter = f"Filtered for {bacteriatypes_menuItems[int(choice_bacteriafilter-1)]}"
            #calls function to filter data for growth rate and returns that data
        elif choice_filter == 2:
            data = filterGrowthrate(data)
            filter = "Filtered for growth rate."
        elif choice_filter == 3: 
            data = dataLoad(filename)
            filter = str()
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
        # display statistics options 
        statistics_menuItems = np.array(["Mean temperature", "Mean growth rate","Std temperature", "Std growth rate", "Rows", "Mean cold growth rate", "Mean hot growth rate", "Quit"])
        print(filter)

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
                print('Mean temperature = {:.2f} °C'.format(dataStatistics(data, 'mean temperature')))
                continue
            elif choice_statistics == 2:
                dataStatistics(data, "mean growth rate")
                print('Mean growth rate = {:.2f}'.format(dataStatistics(data, 'mean growth rate')))
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
        # Plot the data 
        dataPlot(data)
    # 5. Quit
    elif choice == 5:
        break
    # End

    