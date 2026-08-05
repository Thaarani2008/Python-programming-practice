# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 19:25:12 2026

@author: Admin
"""

books=input()
pages=books.split()
for i in pages:
    if(int(i)>300):
        print(i,end=" ")