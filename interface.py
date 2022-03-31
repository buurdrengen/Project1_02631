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
menuItems = np.array(["Load data", "Filter data", "Display settings", "Generate plots", "Quit"])
# Start
while True:
    # Display menu options and ask user to choose a menu item
    choice = displayMenu(menuItems)
    # Menu item chosen
    # ------------------------------------------------------------------
    # 1. Enter name
    if choice == 1:
    # Ask user to input file name 
        filename = input("Please enter the name of the file you want to load: ")
        dataLoad(filename)
    # ------------------------------------------------------------------
    # 2. Display greeting
    elif choice == 2:
    # Is name empty?
        if name == "":
    # Display error message
            print("Error: Name is empty")
        else:
    # Display greeting
            print("Hello {:s}".format(name))
    # ------------------------------------------------------------------
    # 3. Quit
    elif choice == 3:
    # End
    break


# Menu options
   # 1. Load data.
   # 2. Filter data.
   # 3. Display statistics.
   # 4. Generate plots
   # 5. Quit

