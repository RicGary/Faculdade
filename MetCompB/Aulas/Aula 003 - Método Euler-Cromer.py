import numpy as np
import matplotlib.pyplot as plt

"""
Método Euler-Cromer

- As equações diferenciais podem ser expressas como:
    dx/dt = v

    dv/dt = a(t;x;v)

    - Diferença do Euler Explícito para Euler-Crome

• Método Euler-Cromer;

    v(n+1) = vn + a(tn; xn; vn) * h
    x(n+1) = xn + v(n+1) * h

• Método Euler Explícito;

    v(n+1) = vn + a(tn; xn; vn) * h
    x(n+1) = xn + vn * h

TOMAR MUITO CUIDADO;
    - Percebe-se que a diferença está no segundo termo 'vn' e 'v(n+1)'.


OBS: Em um exercício de massa mola podemos observar que utilizando o Método Euler Explícito a energia do sistema não é
conservada, ela vai aumentando com o tempo, o que é claramente errado. No entando, utilizando Método Euler-Cromer
a energia é conservada.

"""

# Exercício: Resolver o sistema massa-mola utilizando os dois métodos.
# Verificar a conservação de energia no sistema massa-mola.

"""
Euler Explícito.

x0 = 2, v0 = 1, w0**2 = 3, h = 0.01

v(n+1) = vn + a(tn; xn; vn) h
x(n+1) = xn + vn h

dx/dt= v
dv/dt = a(t; x; v)

"""


def metodo_explicito_massa_mola(n, tf, x0=2, v0=1, w0=3, h=0.01):
    velocidade = [v0]
    deslocamento = [x0]

    t = np.linspace(0, tf, num=n + 1)

    for i in range(0, n):
        vn = v0 - w0 * x0 * h
        xn = x0 + v0 * h

        v0 = vn
        x0 = xn

        velocidade.append(v0)
        deslocamento.append(x0)

    return deslocamento, velocidade, t


explicito = metodo_explicito_massa_mola(5000, 50)

fig, axs = plt.subplots(2)

axs[0].plot(explicito[2], explicito[0], color='crimson', label='Deslocamento')
axs[0].plot(explicito[2], explicito[1], color='black', label='Velocidade')

axs[1].plot(explicito[0], explicito[1], color='orange')

plt.ylabel('d(t) ,x(t)')
plt.xlabel('t')
plt.suptitle('Sistema massa mola; Método Euler Explícito')

plt.draw()

axs[0].grid(True)
plt.grid(True)
axs[0].legend()
plt.show()

"""
Euler-Cromer.

x0 = 2, v0 = 1, w0**2 = 3, h = 0.01

v(n+1) = vn + a(tn; xn; vn) h
x(n+1) = xn + vn h

dx/dt= v
dv/dt = a(t; x; v)

"""


def metodo_cromer(n, tf, x0=2, v0=1, w0=3, h=0.01):
    velocidade = [v0]
    deslocamento = [x0]

    t = np.linspace(0, tf, num=n + 1)

    for i in range(0, n):
        vn = v0 - w0 * x0 * h
        xn = x0 + vn * h

        v0 = vn
        x0 = xn

        velocidade.append(v0)
        deslocamento.append(x0)

    return deslocamento, velocidade, t


cromer = metodo_cromer(5000, 50)

_, axs = plt.subplots(2)

axs[0].plot(cromer[2], cromer[0], color='crimson', label='Deslocamento')
axs[0].plot(cromer[2], cromer[1], color='black', label='Velocidade')

axs[1].plot(cromer[0], cromer[1], color='orange')

plt.ylabel('d(t) ,x(t)')
plt.xlabel('t')
plt.suptitle('Sistema massa mola; Método Euler Explícito')

plt.draw()

axs[0].grid(True)
plt.grid(True)
axs[0].legend()
plt.show()

"""
Conservação de energia em cada método.

(E(t) - 3.5)/3.5

1/2 * k * x0 ** 2 + 1/2 * m * v0 ** 2

E0 = 1.5 * 2 ** 2 + 0.5 = 3.5 

k = 3 ; m = 1
"""

# return deslocamento, velocidade, t

explicito = metodo_explicito_massa_mola(1000, 10)
cromer = metodo_cromer(1000, 10)

tempo = cromer[2]

# lista a função mapeada substituindo os parâmetros
# list ( map ( função , parâmetros ) )   função = (E(t) - E0)/E0          E0 = 3.5
Energia_explicito = list(map(lambda x0, v0: ((1.5 * x0 ** 2 + 0.5 * v0 ** 2) - 3.5) / 3.5, explicito[0], explicito[1]))
Energia_cromer = list(map(lambda x0, v0: ((1.5 * x0 ** 2 + 0.5 * v0 ** 2) - 3.5) / 3.5, cromer[0], cromer[1]))

plt.plot(tempo, Energia_explicito, color='crimson', label='Método Euler Explícito')
plt.plot(tempo, Energia_cromer, color='black', label='Método Euler-Cromer')
plt.xlabel('Tempo')
plt.ylabel('(E(t) - E0)/E0')
plt.title('Conservação de Energia')
plt.grid(True)
plt.legend()
plt.show()
