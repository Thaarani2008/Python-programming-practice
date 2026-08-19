# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 07:39:00 2026

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.array([*range(1,9)])
y=np.arange(90000,50000,-5000)
plt.scatter(x,y,color='red')    
plt.title('coorelation between car age vs resale value')
plt.xlabel('car age')
plt.ylabel('resale value')
plt.grid(True)