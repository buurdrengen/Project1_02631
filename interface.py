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
        filename = input("Please enter the name of the file you want to load: ")
        dataLoad(filename)
    # ------------------------------------------------------------------
    # 2. Filter data
    elif choice == 2:
    # display filter options
        filter_menuItems = np.array(["Bacteria type", "Growth rate","Quit"])
        while True:
            choice_filter = displayMenu(filter_menuItems)
        # Menu item chosen
            if choice_filter ==1:
                #calls function to filter data for bacteria type 
            if choice_filter ==2:
                #calls function that filters data for growth rate
            if chocie_filter ==3:
                break
    # ------------------------------------------------------------------
    # 3. Display statistics
    elif choice == 3:
        statistics_menuItems = np.array(["mean temperature", "mean growth rate","std temperature", "std growth rate", "rows", "mean cold growth rate", "mean hot growth rate"])
        while True:
            choice_statistics = displayMenu(statistics_menuItems)
            #compute statistics via dataStatistics function 
        
    
    # ------------------------------------------------------------------

    # 3. Quit
    elif choice == 3:
    # End
    break

