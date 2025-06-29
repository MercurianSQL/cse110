"""
Author: Marinda Keller
Purpose: Practice writing functions for complex math problems
"""

import math

def compute_area_circle(radius):
    area = math.pi * (radius ** 2)
    return area

def compute_area_square(side):
    area = side ** 2
    return area

def compute_area_rectangle(length, width):
    area = length * width
    return area

shape = ""
while shape != "quit":
    shape = input("What is your shape? ").lower()
    if shape == "circle":
        radius = float(input(f"What is the radius of the {shape}? "))
        c_area = compute_area_circle(radius)
        print(f"The area of your {shape} is: {c_area:0.2f}")
        
    elif shape == "square":
        side = float(input(f"What is the length of a side of the {shape}? "))
        squarea = compute_area_square(side)
        print(f"The area of your {shape} is: {squarea}")

    elif shape == "rectangle":
        length = float(input(f"What is the length of the {shape}? "))
        width= float(input(f"What is the width of the {shape}? "))
        r_area = compute_area_rectangle(length, width)
        print(f"The area of your {shape} is: {r_area}")

    elif shape == "quit":
        print("Thank you, Goodbye.")

    else:
        print("That shape is outside the parameters of this program.")
