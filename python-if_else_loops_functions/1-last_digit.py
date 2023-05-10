#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    convert = number * -1
    lastdig = (convert % 10)
    if lastdig == 0:
        print(f"Last digit of {number} is {lastdig} and is 0")
    else:
        print(f"Last digit of {number} is {lastdig * -1} and is less than 6 and not 0")
else:
    lastdig = (number % 10)
    if lastdig > 5:
        print(f"Last digit of {number} is {lastdig} and is greater than 5")
    elif lastdig == 0:
        print(f"Last digit of {number} is {lastdig} and is 0")
    else:
        print(f"Last digit of {number} is {lastdig} and is less than 6 and not 0")
