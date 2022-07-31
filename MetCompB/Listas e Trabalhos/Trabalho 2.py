"""
Trabalho Pêndulo Caótico
    Métodos Computacionais da Física B

Nome: Eric Naiber
Cartão UFRGS: ##31##8#

Data de Início: 26/10/2021
Data de Entrega: 03/11/2021

Objetivo:
    Reproduzir os gráficos da página 167 do livro
    Classical Dynamics of Particles and Systems, (5a ed, aut. Marion, Thornton).


Equações:
    Runge-Kutta 4 ordem.

        d"x/dt" = -c dx/dt - sin(x) + Fcos(wt)

Reescrevendo:

    dv/dt = -cv - sin(x) + Fcos(wt)

    dx/dt = v

    Onde c, w são fixados e variamos apenas F de 0.4 até 1.0 variando de 0.1.

    c = 0.05
    w = 0.7

    h = 0.01

Tempo médio de execução do programa: 4.435 segundos.
    Ideias para otimizar:
        ✓ Trocar o while por for
        • Enquanto calcula o ponto xn, excluir o ponto x(n-2)
        • Plotar utilizando Scatter
        ✓ Melhorar os import / numpy e math ...
        • Tentar encaixar um Generator
        • Utilizar menos as listas

    Testes de otimização:
        Utilizando o numpy sin, cos e pi -> 4.435 segundos.
        Utilizando o math sin, cos e pi -> 1.422 segundos.
            - Sucesso

        Utilizando while -> 1.422 segundos.
        Utilizando for -> 1.301 segundos..

OBS:
    - Aumentar número de pontos (tf)

Tamanho lista pi = 315
Tamanho T = 100001
"""
import matplotlib.pyplot as plt
from math import sin, cos, pi, floor
from time import time

start_time = time()

# Definindo Constantes

c = 0.05
w = 0.7

# Definindo outros valores

force_variation = [i / 10 for i in range(4, 11)]


def F(x, v, t, force):
    return - c * v - sin(x) + force * cos(w * t)


def __Runge_Kutta__(f, tf=int(1000 * pi)):
    X = [1]
    V = [0]
    T = [0]
    THETA = [0]
    h = 0.01

    # Dados para fazer o corte apropriado

    len_inicial = 100001

    # Poincaré

    PERIOD = 2 * pi / w

    for _ in range(int(tf / h)):
        # K1

        xm = X[-1]
        vm = V[-1]

        k1_x = V[-1] * h
        k1_v = h * F(xm, vm, T[-1], f)

        # K2

        xm = X[-1] + 0.5 * k1_x
        vm = V[-1] + 0.5 * k1_v

        k2_x = h * vm
        k2_v = h * F(xm, vm, T[-1] + h / 2, f)

        # K3

        xm = X[-1] + 0.5 * k2_x
        vm = V[-1] + 0.5 * k2_v

        k3_x = h * vm
        k3_v = h * F(xm, vm, T[-1] + h / 2, f)

        # K4

        xm = X[-1] + k3_x
        vm = V[-1] + k3_v

        k4_x = h * vm
        k4_v = h * F(xm, vm, T[-1] + h, f)

        # Ponto

        x_novo = X[-1] + 1 / 6 * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
        v_novo = V[-1] + 1 / 6 * (k1_v + 2 * k2_v + 2 * k3_v + k4_v)

        # Adicionando o ponto

        T.append(T[-1] + h)
        X.append(x_novo)
        V.append(v_novo)

        theta = x_novo - floor(x_novo / (2 * pi)) * 2 * pi
        if theta > pi:
            theta = theta - (2 * pi)
        THETA.append(theta)

    len_total = len(T)

    return X[len_inicial: len_total],\
           V[len_inicial: len_total],\
           T[len_inicial: len_total],\
           THETA[len_inicial: len_total]


def __Graficos__():
    """
    Configuração de Gráfico criada por Eric Naiber.
    Suporta apenas versões 3.5x do Python ou maiores.

    Para utilizar as configurações do gráfico a sua
    função __Runge_Kutta__ deverá ter este formato:

    def __Runge_Kutta__(f, tf=int(160 * pi)):
        .
        .
        .
        return X, V, T

    Sendo X, V, T listas, com exatos 50202 pontos.
    Caso surja alguma dúvida, não tema em me chamar :)

    Caso o seu não funcione o código deverá abrir uma
    página no seu navegador.

    Se não abrir peço que clique no link printado, ele o
    levará para meu GitHub, onde você conseguirá ver o
    gráfico gerado.

    OBS:
    Se você for utilizar estas configurações para
    plotar o gráfico peço que não exclua a parte em
    que digo que o código foi feito por mim e a parte
    que printo meu GitHub.
    """

    Tf = 214100
    T0 = 204100

    try:
        fig = plt.figure()
        gs = fig.add_gridspec(7, 2, hspace=0)
        axs = gs.subplots(sharex=False)

        for i, f in enumerate(force_variation):
            X, V, T, THETA = __Runge_Kutta__(f)
            axs[i, 0].plot(T[T0: Tf], V[T0: Tf], color='black')
            axs[0, 0].set_title('Chaos in a Pendulum')
            axs[i, 0].set_yticks([])

            axs[i, 1].scatter(THETA[T0: Tf], V[T0: Tf], color='black', s=1)
            axs[0, 1].set_title('Phase-space plot.')
            axs[i, 1].set_yticks([])

        # \u03C0 --> Representa o pi

        axs[3, 0].set_ylabel("Angular Velocity, y = dx/dt'", labelpad=10)
        fig.set_size_inches(9.5, 9.5)
        print(f'{round(time() - start_time, 3)} seconds.')
        plt.show()

    except:
        from webbrowser import open
        open('https://github.com/RicGary/MetCompB/blob/main/Listas%20e%20Trabalhos/Graficos_Trab2.JPG')

        print("Caso o site não tenha aberto, clique no link logo abaixo:")
        print('https://github.com/RicGary/MetCompB/blob/main/Listas%20e%20Trabalhos/Graficos_Trab2.JPG')


__Graficos__()