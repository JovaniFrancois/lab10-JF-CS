#https://github.com/JovaniFrancois/lab10-JF-CS
#Cecil Took Role 2
#Jovani Took Role 1
"""
calculator.py
- Defines functions used to create a simple calculator

One function per operation, in order.

"""
#https://github.com/JovaniFrancois/lab10-JF-CS
# First example

#Git hub repository : https://github.com/JovaniFrancois/lab10-JF-CS


import math
def add(a, b):
    return a+b

def subtract(a, b):
    return a - b

def mul(a, b):
    return a*b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError ("Division by zero is not allowed")
    return a/b



def logarithm(x, base):
    if b <= 0:

        raise ValueError ("Logarithm of zero or negative number is not allowed")
    if a<=0 or a ==1:
        raise ValueError ("Logarithm must be positive and not equal to 1")

    return math.log(x,base)

def exp(a, b):
    return a**b



