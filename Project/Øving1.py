from Functions import nest
from Functions import cp1c04a
from Functions import cp1c04b
from Functions import cp1c13a
from Functions import cp1c13b
from Functions import cp1c13c
from Functions import cp6c14a
import math as ma
import numpy as np


def cp1c01():
    x = 1.00001
    arr = [1] * 51

    res = nest(arr, x)
    exp = (x ** 51 - 1) / (x - 1)
    diff = ma.fabs(res - exp)
    emach = np.finfo(float).eps

    print("Error: ", diff, " (", diff / emach, " machine epsilons", ")")


def cp1c04():
    arr = []
    for n in range(1, 14):
        arr.append(ma.pow(10, -n))
    print(cp1c04b(arr))
    print(cp1c04a(arr))


def cp5c04():
    length1 = 3344556600
    length2 = 1.2222222
    length_hyp_squared = length1 * length1 + length2 * length2
    length_leg_squared = length1 * length1
    length_diff = length2 * length2
    length_diff = length_diff / (ma.sqrt(length_hyp_squared) + ma.sqrt(length_leg_squared))
    print(length_diff)


def cp1c13():
    a = 0.2
    a1 = 0
    b = 0.2
    b1 = 0
    c = 0.2
    c1 = 0
    while abs(a - a1) > 0.000000005:
        a1 = a
        a = cp1c13a(a)
    while abs(b - b1) > 0.000000005:
        b1 = b
        b = cp1c13b(b)
    while abs(c - c1) > 0.000000005:
        c1 = c
        c = cp1c13c(c)

    print("a) ", a)
    print("b) ", b)
    print("c) ", c)


def cp6c14():
    r = 0.2
    r1 = 0
    while abs(r - r1) > 0.00005:
        r1 = r
        r = cp6c14a(r)
    print(r)


# CP 1 chapter 0.1
# cp1c01()
# CP 1 chapter 0.4
# cp1c04()
# CP 5 chapter 0.4
# cp5c04()
# CP 1 chapter 1.3
# cp1c13()
# CP 6 chapter 1.4
cp6c14()
