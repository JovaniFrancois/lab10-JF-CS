

"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.

"""

# First example



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

        raise ValueError ("Logarithm of zero")

    return math.log(b,a)

def exp(a, b):
    return a**b


print (log(1, 2))

