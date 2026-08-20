# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 10:53:47 2026

@author: Admin
"""

import numpy as np
import matplotlib.pyplot as plt
x=np.array([*range(1,9)])
y=np.arange(90000,50000,-5000)

n=len(x)
xy=np.multiply(x,y)
print(xy)
sum_xy =  np.sum(xy)
print(sum_xy)
sumx=np.sum(x)
sumy=np.sum(y)
sumxxsumy=sumx*sumy
x_square=np.square(x)
y_square=np.square(y)
r=((n*sum_xy)-(sumx)*(sumy))/np.sqrt((n*np.sum(x_square)-(np.square(sumx)))*(n*np.sum(y_square)-(np.square(sumy))))
print(r)