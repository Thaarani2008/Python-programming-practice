# -*- coding: utf-8 -*-
"""
Created on Thu Aug  6 11:35:04 2026


@author: Admin
"""

a=int((input("enter 1 for addition \n 2 for subration \n 3 for multipicatin  \n 4 for division " )))
if a==1:
   x=float(input("enter the first number"))
   y=float(input("enter the second number"))
   print("{x}+{y}=",x+y)
elif a==2:
    x=float(input("enter the first number"))
    y=float(input("enter the second number"))
    print("{x}-{y}=",x-y)
elif a==3:
    x=float(input("enter the first number"))
    y=float(input("enter the second number"))
    print("{x}+*{y}=",x*y)
elif a==4:
    x=float(input("enter the first number"))
    y=float(input("enter the second number"))
    print("{x}/{y}=",x/y)