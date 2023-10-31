#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
checked_num = number % 10
temp = number
if temp < 0:
    temp *= -1
    checked_num = -(temp % 10)
if checked_num > 5:
    print(f"Last digit of {number} is {checked_num} and is greater than 5")
elif checked_num == 0:
    print(f"Last digit of {number} is {checked_num} and is 0")
else:
    print(f"Last digit of {number} is {checked_num} and is less than 6 and not 0")
