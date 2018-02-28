import math as ma
import numpy as np


def nest(c, x, b=None):
    d = len(c)-1
    if b is None:
        b = [0] * d
    y = c[d]
    i = d-1
    while i > -1:
        y = y*(x-b[i])+c[i]
        i = i - 1
    return y


# Rewritten function
def cp1c04a(numbers):
    res = []
    for n in numbers:
        fx = -1/(1 + 1 / ma.cos(n))
        res.append(fx)
    return res


# Original function
def cp1c04b(numbers):
    res = []
    for n in numbers:
        fx = (1 - (1/ma.cos(n)))/(ma.tan(n) * ma.tan(n))
        res.append(fx)
    return res


# Function a
def cp1c13a(x):
    return x - (x ** 3 - 2 * x - 2) / (3 * x ** 2 - 2)


def cp1c13b(x):
    return x - (ma.e ** x + x - 7) / (ma.e ** x + 1)


def cp1c13c(x):
    return x - (ma.e ** x + ma.sin(x) - 4) / (ma.e ** x + ma.cos(x))


def cp6c14a(x):
    return x - ((2 * ma.pi * x ** 3) / 3 + (10 * ma.pi * x ** 2) / 3 - 60) / (2 * ma.pi / 3 * x * (3 * x + 10))
