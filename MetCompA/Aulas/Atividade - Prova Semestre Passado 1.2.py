"""
1. Tarefa 1: Python
    (a) Escreva uma função em Python que calcule a função ln(1 + x) para |x| < 1 com base na
        expansão em série de Taylor:

        Note que você não poderá somar termos infinitamente. Por isso o somatório deverá ser de
        0 até um certo N.

    (b) Teste vários valores de N para verificar quando ln(1 + x) dado pela expressão (1) converge.
        Compare com o valor que você obtém se fizer o cálculo em uma calculadora. Construa um
        gráfico do valor obtido de ln(1 + x) dado pela equação (1) em função de N, para N no
        intervalo de 1 a 100. Salve esse gráfico em pdf.

    (c) Crie um programa em que o usuário forneça os valores de x e N e imprima na tela o valor
        de ln(1 + x). O programa deve verificar que |x| < 1.
"""
from numpy import linspace
import matplotlib.pyplot as plt


# 1.a) Escrevendo a função em série de Taylor.


def __Taylor__(x, n=100):
    taylor = 1 * x
    LISTA = [taylor]

    for i in range(1, n + 1):
        pn = (-1) ** i
        px = x ** (i + 1)
        pb = (i + 1)

        taylor += (pn * px) / pb

        LISTA.append(taylor)

    return LISTA

print(__Taylor__(0.5))

# 1.b) Gráfico

k = list(range(0, 101))

plt.plot(k, __Taylor__(0.5), color = 'crimson')
plt.xlabel('N')
plt.ylabel('Valor da série de Taylor')
plt.title('Análise de Valores')

plt.show()