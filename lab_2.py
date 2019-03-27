# TASKS (8p)- calculate & print:
#0 Use alternative way of reading inputs - using library (0.5p)
#1 Perimeter & field of circles with given radius X for the first circle & Y for the second one. (1p)
#2 Find X & Y that satisfy: X is divisible by Y and both X & Y are even. (0.5p)
#3 Check if X is divisible by Y (do it in one line of code), print 'X is divisible by Y' or 'X is not divisible by Y'. (1p)
#Ad 3 Hint- use the "ternary operator" as we did calculating xIsEvenLog above.
#4 Add rounding for the above x/y operation. Round to 2 decimal points. Hint: look up in Google "python limiting number of decimals". (1p)
#5 Look at lab2-plot.py and create your own script which takes a number as an input and plots the same 3D wave but with different characteristics
# it's totally up to your imagination how do you want to amend the figure according to the input number (1p)
#6 Test your code. Check various edge cases. In other words: does your program (1, 3, 4 & 5)work for all input values?
# In case of task 4  do not forget to round to different amount of decimals and see if it still works.(3p)

from cs50 import get_int
from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D

print("TASK 1\n")

x = input("normal")
y = get_int("get")

print(x, type(x))
print(y, type(y))

print("-"*20)
print("TASK 2\n")

X = abs(get_int("Radius of first circe"))
Y = abs(get_int("Radius of second circe"))
print("First circe:\n", "Perimeter: ", round(2 * pi * X,2), "\nField: ", round(pi * X**2,2))
print("Second circe:\n", "Perimeter: ", round(2 * pi * Y,2), "\nField: ", round(pi * Y**2,2))

print("-"*20)
print("TASK 3\n")

print("X is divisible by Y") if (X%Y == 0) else print("X is not divisible by Y")

print("-"*20)
print("TASK 5\n")


x = get_int("Give us a number")
x_knots = linspace(-3*pi,3*pi,201)
y_knots = linspace(-3*pi,3*pi,201)
X, Y = meshgrid(x_knots, y_knots*x)
R = sqrt(X**2+Y**2)
Z = cos(R)**2*np.exp(-0.1*R)
ax = Axes3D(figure(figsize=(8,5)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0.4)
show()