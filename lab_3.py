#1 Write a function countField which calculates the field of a given figure. It takes the following input parameters:
# - type: circle/rectangle/triangle/rhombus
# - x & optional y.
# For circle we get only x which stands for radius. For Rectangle x&y are the figure's sides, for triangle they are
# accordingly the base and the height and for rhombus - diagonals (4p)
#2 Write a function which takes sets of parameters of two figures and compares their fields. (4p)
# The exemplary input is [[Circle, 4], [Rhombus, 2, 4]]
# Expected output would be 'The first figure (Circle) has larger field'
#3 Test your solutions
from cs50 import get_float
from numpy import pi


def countField(figure):
    y = 0
    if figure == 'circle':
        x = get_float("First number")
    else:
        x = get_float("First number")
        y = get_float("Second number")
    if figure == 'circle':
        z = round(2 * pi * x, 2)
        print("Field of circle: ", z)
    elif figure == 'rectangle':
        z = round(x * y, 2)
        print("Field of rectangle: ", z)
    elif figure == 'triangle':
        z = round(1/2 * x * y, 2)
        print("Field of rectangle: ", z)
    else:
        z = round(1 / 2 * x * y, 2)
        print("Field of rhombus: ", z)
    return z

def compare():
    x = []
    for i in range(2):
        figure = 'a'
        while figure != 'circle' and figure != 'rectangle' and figure != 'triangle' and figure != 'rhombus':
            figure = str(input("Write: circle/rectangle/triangle/rhombus\n"))
            if figure != 'circle' and figure != 'rectangle' and figure != 'triangle' and figure != 'rhombus':
                print("You must write exacle this figure")
        x.append([countField(figure),figure])
    if x[0][0] == x[1][0]:
        print("Both figure has a same field")
    elif x.index(max(x)) == 0:
        print("The first figure", max(x)[1], "has larger field")
    else:
        print("The second figure", max(x)[1], "has larger field")


figure = 'a'
while figure != 'circle' and figure != 'rectangle' and figure != 'triangle' and figure != 'rhombus':
    figure = str(input("Write: circle/rectangle/triangle/rhombus\n"))
    if figure != 'circle' and figure != 'rectangle' and figure != 'triangle' and figure != 'rhombus':
        print("You must write exacle this figure")
countField(figure)

compare()
