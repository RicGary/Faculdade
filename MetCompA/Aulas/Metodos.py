"""
Código com quase todo o conteúdo da área 2

Escrito utilizando:
 - PyCharm 2020.2.5
 - Python 3.9.2

By Eric Naiber.
"""


def __Simples__(f, a, b, N):
    """
    Função para calcular uma integral utilizando o método mais
    simples possível.

    Escala de precisão: ★ ☆ ☆ ☆ ☆

    :param f: função
    :param a: limite inferior
    :param b: limite superior
    :param N: quantia de fatias
    """
    integral = 0
    dx = (b - a) / N

    for i in range(N):
        x = a + i * dx
        integral = integral + f(x) * dx

    return integral


def __Trapezio__(f, a, b, N):
    """
    Função para calcular uma integral utilizando o método um pouco mais elegante
    que o método simples.

    Escala de precisão: ★ ★ ☆ ☆ ☆

    :param f: função
    :param a: limite inferior
    :param b: limite superior
    :param N: quantia de fatias
    """
    from numpy import linspace

    delta_x = (b - a) / N
    inicio = (f(a) + f(b)) / 2

    N_VALORES = linspace(a, b, N)

    for i in range(1, N - 1):
        inicio += f(N_VALORES[i])

    return inicio * delta_x


def __Simpson__(f, a, b, N):
    """
    Função para calcular uma integral utilizando o método legítimo e útil,
    possui uma ótima precisão.

    Escala de precisão: ★ ★ ★ ★ ☆

    :param f: função
    :param a: limite inferior
    :param b: limite superior
    :param N: quantia de fatias
    """

    extremos = f(a) + f(b)

    h = (b - a) / N

    for i in range(1, N):
        if i % 2:  # Ímpar pois 0 -> False
            extremos += 4 * f(a + i * h)

        else:
            extremos += 2 * f(a + i * h)

    return extremos * h / 3


def __Erro__(Iexato, metodo, f, a, b, N):
    """
    Função para calcular o erro da integral.

    Iexato: valor exato da integral
    metodo: método de integração
    :param f: função
    :param a: limite inferior
    :param b: limite superior
    :param N: quantia de fatias
    """
    return abs(Iexato - metodo(f, a, b, N))


def __Zero_Bisseccao__(f, a, b, erro=1e-8):  # Recebe quaisquer f(x), o intervalo [a,b] e a tolerância desejada.
    """
    Contribuição: Michel Alves da Silva

    Função para calcular os zeros de uma função a partir
    de um "chute" inicial.

    Pode dar resultados errados se os chutes não forem perto, e
    também é muito lento.

    Qualidade do método: ★ ★ ☆ ☆ ☆
    """

    while abs(b - a) > erro:
        xm = (a + b) / 2
        if f(a) * f(xm) < 0:
            b = xm

        else:
            a = xm

    return xm


def __Zero_Newton__(f, x, erro=1e-8):
    """
    Contribuição: Augusto Bopsin Borges

    Função para calcular os zeros de uma função a partir
    de um "chute" inicial.

    Pode dar resultados errados se o chute não for muito perto, é
    mais rápido que o método da bissecção, porém depende do valor
    da derivada.

    Qualidade do método: ★ ★ ★ ☆ ☆

    :param f: função
    :param x: chute inicial
    """
    def deriv_centrada(f, x, dx=1e-8):
        """
        Método para calcular a derivada central.
        """
        return (f(x + dx) - f(x - dx)) / (2 * dx)

    while True:
        x1 = x - f(x) / deriv_centrada(f, x)
        t = abs(x1 - x)
        if t < erro:
            break
        x = x1

    return x


def __Zero_Secante__(f, a, b, erro=1e-6):
    """
    Contribuição: Eric Naiber & Isadora Espindola

    Função para calcular os zeros de uma função a partir
    de um "chute" inicial.

    Melhor método para calcular zeros de funções, porém possui alguns
    fatores limitantes.

    Qualidade do método: ★ ★ ★ ★ ☆

    :param f: função
    :param a: chute inicial inferior
    :param b: chute inicial superior
    """

    while erro <= abs(b - a) / abs(a):
        c = (a * f(b) - b * f(a)) / (f(b) - f(a))

        if abs(c - a) < abs(b - c):
            b, a = a, c
        else:
            a, b = b, c

    return a


if __name__ == '__main__':
    print(__name__)

    def F(x):
        """
        Função de teste:
        - Resultado analítico: e³ + e
        - Resultado decimal: 22.80381

        (F, 0, 2, 200)
        """
        from math import e
        return x * e ** (x + 1)

    print(
        "Métodos para Integração",
        "-"*(len(str(__Simpson__(F, 0, 2, 200)))),
        __Simples__(F, 0, 2, 200),
        __Trapezio__(F, 0, 2, 200),
        __Simpson__(F, 0, 2, 200),
        "-"*(len(str(__Simpson__(F, 0, 2, 200)))),
        sep='\n'
    )

    def G(x):
        """
        Função de teste:
        - Primeira raiz: -1,3588989
        - Segunda raiz: 7,3588989
        """
        return -x ** 2 + 6 * x + 10

    print(
        "Métodos de f(x) = 0",
        "-"*len(str(__Zero_Bisseccao__(G, 6, 8))),
        __Zero_Bisseccao__(G, 6, 8),
        __Zero_Newton__(G, 6),
        __Zero_Secante__(G, 6, 8),
        "-" * len(str(__Zero_Bisseccao__(G, 6, 8))),
        sep='\n'
    )