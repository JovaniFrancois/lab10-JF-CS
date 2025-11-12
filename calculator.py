

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.

"""

# First example
#Cecil Took Role 2
#Jovani Took Role 1
#Git hub repository : https://github.com/JovaniFrancois/lab10-JF-CS


import math
def add(a, b):
    return a+b

def sub(a, b):
    return a - b

def mul(a, b):
    return a*b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError ("Division by zero is not allowed")




def log(a, b):
    if b == 0:

        raise ValueError ("Logarithm of zero is not allowed")

    return math.log(b,a)

def exp(a, b):
    return a**b




