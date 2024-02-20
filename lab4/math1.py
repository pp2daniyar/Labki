# Exercise 1
import math
deg = float(input("Input degree: "))
rad = math.radians(deg)
print(rad)

# Exercise 2
h = float(input("Height: "))
a = float(input("Base, first value: "))
b = float(input("Base, second value: "))
area = (((a + b) / 2) * h)
print(area)

# Exercise 3
from math import tan, pi
n = int(input("Input number of sides: "))
l = float(input("Input the length of a side: "))
A = n * (l ** 2) / (4 * tan(pi / n))
print("The area of the polygon is: ", A)

# Exercise 4
x = float(input('Length of base: '))
h = float(input('Measurement of height: '))
A = x * h
print("Area is: ", A)