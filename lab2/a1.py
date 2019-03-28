from cs50 import get_int, get_float
from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D

print("-" * 20)
print("TASK 2\n")

X = get_float("Radius of first circe")
Y = get_float("Radius of second circe")
if X > 0:
    print("First circe:\n", "Perimeter: ", round(2 * pi * X, 2), "\nField: ", round(pi * X ** 2, 2))
else:
    print("Nie moze byc ujemne 1 okreg")
if Y > 0:
    print("Second circe:\n", "Perimeter: ", round(2 * pi * Y, 2), "\nField: ", round(pi * Y ** 2, 2))
else:
    print("Nie moze byc ujemne 2 okreg")
print("-" * 20)


