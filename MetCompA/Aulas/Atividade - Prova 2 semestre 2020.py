"""
Prova 2 - Semestre 2020/2
"""
from math import e


def F(x, u):
    return 1 / (e ** ((x - u) / 0.02) + 1)


def G(u):
    return __Simpson__(u) - 1


def __Simpson__(u, a=0, b=2, N=100):
    extremos = F(a, u) + F(b, u)

    h = (b - a) / N

    for i in range(1, N):
        if i % 2:  # Ímpar pois 0 -> False
            extremos += 4 * F(a + i * h, u)

        else:
            extremos += 2 * F(a + i * h, u)

    return extremos * h / 3


def __Zero_Secante__(a, b, erro=1e-6):
    while erro <= abs(b - a) / abs(a):
        c = (a * G(b) - b * G(a)) / (G(b) - G(a))

        if abs(c - a) < abs(b - c):
            b, a = a, c
        else:
            a, b = b, c

    return a


print(__Zero_Secante__(0.1, 2))