#TASKS (4p)
#1 calculate & print the value of function y = 2x^2 + 2x + 2 for x=[56, 57, ... 100] (0.5p)
#2 ask the user for a number and print its factorial (1p)
#3 write a function which takes an array of numbers as an input and finds the lowest value. Return the index of that element and its value (1p)
#4 looking at lab1-input and lab1-plot files create your own python script that takes a number and returns any chart of a given length.
#the length of a chart is the input to your script. The output is a plot (it doesn't matter if it's a y=x or y=e^x+2x or y=|x| function, use your imagination)
#test your solution properly. Look how it behaves given different input values. (1p)
#5 upload the solution as a Github repository. I suggest creating a directory for the whole python course and subdirectories lab1, lab2 etc. (0.5p)
#Ad 5 Hint write in Google "how to create a github repo". There are plenty of tutorials explaining this matter.

from numpy import *
from matplotlib.pyplot import *

def quadratic ():
    for x in range(56,101):
        y = 2 * x ** 2 + 2 * x + 2
        print(x, ": ", y)

def factorial(x):
    y = 1
    for i in range(1,x+1):
        y *= i
    print("Factorial: ", y)

def lowest():
    list = []
    while (True):
        x = input("Write a number or leave empty to stop\n")
        if x == "" and len(list) != 0:
            break
        try:
         list.append(int(x))
        except ValueError:
            print("Value Error. Write a number")
            continue
    low = list[0]
    for i in range(len(list)):
        if low > list[i]:
            low = list[i]
    print("Index: ")
    for i in range(len(list)):
        if list[i] == low:
            print(i)
    return low

print("TASK 1\n")

quadratic()

print("-"*20)
print("TASK 2\n")

while True:
    try:
        x = int(input("Write a number >=0\n"))
        if x >= 0:
            break
        else:
            print("Number should be greater than 0")
    except ValueError:
        print("Value error, write a number")
        continue

factorial(x)

print("-"*20)
print("TASK 3\n")

print("Number:", lowest())

print("-"*20)
print("TASK 4\n")

while True:
    try:
        lenght = int(input("Lenght: "))
        break
    except ValueError:
        print("Value Error, write a number")
        continue

num_points = lenght
x_values = []
y_values = []
for i in range(abs(lenght)*10):
    x_values.append(i/10-20)
    y_values.append(sin(x_values[i]) * x_values[i])

point_numbers = range(num_points)
plot(x_values, y_values)
show()
