# -*- coding: utf-8 -*-
"""
Created on Tue Aug 18 07:26:33 2026

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.array([*range(1,9)])
y=np.arange(55,95,5)
plt.scatter(x,y,color='red')    
plt.title('coorelation between study hours and exam scores')
plt.xlabel('study hour')
plt.ylabel('exam score')
plt.grid(True)