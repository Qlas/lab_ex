from cs50 import get_int, get_float
from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D

print("-"*20)
print("TASK 5\n")


x = get_int("Give us a number")
x_knots = linspace(-3*pi,3*pi,201)
y_knots = linspace(-3*pi,3*pi,201)
X, Y = meshgrid(x_knots, y_knots)
R = sqrt(X**(2*x)+Y**2)
Z = cos(R)**2*np.exp(-0.1*R*x)
ax = Axes3D(figure(figsize=(8,5)))
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0.4)
show()