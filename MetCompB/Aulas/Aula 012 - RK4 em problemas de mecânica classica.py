from numpy import sin
from matplotlib.pyplot import plot
from matplotlib.pyplot import xlabel
from matplotlib.pyplot import ylabel
from matplotlib.pyplot import title
from matplotlib.pyplot import show

"""
Sistema de Equações Diferenciais.

- Veremos como abordar equações de ordem mais alta por meio da construção de um
sistema de equações.

    du1/dt = f1(t, u1, u2, ..., um)
    du2/dt = f2(t, u1, u2, ..., um)
    ...
    dum/dt = fm(t, u1, u2, ..., um)

    para a<= t <= b.

- Podemos utilizar RK4 (Runge-Kutta 4).
Runge-Kutta 4:

    w0 = alfa

    k1 = h * f(ti, wi)
    k2 = h * f(ti + h/2, wi + 1/2 * k1)
    k3 = h * f(ti + h/2, wi + 1/2 * k2)
    k4 = h * f(t(i + 1), wi + k3)

    w(i+1) = wi + 1/6 * (k1 + k2 + k3 +k4),     i = 0, 1, 2, ..., N-1

    Para o problema:
        y' = f(t, y), a <= t <= b, y(a) = alfa

OBS: Usaremos o índice j para variável temporal e i para identificar as
equações que compõe o sistema.

        tj = a + j * h,  j = 0, 1, 2, ..., N

    Onde h = (b - a)/N
    As condições iniciais são:

        w1,0 = alfa1 | w2,0 = alfa2 | ... | wm,0 = alfam

Calculando de k1 até k4:

    k1.i = h * fi(tj, wi.j, w2.j, ..., wm.j) para i = 1, 2, ..., m

    k2.i = h * fi(tj + h/2, wi.j + 1/2 * k1.1, w2.j + 1/2 * k1.2, ..., wm.j + 1/2 * k1.m)

    k3.i = h * fi(tj + h/2, wi.j + 1/2 * k2.1, w2.j + 1/2 * k2.2, ..., wm.j + 1/2 * k2.m)

    k4.i = h * fi(tj + h, wi.j + k3.1, w2.j + k3.2, ..., wm.j + k3.m)

    Agora podemos calcular o próximo passo.

        wi.j = wi.j + 1/6 * ( k1.i + 2 * k2.i + 2 * k3.i + k4.i)


• Aplicação em Mecânica

    - No caso em que conhecemos a força e queremos determinar a trajetória de uma
    partícula, teremos um sistema com duas equações.

    OBS: Lembrando que m * d²r/dt² = Fa

        dx/dt = v

        dv/dt = F  |  dv/dt = Fr(t, x, v)/m

    Então teríamos que:

        x = u1

        v = u2

        du1/dt = f1(t, u1, u2) = u2 = v

        du2 = f2(t, u1, u2) = F(t, u1, u2) = F(t, x, v)

    Calculando os k1:

        k1.x = h * vi
        k1.v = h * F(tj, xi, vi) / m

    Para calcular os k2:

        xm = xi + 1/2 * k1.x

        vm = vi + 1/2 * k1.v

        k2.x = h * vm

        k2.v = h * F(tj + h/2, xm, vm)

    Calculando os k3:

        xm = xi + 1/2 * k2.x

        vm = vi + 1/2 * k2.v

        k3.x = h * vm

        k3.v + h * F(tj + h/2, xm, vm) / m

    Calculando os k4:

        xm = xi + k3.x

        vm = vi + k3.v

        k4.x = h * vm

        k4.v = h * F(tj + h, xm, vm)

    E finalmente, atualizamos as posições e velocidades:

        x(j+1) = xj + 1/6 * (k1.x + 2 * k2.x + 2 * k3.x + k4.x)

        v(j+1) = vj + 1/6 * (k1.v + 2 * k2.v + 2 * k3.v + k4.v)



• Exercício: Pêndulo - RK4
    Aplique o método RK4 ao problema do pêndulo. Compare com os resultados
    como o velocity-Verlet e com o RK2.
    Varie h e theta0.

    - Condições iniciais:
        theta0 = 1.5 rad, theta0' = 0, g = 10 m/s², L = 1m, h = 0.01

OBS: Não irei comparar com os outros dois métodos inidicado, o importante saber
é que o método de RK4 pode ser utilizado um h menor, afim de fazer menos cálculos
e deixar então, o código mais rápido.

OBS**: Se você não lembra a fórumla, aqui está:     (d²theta/dt²) = -g/L * sen(theta)
Caso ainda não se lembre de como abrir a fórmula volte para Aula 5.

dw/dt = - g/L * sen(theta) = a

dtheta/dt = w

"""

# Condições iniciais

X = [1.5]

v = [0]

g = 10

L = 1

h = 0.01

t = [0]

tf = 15


# Definindo a Função:

def F(x):
    return - g / L * sin(x)


# Calculando o método:

while t[-1] <= tf:
    # x inicial:

    xm = X[-1]

    # Calculando os k1:

    k1_x = v[-1] * h
    k1_v = h * F(xm)

    # Calculando os k2: xm = xi + 1/2 * k1.x | k3.x = h * vm

    xm = X[-1] + 0.5 * k1_x

    vm = v[-1] + 0.5 * k1_v

    k2_x = h * vm

    k2_v = h * F(xm)

    # Calculando os k3:

    xm = X[-1] + 0.5 * k2_x

    vm = v[-1] + 0.5 * k2_v

    k3_x = h * vm

    k3_v = h * F(xm)

    # Calculando os k4:

    xm = X[-1] + k3_x

    vm = v[-1] + k3_v

    k4_x = h * vm

    k4_v = h * F(xm)

    # Finalmente, o próximo ponto

    x_novo = X[-1] + 1 / 6 * (k1_x + 2 * k2_x + 2 * k3_x + k4_x)

    v_novo = v[-1] + 1 / 6 * (k1_v + 2 * k2_v + 2 * k3_v + k4_v)

    # Finalizando o código

    t.append(t[-1] + h)
    X.append(x_novo)
    v.append(v_novo)

plot(t, X, color='crimson')
xlabel('t')
ylabel('\u03B8(t)')
title('Runge-Kutta 4° ordem: Pêndulo.')
show()

plot(t, v, color='crimson')
xlabel('t')
ylabel('\u03C9(t)')
title('Runge-Kutta 4° ordem: Pêndulo.')
show()
