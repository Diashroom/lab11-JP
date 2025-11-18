# https://github.com/Diashroom/lab11-JP.git
# Partner 1: Jingjing
# Partner 2: Jingjing


import math


def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if a == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return b / a

def log(a, b):
    if a <= 0 or b <= 0:
        raise ValueError("Logarithm arguments must be positive")
    return math.log(b, a)

def exp(a, b):
    return a ** b