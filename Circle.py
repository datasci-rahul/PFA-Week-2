# -*- coding: utf-8 -*-
"""
Created on Sat Sep 10 14:59:14 2022

@author: Rahul Sharma M.Tech(Data Science)
"""
'''Objective:
Create a Python class named Circle constructed by a radius and two methods 
which will compute the area and the perimeter of a circle'''


from math import pi
# Creating Class named Circle()

class Circle():
    def __init__(self):
        self.r = float(input("Enter radius of circle :"))
        
# defining first method area of a circle

    def area(self):
        print("The Area Of Circle is:", pi*self.r*self.r)
        
# defining second method perimeter of a circle    
    def perimeter(self):
        print("The Perimeter of circle is :",  2*pi*self.r)

C = Circle()
C.area()
C.perimeter()



