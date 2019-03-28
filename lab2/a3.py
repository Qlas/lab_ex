from cs50 import get_int, get_float
from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D

print("TASK 3\n")
X = get_float("First number")
Y = get_float("First number")
print("X is divisible by Y") if (X%Y == 0) else print("X is not divisible by Y")

