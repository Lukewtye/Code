'''
Name: Luke Tye
Date: 9/7/23
Description:
This is my Unit 1 Coding Final Project. These are the objectives:

Write a program named geometry_fun.py which prompts a user for a positive whole number and outputs the following:

The perimeter and area of a square whose side length is the entered number
The radius, circumference, and area of a circle whose diameter is the entered number
The perimeter and area of an equilateral triangle whose side length is equal to the entered number.
The program will use the command line for its input and output (I/O). 
'''
import math

PI = 3.1416
positive_number = (int(input("Give a whole, positive number: ")))
positive_radius = int(positive_number / 2)
square_peri = (positive_number * 4)
square_area = (positive_number * 2)
circle_radius = (positive_number / 2)
circle_circumference = (positive_number * PI)
circle_area = PI * math.pow (positive_radius)
#WHY IS THIS AN ERROR
#CHECK THIS AT HOME WITH PYTHON 3.11 TO MAKE SURE IT WORKS
eq_triangle_perimeter = (positive_number * 3)
eq_triangle_height = (1/2(sqrt (3 * positive_number)))

