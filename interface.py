# -*- coding: utf-8 -*-
"""
Created on Thu Mar 31 09:18:44 2022

@author: cglitz
"""

import numpy as np
from dataLoad import dataLoad

data_file = dataLoad('Data_files_for_projects/Bacteria/test.txt')
print(data_file)
# Menu options
   # 1. Load data.
   # 2. Filter data.
   # 3. Display statistics.
   # 4. Generate plots
   # 5. Quit
menuItems = np.array(["1. Load data", "2. Filter data", "3. Display settings", "4. Generate plots", "5. Quit"])

