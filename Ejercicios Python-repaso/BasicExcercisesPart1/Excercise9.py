# Write a Python program to get the volume of a sphere.
import math
radius = float(input("Radius: "))
volume = (4/3) * math.pi * radius**3
print("%.2f" % volume)