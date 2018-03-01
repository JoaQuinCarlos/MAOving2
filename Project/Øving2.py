import numpy as np
from Functions2 import gausselim
from Functions2 import tilbakesubstitusjon
from Functions2 import LUtilbakesubstitusjon
from Functions2 import jacobi


def cp1c21():
    a = np.array([[2.0, -2.0, -1.0, -2.0],[4.0, 1.0, -2.0, 1.0],[-2.0, 1.0, -1.0, -3.0]])
    b = np.array([[1.0, 2.0, -1.0, 2], [0, 3.0, 1.0, 4], [2.0, -1.0, 1.0, 2]])
    c = np.array([[2.0, 1.0, -4.0, -7], [1, -1.0, 1.0, -2], [-1.0, 3.0, -2.0, 6]])

    ag = gausselim(a)[0]
    bg = gausselim(b)[0]
    cg = gausselim(c)[0]

    print("Oppgave A")
    print(ag)
    s1 = tilbakesubstitusjon(ag)
    print(s1)
    print()

    print("Oppgave B")
    print(bg)
    s2 = tilbakesubstitusjon(bg)
    print(s2)
    print()

    print("Oppgave C")
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
    print("L:")
    print(L)
    print("U:")
    print(U)


def cp2c22(A):
    s = A.shape
    L = gausselim(A)[1]
    L = np.c_[L, A[:, s[1]-1]]
    U = gausselim(A)[0]
    x1 = LUtilbakesubstitusjon(L)
    U = np.c_[U, x1]
    print(tilbakesubstitusjon(U))


def cp6c23():
    oppg62 = np.array([
        [10.0 ** -20, 1.0, 1.0],
        [1.0, 2.0, 4.0]
    ])
    oppg63 = np.array([
        [1.0, 2.0, 4.0],
        [10.0 ** -20, 1.0, 1.0]
    ])
    print("Naiv gauss")
    print(tilbakesubstitusjon(gausselim(oppg62)[0]))
    print("Med radbytte")
    print(tilbakesubstitusjon(gausselim(oppg63)[0]))


def cp1c25a(n):
    A = np.array([[0.0]*n for _ in range(n)])
    S = np.array([0.0]*n)
    for m in range(0, n):
        A[m, m] = 3
        if m < n - 1:
            A[m, m + 1] = -1
            S[m] = 1
        if m > 0:
            A[m, m - 1] = -1
            S[m] = 1
        if m == 0 or m == n-1:
            S[m] = 2
    S0 = np.array([0.0]*n)
    return jacobi(A, S, S0)


def cp1c25b(n):
    S = np.array([0.0]*n)
    for m in range(0, n):
        if m < n - 1:
            S[m] = 1
        if m > 0:
            S[m] = 1
        if m == 0 or m == n-1:
            S[m] = 2
    tempS = np.array([0.0]*n)
    S0 = np.array([0.0]*n)
    s = 1
    counter = 0
    while s > 0.0000001:
        counter += 1
        s = 0
        for i in range(0, n):
            if i == 0:
                newVal = (S[i] + S0[i + 1]) / 3
            elif i == (n - 1):
                newVal = (S[i] + S0[i - 1]) / 3
            else:
                newVal = (S[i] + S0[i - 1] + S0[i + 1]) / 3
            if abs((S0[i] - newVal)) > s:
                s = abs(S0[i] - newVal)
            tempS[i] = newVal
        S0 = tempS.copy()
    print("Iterasjoner: ", counter)
    calcBackwardError(S, S0)
    return S0


def calcBackwardError(S, S0):
    n = S.shape[0]
    e = np.array([0.0]*n)
    for i in range(0, n):
        if i == 0:
            e[i] = abs(S[i] - (S0[i]*3 - S0[i + 1]))
        elif i == (n - 1):
            e[i] = abs(S[i] - (S0[i]*3 - S0[i - 1]))
        else:
            e[i] = abs(S[i] - (S0[i]*3 - S0[i + 1] - S0[i - 1]))
    print("Backward error: ", np.amax(e))


# Computer problem 1 chapter 2.1
# cp1c21()

# Computer problem 2 chapter 2.1
# print("n = 2")
# cp2c21(2)  # n = 2
# print()
# print("n = 5")
# cp2c21(5)  # n = 5
# print()
# print("n = 10")
# cp2c21(10)  # n = 10

# Computer problem 1 chapter 2.2
# La til en vektor med 0ere til høyre i matrisene for å kunne gjenbruke koden fra kapittel 2.1

# cp1c22(np.array([[3.0, 1.0, 2.0, 0.0], [6.0, 3.0, 4.0, 0.0], [3.0, 1.0, 5.0, 0.0]]))  # a)
# cp1c22(np.array([[4.0, 2.0, 0.0, 0.0], [4.0, 4.0, 2.0, 0.0], [2.0, 2.0, 3.0, 0.0]]))  # b)
# cp1c22(np.array([[1.0, -1.0, 1.0, 2.0, 0.0], [0.0, 2.0, 1.0, 0.0, 0.0], [1.0, 3.0, 4.0, 4.0, 0.0], [0.0, 2.0, 1.0, -1.0, 0.0]]))  # c)

# Computer problem 2 chapter 2.2
# print("Oppgave A:")
# cp2c22(np.array([[3, 1, 2, 0], [6, 3, 4, 1], [3, 1, 5, 3]]))  # a)
# print()
# print("Oppgave B:")
# cp2c22(np.array([[4, 2, 0, 2], [4, 4, 2, 4], [2, 2, 3, 6]]))  # b)

# Computer problem 6 chapter 2.3
# cp6c23()

# Computer problem 1 chapter 2.5
print("Generel metode: ")
S = cp1c25a(100)
calcBackwardError(S[0], S[1])
print()
print("Rask metode: ")
Sa = cp1c25b(100)  # Oppgave a
Sb = cp1c25b(100000)  # Oppgave b
