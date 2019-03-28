from cs50 import get_int, get_float
from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D

X = get_float("First number")
Y = get_float("First number")

if Y == 0:
    print("Nie dziel przez 0")
else:
    if X == -0 or X == 0:
        s = 0
    else:
        s= X/Y
    print(round(s,2))
    print('%.2f' % s)


