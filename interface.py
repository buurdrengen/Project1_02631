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
from statistics import *
from sortBacteria import filterBacteria
from filterGrowthrate import filterGrowthrate

# Define menu items
menuItems = np.array(["Load data", "Filter data", "Display statistics", "Generate plots", "Quit"])
# display filter options
# filter_menuItems = np.array(["Bacteria type", "Growth rate","Quit"])
# Bacteria types menu
# bacteriatypes_menuItems = np.array(["Salmonella interica", "Bacillus cereus","Listeria", "Brochotrix thermosphacta"])
# Statistics menu 
# statistics_menuItems = np.array(["mean temperature", "mean growth rate","std temperature", "std growth rate", "rows", "mean cold growth rate", "mean hot growth rate", "Quit"])

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
            print("load a dataset first")
    # display filter options
        filter_menuItems = np.array(["Bacteria type", "Growth rate","Quit"])
        while True:
            # Display menu options for filtering and ask user to choose a menu item
            choice_filter = displayMenu(filter_menuItems)
        # Menu item chosen
            # filters data for bacteria type
            if choice_filter ==1:
                bacteriatypes_menuItems = np.array(["Salmonella interica", "Bacillus cereus","Listeria", "Brochotrix thermosphacta"])
                while True:
                    # display options for bacteria to filter
                    choice_bacteriafilter = displayMenu(bacteriatypes_menuItems)
                    # returns filtered data set depending on which bacteria type was chosen 
                if choice_bacteriafilter == 1:
                    data = filterBacteria(data, 1)
                elif choice_bacteriafilter == 2:
                    data = filterBacteria(data, 2)
                elif choice_bacteriafilter == 3:
                    data = filterBacteria(data, 3)
                elif choice_bacteriafilter == 4:
                    data = filterBacteria(data, 4)            
                #calls function to filter data for growth rate and returns that data
            elif choice_filter ==2:
                filter_growthrate_data = filterGrowthrate(data)
            elif choice_filter ==3:
                break
    # ------------------------------------------------------------------
    # 3. Display statistics
    elif choice == 3:
        
        # display statistics options 
        statistics_menuItems = np.array(["mean temperature", "mean growth rate","std temperature", "std growth rate", "rows", "mean cold growth rate", "mean hot growth rate", "Quit"])
        # Start 
        while True:
            # Display menu options for statistics and ask user to choose a menu item
            choice_statistics = displayMenu(statistics_menuItems)
            #compute statistics via dataStatistics function 
            if choice_statistics == 1:
                dataStatistics(data,"mean temperature")
            elif choice_statistics == 2:
                dataStatistics(data, "mean growth rate")
            elif choice_statistics == 8:
                break
            
            
            
                
    
    # ------------------------------------------------------------------

    # 3. Quit
    elif choice == 3:
    # End
    break

        