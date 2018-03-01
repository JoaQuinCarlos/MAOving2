import numpy as np


def gausselim(A):
    s = A.shape
    n = s[0]
    m = s[1]
    G = np.copy(A)
    L = np.array([[0.0]*n for _ in range(n)])

    for m in range(0, n):
        row = L[m]
        row[m] = 1

    for j in range(0, n - 1):
        for i in range(j+1, n):
            mult = (G[i, j]/G[j, j])
            L[i, j] = mult
            for k in range(j, m + 2):
                G[i, k] = G[i, k]-G[j, k]*mult
    return G, L


def jacobi(A, S, S0):
    n = A.shape[0]
    diff = np.array([1.0]*n)  # Endringen fra iterasjon til iterasjon. Setter den lik 1 for alle ukjente fra start.
    counter = 0
    while np.amax(diff) > 0.0000001:  # Så lenge løsningen ikke har 6 riktige desimaler
        tempS0 = np.array([0.0] * n)  # Array for å lagre den nye S0 siden Jakobi ikke bruker oppdaterte verdier
        for i in range(0, n):
            tot = S[i]
            for j in range(0, i):
                tot -= S0[j]*A[i, j]
            for k in range(i+1, n):
                tot -= S0[k]*A[i, k]
            tempS0[i] = tot/A[i, i]
        for i in range(0, n):
            diff[i] = abs(S0[i]-tempS0[i])  # Oppdaterer differansen
        S0 = tempS0  # Oppdater S0
        counter += 1
    print("Iterasjoner: ", counter)
    return S, S0


def tilbakesubstitusjon(Ain):
    s = Ain.shape
    n = s[0]  # Antall rader
    m = s[1]  # Antall søyler
    A = np.copy(Ain)
    b = A[:, m-1]
    x = [0] * n  # Løsningsvektor
    x[n-1] = b[n-1]/A[n-1, n-1]
    for i in range(n-2, -1, -1):
        x[i] = b[i]/A[i, i]
        for j in range(i + 1, n):
            x[i] = x[i]-A[i, j] * x[j]/A[i, i]
    return x


def LUtilbakesubstitusjon(L):
    s = L.shape
    n = s[0]
    m = s[1]
    A = np.copy(L)
    b = A[:, m-1]
    x = [0] * n
    x[0] = b[0]/A[0, 0]
    for i in range(1, n):
        x[i] = b[i]/A[i, i]
        for j in range(i - 1, -1, -1):
            x[i] = x[i]-A[i, j] * x[j]/A[i, i]
    return x

