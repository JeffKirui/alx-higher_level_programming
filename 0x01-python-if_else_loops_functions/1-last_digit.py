#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numb = number % 10
temp = number
if temp < 0:
    temp *= -1
    numb = -(temp % 10)
if numb > 5:
    print(f"Last digit of {number} is {numb} and is greater than 5")
elif numb == 0:
    print(f"Last digit of {number} is {numb} and is 0")
else:
    print(f"Last digit of {number} is {numb} and is less than 6 and not 0")
