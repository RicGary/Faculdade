from numpy import pi
import matplotlib.pyplot as plt

"""
Prova 1 de MetComp B

Nome: Eric Naiber
Número: 313389


Exercício proposto:
- Calcular a vazão da água de um tanque cônico utilizando Euler modificado.

    k1 = f(tn, xn)
    k2 = f(tn + h, xn + k1 * h)

    xn+1 = xn + (h/2) * (k1 + k2)

- Fórmula da vazão.
                         2
    dx/dt = -0.6 * pi * r * ((2 * g * x)^0.5)/A(x)

"""

# Constantes e valores úteis (já convertidos).

r = 0.03
g = 9.78


def A(x):
    """ Área circular do cone (área da base). """
    return pi * x ** 2


def f(xn):
    """ Fórmula da vazão dada no enunciado. """
    return -0.6 * pi * (r ** 2) * ((2 * g * xn) ** 0.5) / A(xn)


def __Vazao__(exercicio='b', tf=600, h=0.1):
    """ Cálculo da vazão utilizando Euler. """
    X = [2.438]
    T = [0]
    VOLUME = [15.1801757]

    if exercicio == 'b':

        while tf > T[-1]:
            k1 = f(X[-1])
            k2 = f(X[-1] + k1 * h)

            xn = X[-1] + (h / 2) * (k1 + k2)

            volume = (pi / 3) * xn ** 3

            VOLUME.append(volume)
            X.append(xn)
            T.append(T[-1] + h)

    if exercicio == 'c':
        condicao = True

        while condicao:

            k1 = f(X[-1])
            k2 = f(X[-1] + k1 * h)

            xn = X[-1] + (h / 2) * (k1 + k2)

            volume = (pi / 3) * xn ** 3

            VOLUME.append(volume)
            X.append(xn)
            T.append(T[-1] + h)

            if X[-1] < 0.1:
                condicao = False

    return X, T, VOLUME


def __Plot_Teste__():
    """
    Coloquei o plot dentro de uma função pois fica mais fácil
    de testar valores, já que não queremos ficar comentando o código
    do gráfico toda hora que alteramos algo no código.
    """

    X, T, V = __Vazao__('b')

    plt.plot(T, X, color='crimson')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Raio (m)')
    plt.title('Raio variando em 10 minutos.')
    plt.show()

    plt.plot(T, V)
    plt.ylabel('Volume (m3)')
    plt.xlabel('Tempo (s)')
    plt.title(f'Volume no instante de 10 minutos: {round(V[-1], 2)}m3')
    plt.show()

    X, T, V = __Vazao__('c')

    plt.plot(T, X, color='crimson')
    plt.xlabel('Tempo (s)')
    plt.ylabel('Raio (m)')
    plt.title(f'Tempo para esvaziar o tanque cônico: aprox. {int(T[-1] / 60)} minutos.')
    plt.show()
    print(f'O tanque leva {round(T[-1], 3)}s para esvaziar ou {round(T[-1] / 60, 1)} minutos.')

    plt.plot(T, V)
    plt.ylabel('Volume (m3)')
    plt.xlabel('Tempo (s)')
    plt.title(f'Volume no instante de {int(T[-1] / 60)} minutos: {round(V[-1], 2)}m3')
    plt.show()


def __SubPlots__(save=False):
    """
    save = False -> Não salvará a figura como um png/pdf
    save = True -> Salvará a figura como um png/pdf

    Coloquei o plot dentro de uma função pois fica mais fácil
    de testar valores, já que não queremos ficar comentando o código
    do gráfico toda hora que alteramos algo no código.
    """

    X, T, V = __Vazao__('b')

    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    axs[0, 0].plot(T, X, color='crimson')
    axs[0, 0].set_title('Raio variando em 10 minutos.')
    axs[0, 0].set_xlabel('Tempo (s)')
    axs[0, 0].set_ylabel('Raio (m)')

    axs[0, 1].plot(T, V)
    axs[0, 1].set_title(f'Volume no instante de 10 minutos: {round(V[-1], 2)}m3')
    axs[0, 1].set_xlabel('Tempo (s)')
    axs[0, 1].set_ylabel('Volume (m3)')

    X, T, V = __Vazao__('c')

    axs[1, 0].plot(T, X, color='crimson')
    axs[1, 0].set_title(f'Raio variando em {round(T[-1]/60, 2)} minutos.')
    axs[1, 0].set_xlabel('Tempo (s)')
    axs[1, 0].set_ylabel('Raio (m)')

    axs[1, 1].plot(T, V)
    axs[1, 1].set_title(f'Volume no instante de {round(T[-1]/60, 2)} minutos: {round(V[-1], 2)}m3')
    axs[1, 1].set_xlabel('Tempo (s)')
    axs[1, 1].set_ylabel('Volume (m3)')

    plt.subplots_adjust(left=0.1,
                        bottom=0.1,
                        right=0.9,
                        top=0.9,
                        wspace=0.2,
                        hspace=0.4)

    if save:
        import os
        if not os.path.exists('analise_volume'):
            plt.savefig('analise_volume')

    plt.show()


__SubPlots__()
