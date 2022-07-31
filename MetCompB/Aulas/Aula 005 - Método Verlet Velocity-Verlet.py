"""
Método de Verlet.

• Ótima para simulações de Ragdoll em jogos.
• Funciona apenas para derivadas de segunda-ordem.

Prós:
- Não é tão lenta quanto o Euler-Cromer.
- É muito mais estável quando utiliza-se várias interações.

Contras:
- Não é tão precisa.

Temos a seguinte expressão;

    x(n+1) = 2xn - x(n-1) + a(tn; xn; vn) * h ** 2

    vn = ( x(n+1) - x(n-1) )/2*h


Resolvendo problema de Pêndulo

    (d²theta/dt²) = -g/L * sen(theta)

• Abrindo a derivada ficamos com;

    d_theta/dt = w

    dw/dt = -g/L * sen(theta)

• Constantes do problema;
    
    theta0 = 1.5 ;w0 = 0 ;g = 10 ;L = 1 ;h = 0.01

"""
import numpy as np
import matplotlib.pyplot as plt


# Método de Euler-Cromer

g = 10
L = 1
h = 0.01
tf = 10

x = [1.5]
v = [0]

t = [0]

i = 0

while t[-1] <= tf:
    a = -(g / L) * np.sin(x[i])

    vn = v[i] + a * h
    xn = x[i] + vn * h

    x.append(xn)
    v.append(vn)
    t.append(t[-1] + h)

    i = i + 1

print(len(t))

plt.plot(t, x, label='Euler-Cromer', color = 'blue')
x = [x[i] for i in range(0,1002,10)]
t = [t[i] for i in range(0,1002,10)]
plt.plot(t, x, '.', color = 'blue', markersize = '14')
plt.plot(t, x, '.', color = 'white', markersize = '10')
# Método Euler Explícito

"""
vn = v[i] + a * h
xn = x[i] + vn * h
"""
g = 10
L = 1
h = 0.01
tf = 10

x = [1.5]
v = [0]

t = [0]

i = 0

while t[-1] <= tf:
    a = -g / L * np.sin(x[i])

    # Velocity-Verlet

    vn = v[i] + a * h
    xn = x[i] + v[i] * h

    t.append(t[i] + h)
    x.append(xn)
    v.append(vn)

    i = 1 + i

plt.plot(t, x, label='Euler Explícito', color='black')

# Método de Verlet
# Constantes

g = 10
L = 1
h = 0.01
tf = 10

# Condições iniciais

x = [1.5]
v = [0]

# Tempo

t = [0]

"""
• Utilizaremos pra Verlet;

    x(n+1) = 2xn - x(n-1) + a(tn; xn; vn) * h ** 2
    vn = ( x(n+1) - x(n-1) )/2*h
    
"""
i = 0
while t[-1] <= tf:

    # Precisamos calcular x(n+1), usaremos Euler-Cromer
    # Refazer sem Euler-Cromer

    if t[i] == 0:
        a = -(g / L) * np.sin(x[i])
        """
        v(n+1) = vn + a(tn; xn; vn) h
        x(n+1) = xn + vn h
        """
        vn = v[i] + a * h
        xn = x[i] + vn * h

    # Agora usaremos o método de Verlet
    else:
        a = -(g / L) * np.sin(x[i])
        """
        x(n+1) = 2xn - x(n-1) + a(tn; xn; vn) * h ** 2
        vn = ( x(n+1) - x(n-1) )/2*h
        """
        xn = 2 * x[i] - x[i - 1] + a * h ** 2
        vn = (xn - x[i - 1]) / 2 * h

    """
    Na hora de fazer append iremos converter o valor de rad para graus.
        pi rad = 180
     theta rad = xn
     
     theta rad = xn * pi rad / 180
    """

    x.append(xn)
    t.append(t[-1] + h)

    i = i + 1

plt.plot(t, x, label='Método de Verlet', color='crimson')
plt.title('Comparação de Métodos: Problema Pêndulo Simples')
plt.xlabel('Tempo (s)')
plt.ylabel(r'${\theta}$ - Theta(rad)')
#plt.grid()
plt.legend()
plt.show()