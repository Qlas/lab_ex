from cs50 import get_int, get_float
from numpy import *
from matplotlib.pyplot import *
from mpl_toolkits.mplot3d import Axes3D
from random import *
for i in range(100):
    x = randint(-19,20)
    y = randint(-20,20)
    try:
        if x%2 == 0 and y%2 == 0 and x%y == 0:
            print(x,y)
            break
    except ZeroDivisionError:
        print("Nie dziel przez 0")
