# Create a custom math module and import it in another file.

from numpy import number

import mymath


print("Addition =", mymath.add(5, 10))
print("Subtraction =", mymath.subtract(5, 10))
print("Multiplication =", mymath.multiply(5, 10))


# Create a module to perform string operations.

import string_module

text = input("Enter a string: ")

print("Uppercase:", string_module.uppercase(text))
print("Lowercase:", string_module.lowercase(text))
print("Reverse:", string_module.reverse(text))


# Use random module to generate 5 random integers.

import random

print("Five Random Numbers:")

for i in range(5):
    num = random.randint(1, 100)
    print(num)
 
# Use datetime module to display current date and time.

from datetime import datetime

current = datetime.now()

print("current Date and Time =", current)
print(current)

#  Use math module to find factorial of a number.

import math
num = int(input("Enter a number to find its factorial: "))
print("Factorial of num is:", math.factorial(num))

# Create a package shapes with modules for circle and rectangle.

from shapes import circle
from shapes import rectangle

r = float(input("Enter radius: "))
print("Area of Circle =", circle.area(r))

l = float(input("Enter length: "))
w = float(input("Enter width: "))
print("Area of Rectangle =", rectangle.area(l, w))


# Import multiple functions from one module and use them.
from calculator import add, subtract, multiply

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition =", add(a, b))
print("Subtraction =", subtract(a, b))
print("Multiplication =", multiply(a, b))


# Write a program to shuffle a list using random module.
import random

numbers = [10, 20, 30, 40, 50]

print("Original List:", numbers)

random.shuffle(numbers)

print("Shuffled List:", numbers)


# Write a program to calculate the difference between two dates.

from datetime import datetime

date1 = input("Enter first date (DD-MM-YYYY): ")
date2 = input("Enter second date (DD-MM-YYYY): ")

d1 = datetime.strptime(date1, "%d-%m-%Y")
d2 = datetime.strptime(date2, "%d-%m-%Y")

difference = d2 - d1

print("Difference in days =", difference.days)

# Use os module to list files in a directory.

import os

path = "."

files = os.listdir(path)

print("Files in directory:")

for file in files:
    print(file)