# https://github.com/Diashroom/lab11-JP.git
# Partner 1: Jingjing
# Partner 2: Jingjing


import math

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero.")
    return a / b

def logarithm(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Arguments for logarithm must be positive.")
    return math.log(b, a)

def exponent(a, b):
    return a ** b

