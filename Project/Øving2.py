import numpy as np
from Functions2 import gausselim
from Functions2 import tilbakesubstitusjon
from Functions2 import LUtilbakesubstitusjon


def cp1c21():
    a = np.array([[2.0, -2.0, -1.0, -2.0],[4.0, 1.0, -2.0, 1.0],[-2.0, 1.0, -1.0, -3.0]])
    b = np.array([[1.0, 2.0, -1.0, 2], [0, 3.0, 1.0, 4], [2.0, -1.0, 1.0, 2]])
    c = np.array([[2.0, 1.0, -4.0, -7], [1, -1.0, 1.0, -2], [-1.0, 3.0, -2.0, 6]])

    ag = gausselim(a)[0]
    bg = gausselim(b)[0]
    cg = gausselim(c)[0]

    print(ag)
    s1 = tilbakesubstitusjon(ag)
    print(s1)

    print(bg)
    s2 = tilbakesubstitusjon(bg)
    print(s2)

    print(cg)
    s3 = tilbakesubstitusjon(cg)
    print(s3)


def cp2c21(n):
    A = 1. / (np.arange(1, n + 1) + np.arange(0, n)[:, np.newaxis])
    A = np.c_[A, np.ones(n)]
    B = gausselim(A)[0]
    S = tilbakesubstitusjon(B)
    print(S)


def cp1c22(arr):
    A = arr
    U = gausselim(A)[0]
    L = gausselim(A)[1]
    print(L)
    print(U)


def cp2c22(A):
    s = A.shape
    L = gausselim(A)[1]
    L = np.c_[L, A[:, s[1]-1]]
    U = gausselim(A)[0]
    x1 = LUtilbakesubstitusjon(L)
    U = np.c_[U, x1]
    print(tilbakesubstitusjon(U))


# Computer problem 1 chapter 2.1
# cp1c21()

# Computer problem 2 chapter 2.1
# cp2c21(2)  # n = 2
# cp2c21(5)  # n = 5
# cp2c21(10)  # n = 10

# Computer problem 1 chapter 2.2
# La til en vektor med 0ere til høyre i matrisene for å kunne gjenbruke koden fra kapittel 2.1

# cp1c22(np.array([[3.0, 1.0, 2.0, 0.0], [6.0, 3.0, 4.0, 0.0], [3.0, 1.0, 5.0, 0.0]]))  # a)
# cp1c22(np.array([[4.0, 2.0, 0.0, 0.0], [4.0, 4.0, 2.0, 0.0], [2.0, 2.0, 3.0, 0.0]]))  # b)
# cp1c22(np.array([[1.0, -1.0, 1.0, 2.0, 0.0], [0.0, 2.0, 1.0, 0.0, 0.0], [1.0, 3.0, 4.0, 4.0, 0.0], [0.0, 2.0, 1.0, -1.0, 0.0]]))  # c)

cp2c22(np.array([[3, 1, 2, 0], [6, 3, 4, 1], [3, 1, 5, 3]]))  # a)
cp2c22(np.array([[4, 2, 0, 2], [4, 4, 2, 4], [2, 2, 3, 6]]))  # b)
