# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 15:43:43 2022

@author: Rahul Sharma M.Tech(Data Science)
"""

"""Objective:
Create a Python class named Rectangle constructed by a length and width 
and a method which will compute the area of a rectangle. """


"""Creating a Python class named Rectangle"""

class Rectangle():
    def __init__(self):
        self.l= float(input("Enter the length of rectangle:"))
        self.b=float(input("Enter the width of rectangle:"))
    def area(self):
        print("The Area Of Circle is:", self.l*self.b)
R=Rectangle()
R.area()