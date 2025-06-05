"""
Author: Maridna Keller
Purpose: Practice writing complex math problems
"""

import math

# area of square
s_length = float(input("What is the length in centimeters of a side of the square? "))
squarea = s_length ** 2
print (f"The area of the square is: {squarea:.2f} cm\u00b2")
m_squarea = squarea * 0.0001
print (f"The area of the square is: {m_squarea:.2f} m\u00b2")
print()

# area of rectangle
r_length = float(input("What is the length in meters of the rectangle? "))
r_width = float(input("What is the width in meters of the rectangle? "))
r_area = r_length * r_width
print (f"The area of the rectangle is: {r_area:.1f} cm\u00b2")
mr_area = r_area * 0.0001
print (f"The area of the rectangle is: {mr_area:.1f} m\u00b2")
print()

# area of circle
c_radius= float(input("What is the radius of the circle in meters? "))
c_area = math.pi * (c_radius ** 2)
print (f"The area of the circle is: {c_area:.4f} cm\u00b2")
mc_area = c_area * 0.0001
print (f"The area of the circle is: {mc_area:.4f} m\u00b2")

"""quiz check
area = 5
print(f"The area of the square is: {area / 10000} m^2")
print(f"The area of the square is: {area} / 10000 m^2")

length = int(input("What is the length of rectangle? "))
print(length)"""
