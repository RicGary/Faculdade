from numpy import pi
import matplotlib.pyplot as plt

"""
def __esq__(x, n = 100):

    N = linspace(1, n, num = n)

    VALORES_ARCTAN = list( (((-1)**i)/(2*i + 1))*(x**(2*i + 1)) for i in N)
    VALORES_ARCTAN[0] = x*1


    return N, VALORES_ARCTAN, sum(VALORES_ARCTAN)
"""


# 1.a)

def __Taylor__(x, n=100):
    LISTA_N = []
    LISTA_ARCTAN = []

    arctan = x * 1
    for i in range(1, n + 1):
        parte_cima = (-1) ** i
        parte_baixo = (2 * i + 1)
        parte_x = x ** (2 * i + 1)

        arctan = arctan + (parte_cima / parte_baixo) * parte_x

        LISTA_N.append(i)
        LISTA_ARCTAN.append(arctan)

    return LISTA_N, LISTA_ARCTAN, LISTA_ARCTAN[-1]


# 1.b)

x, y, valor = __Taylor__(0.5, 100)

plt.plot(x, y, color='crimson')
plt.title('Análise Arco Tangente')
plt.xlabel('N')
plt.ylabel('ArcTan')
plt.show()


# 1.c)

def __Graus__():
    x = float(input('Insira o valor de x: '))
    if abs(x) > 1:
        print("Valor inválido. Insira o algo entre -1 e 1.")

    n = int(input('Insira o valor de n: '))

    return __Taylor__(x, n)[2] * 180 / pi


print(__Graus__())
