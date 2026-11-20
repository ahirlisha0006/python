#1
import mymath
print("addtion:",mymath.add(10,5))
print("subtration:",mymath.subtract(20,5))
print("multiplation:",mymath.multiply(5,3))

#2
import string
text=input("enter an string:")
print("uppercase:",string.uppercase(text))
print("lowercase:",string.lowercase(text))
print("reverse:",string.reverse(text))
#3
import random

for i in range(5):
    num = random.randint(1, 100)
    print(num)

#4
import datetime    
now= datetime.datetime.now()
print("current date and time:",now)
#5
import math

num = int(input("Enter a number: "))

result = math.factorial(num)

print("Factorial =", result)
#6
import shapes
from shapes.circle import area as circle_area
from shapes.rectangle import area as rectangle_area

print("Area of circle:", circle_area(5))
print("Area of rectangle:", rectangle_area(10, 5))
#7
from math import sqrt, pow, factorial

print("Square root:", sqrt(25))

print("Power:", pow(2, 3))

print("Factorial:", factorial(5))
#8
import random

numbers = [10, 20, 30, 40, 50]

random.shuffle(numbers)

print("Shuffled list:", numbers)
#9
from datetime import date

date1 = date(2026, 11, 18)
date2 = date(2026, 11, 25)

difference = date2 - date1

print("Difference between dates:", difference.days, "days")
#10
import os

files = os.listdir(".")

print("Files in current directory:")

for file in files:
    print(file)