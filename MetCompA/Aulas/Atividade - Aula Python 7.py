from random import randint
from numpy import nanmean, nanstd
from matplotlib.pyplot import hist, show
from collections import Counter
from colorama import init
from colorama import Back


# Parte 1: Escreva uma função que retorna um array de N valores de Y


def __yvalores__(N):
    Y = tuple(randint(1, 6) + randint(1, 6) for _ in range(N))
    return Y


# Parte 2: Escreva uma função que retorna uma estimativa da média de um array y usando a equação acima


def __media(N):
    Y = __yvalores__(N)
    soma = 0
    for valor in Y:
        soma += valor

    return soma / N, Y


# Parte 3:  Escreva uma função que retorna uma estimativa do desvio padrão de um array y usando a equação acima


def __desvio_padrao(N):
    media, Y = __media(N)
    desvio_parte = tuple((y - media) ** 2 for y in Y)

    soma = 0
    for valor in desvio_parte:
        soma += valor
    desvio_padrao = (soma / N) ** 0.5

    return desvio_padrao, media, Y


# Parte 4: Encontre a média e o desvio padrão da média para N=1000 jogadas dos dois dados utilizando as funções
# dos itens 2 e 3 acima. Compare os resultados com os obtidos usando os métodos numpy.mean() e
# numpy.std()


def __comparacao():
    desvio_padrao, media, Y = __desvio_padrao(1000)

    if round(desvio_padrao, 5) == round(nanstd(Y), 5):
        print('O desvio padrão foi calculado da forma correta.')

    if media == nanmean(Y):
        print('A média foi calculada de forma correta')


# Parte 5: Faça um histograma dos valores Y obtidos a partir de N = 1000 jogadas dos dois dados. Salve este
# gráfico em formato PNG.


def __terminal_graph():
    Y = sorted(__yvalores__(1000))
    B = Counter(Y)

    chaves = []
    valores = []

    for i in B:
        chaves.append(i)
    for i in chaves:
        valores.append(B[i])

    print('    5%   10%   15%   25%   30%   35%   40%')
    for i in range(len(B)):
        print(f'{chaves[i]:^2}', end='')
        if chaves[i] == 2 or chaves[i] == 12:
            print(Back.LIGHTBLUE_EX + " " * int(valores[i] / 5) + Back.RESET)
        if chaves[i] == 3 or chaves[i] == 11:
            print(Back.BLUE + " " * int(valores[i] / 5) + Back.RESET)
        if chaves[i] == 4 or chaves[i] == 10:
            print(Back.LIGHTYELLOW_EX + " " * int(valores[i] / 5) + Back.RESET)
        if chaves[i] == 5 or chaves[i] == 9:
            print(Back.YELLOW + " " * int(valores[i] / 5) + Back.RESET)
        if chaves[i] == 6 or chaves[i] == 8:
            print(Back.RED + " " * int(valores[i] / 5) + Back.RESET)
        if chaves[i] == 7:
            print(Back.LIGHTRED_EX + " " * int(valores[i] / 5) + Back.RESET)
    print('    5%   10%   15%   25%   30%   35%   40%')

    print(valores)


import matplotlib.pyplot as plt


def __grafico():
    Y = __yvalores__(1000)
    hist(Y, bins=11, color='crimson')
    show()


__grafico()

__terminal_graph()