

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
    return b/a



def log(a, b):
    if b <= 0:

        raise ValueError ("Logarithm of zero or negative number is not allowed")
    if a<=0 or a ==1:
        raise ValueError ("Logarithm must be positive and not equal to 1")

    return math.log(b,a)

def exp(a, b):
    return a**b




