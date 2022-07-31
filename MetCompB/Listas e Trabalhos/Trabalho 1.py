"""
OBS: ESTE CÓDIGO FOI FEITO COM O PROPÓSITO DE ENSINAR OUTRAS PESSOAS, SENDO ASSIM, NÃO ME PREOCUPEI COM
     O DESEMPRENHO, MUITAS LINHAS PODERIAM TER SIDO FEITAS DE FORMA MAIS RÁPIDA.

Problema de valor inicial: Ressonância.

y(0) = 0

0 <= t <= 8
w = pi
w0 = 2

y'' + w²y = cos(w0.t)


Solução analítica:

- Se w = w0
    y = t/2w . sen(wt)

- Se w != w0
    y = cos(w0.t) - cos(w.t)/(w² - w0²)
"""
from numpy import linspace, sin, pi, cos
import matplotlib.pyplot as plt
from copy import deepcopy

# Definindo Constantes;
w = pi
h = 0.001


def __cromer__(h):
    """
    Função a ser tratada:

    y'' + w²y = cos(w.t)

    O Euler-Cromer funciona da seguinte forma:

    v(n+1) = vn + a(tn; xn; vn) * h
    x(n+1) = xn + v(n+1) * h

    Convertendo para nossa fução:

    dv/dt = cos(w.t) - w²y
    dx/dt = v
    """
    X = [0]
    V = [0]
    t = [0]
    tf = 8

    while tf > t[-1]:
        vn = V[-1] + (cos(w * t[-1]) - w ** 2 * X[-1]) * h
        xn = X[-1] + vn * h

        V.append(vn)
        X.append(xn)
        t.append(t[-1] + h)

    Xc = deepcopy(X)
    tc = deepcopy(t)

    return tc, Xc


def __verlet__(h):
    """
    Função a ser tratada:

    y'' + w²y = cos(w.t)

    O método de Verlet funciona da seguinte forma:

    x(n+1) = 2xn - x(n-1) + a(tn; xn; vn) * h ** 2
    vn = ( x(n+1) - x(n-1) )/2*h

    Convertendo para nossa fução:

    dv/dt = cos(w.t) - w²y
    dx/dt = v

    OBS: Para encontrar x(n-1) utilizaremos Euler-Cromer
    """
    X = [0]
    V = [0]
    t = [0]
    tf = 8

    vn = V[-1] + (cos(w * t[-1]) - w ** 2 * X[-1]) * h
    xn = X[-1] + vn * h

    V.append(vn)
    X.append(xn)
    t.append(t[-1] + h)

    while tf > t[-1]:
        xn = 2 * X[-1] - X[-2] + (cos(w * t[-1]) - w ** 2 * X[-1]) * h ** 2

        V.append(vn)
        X.append(xn)
        t.append(t[-1] + h)

    Xv = deepcopy(X)
    tv = deepcopy(t)

    return tv, Xv


def __rk4__(h):
    """
    Função a ser tratada:

    y'' + w²y = cos(w.t)

    O método de Runge-Kutta 4 da seguinte forma:

        - Olhar Aula 12: https://github.com/RicGary/MetCompB/tree/main/Aulas

    Convertendo para nossa fução:

    dv/dt = cos(w.t) - w²y
    dx/dt = v

    OBS: Já que o código é muito extenso irei utilizar o já feito anteriormente,
        sendo assim definirei uma função dentro da outra, mas gostaria de ressaltar
        que fazer algo deste tipo NÃO é recomendável.
    """
    X = [0]
    V = [0]
    t = [0]
    tf = 8

    def F(t, x):
        return cos(w * t) - w ** 2 * x

    while t[-1] <= tf:
        # x inicial:
        xm = X[-1]

        # Calculando os k1:
        k1_x = V[-1] * h
        k1_v = h * F(t[-1], X[-1])

        # Calculando os k2: xm = xi + 1/2 * k1.x | k3.x = h * vm
        xm = X[-1] + 0.5 * k1_x
        vm = V[-1] + 0.5 * k1_v

        k2_x = h * vm
        k2_v = h * F(t[-1] + h / 2, xm)

        # Calculando os k3:
        xm = X[-1] + 0.5 * k2_x
        vm = V[-1] + 0.5 * k2_v

        k3_x = h * vm
        k3_v = h * F(t[-1] + h / 2, xm)

        # Calculando os k4:
        xm = X[-1] + k3_x
        vm = V[-1] + k3_v

        k4_x = h * vm
        k4_v = h * F(t[-1] + h, xm)

        # Finalmente, o próximo ponto
        x_novo = X[-1] + 1 / 6 * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)
        v_novo = V[-1] + 1 / 6 * (k1_v + 2 * k2_v + 2 * k3_v + k4_v)

        # Finalizando o código
        t.append(t[-1] + h)
        X.append(x_novo)
        V.append(v_novo)

    Xr = deepcopy(X)
    tr = deepcopy(t)

    return tr, Xr


def __analitica__(h):
    x = linspace(0, 8, num=int(8 / h + 2))
    y = x * sin(pi * x) / (2 * pi)

    return x, y


def __plots__():
    plt.plot(tc, Xc, label='Euler-Cromer', color='gold')
    plt.plot(tv, Xv, label='Velocity-Verlet', color='salmon')
    plt.plot(tr, Xr, label='Runge-Kutta 4', color='rebeccapurple')
    plt.plot(t, x, label='Solução Analítica', color='darkslategrey')
    plt.legend()
    plt.title('Análise se método no problema de Ressonância. h = 0,001')
    plt.show()


tc, Xc = __cromer__(h)
tv, Xv = __verlet__(h)
tr, Xr = __rk4__(h)
t, x = __analitica__(h)


def __erro__():
    ERRO_CROMER = []
    ERRO_VERLET = []
    ERRO_RUNGE = []

    for i in range(8001):
        erro_c = abs(Xc[i] - x[i])
        erro_v = abs(Xv[i] - x[i])
        erro_r = abs(Xr[i] - x[i])

        ERRO_CROMER.append(erro_c)
        ERRO_VERLET.append(erro_v)
        ERRO_RUNGE.append(erro_r)

    plt.plot(tc, ERRO_CROMER, 'o', markersize=2, color='red', label='Erro: Euler-Cromer')
    plt.plot(tv, ERRO_VERLET, 'x', markersize=1, color='lime', label='Erro: Verlet')
    plt.plot(tr, ERRO_RUNGE, 'o', markersize=1, color='blue', label='Erro: Runge-Kutta 4')

    plt.yscale('log')
    plt.title('Análise dos erros.')
    plt.legend()
    plt.show()


__plots__()
__erro__()
