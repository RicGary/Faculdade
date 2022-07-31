"""
Trabalho 3: Mapa Logístico (até 24/11)

Nome: Eric Naiber
Cartão UFRGS: 31***9

Versão Python: 3.9.2
IDE: PyCharm
"""
import matplotlib.pyplot as plt
from numpy import linspace

# Constante inicial

x0_init = 0.51
n_max = 1000

# Valores de lambda

LAMB = (0.7, 0.8, 0.88, 1)

# Listas para futuros gráficos

XNs = [[] for _ in range(len(LAMB))]
X0s = [[] for _ in range(len(LAMB))]

N = [n for n in range(n_max)]


def __Map__(x, lamb):
    """
    Equação do mapa logístico.

    OBS: Em julia o código ficaria com o lambda bonito :(

    :param x0: calor inicial.
    :param lamb: lambda
    :return: valor do próximo x
    """

    return 4 * lamb * x * (1 - x)


def __Questao_1__(graph=1):
    """
    Função para povoar as listas XNs.

    O código funciona da seguinte forma:

    - Primeiro fazemos um loop for utilizando enumerate(), já que
    este retorna o valor da lista e seu index, o index será importante
    para poder trocar a lista de XN.

    - Para cada lambda temos um index de 0 até 3, e para cada índice temos
    uma lista própria.

    - Já que N não muda podemos utilizar list comprehension para povoar o
    mesmo.

    - Retorno True por motivo algum :)

    By Eric Naiber.
    """

    CORES = ('black', 'crimson', 'gold', 'mediumaquamarine')
    MARCADORES = ('.', ',', 'v', '8')
    NUMERINHOS = ('\u2081', '\u2082', '\u2083', '\u2084')

    for i, lamb in enumerate(LAMB):
        x0 = x0_init

        for n in range(1, n_max + 1):
            xn = __Map__(x0, lamb)

            X0s[i].append(x0)
            XNs[i].append(xn)

            x0 = xn

        if graph:
            plt.scatter(N, XNs[i], color=CORES[i], marker=MARCADORES[i],
                        s=1.5, label=f'\u03BB{NUMERINHOS[i]} = {lamb}')
    if graph:
        plt.title('Gráfico Questão 1: X\u2099 \u2A2F n ')
        plt.legend()
        plt.xlabel(f'N = {len(N)}')
        plt.ylabel('x\u2099', fontsize=12)
        plt.show()

    return True


def __Questao_2__(graph=1):
    """

    :return:
    """
    X = linspace(0, 0.6, num=50)
    # plt.hlines(0.5, __Map__(0.5, lamb), __Map__(0.5, lamb), linestyles='-')

    for lamb in LAMB:
        Y = __Map__(X, lamb)
        plt.plot(X, Y, color='crimson', label='f(x) = map')
        plt.plot(Y, Y, color='black', label='Y = Y')
        plt.xlim(0, 0.6)

        n = X[1]
        i = 0
        for _ in range(2, 50):
            if i < 4:
                plt.hlines(__Map__(n, lamb), n, __Map__(n, lamb), linestyles='--', colors='darkturquoise')
                plt.vlines(n, n, __Map__(n, lamb), linestyles='--', colors='darkturquoise')
                n = __Map__(n, lamb)
                i += 1

        plt.legend()
        plt.show()

    return X


def __Questao_3__(graph=1):
    """
    Fixa valor de lambda
    n = índice temporal???
    E = outro indice temporal

    gera a série temporal
    x0, x1, ..., xn

    1 pra True
    0 para False

    E = índice temportal de f(n)
    n = índice temporal de n

    Condição:   e = 1e-5
    1, abs(f(n)-n) < e
    0, else

    plotar condição
    """


def __Questao_4__():
    """
    lambda -> lb_1
    f(x, lambda) -> for 20 vzs lb_1
    append -> f(x) estável

    as vezes tem 2 valores de f(x) estável
    para cada valor estável adiciona mais um lambda
    """
    from collections import Counter

    LAMBDA = []
    Xn = []

    lamb = 0.7
    while lamb < 1:
        x0 = x0_init
        temp = [x0]
        for _ in range(20):
            xn = __Map__(x0, lamb)
            temp.append(round(xn, 5))
            x0 = xn

        count = Counter(temp)

        for i in count.keys():
            if count[i] > 1:
                Xn.append(i)
                LAMBDA.append(lamb)

        for i in range(10, 20):
            LAMBDA.append(lamb)
            Xn.append(temp[i])

        lamb += 0.00005

    plt.scatter(LAMBDA, Xn, s=0.2, color='crimson')
    plt.ylabel('x\u2099 \u208a \u2081', fontsize=15)
    plt.xlabel('\u03BB', fontsize=13)
    plt.title('Diagrama de Bifurcação')
    plt.show()


__Questao_1__()
__Questao_2__()
__Questao_3__()
__Questao_4__()
