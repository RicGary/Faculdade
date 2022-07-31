import matplotlib.pyplot as plt

"""

Método de Runge-Kutta
Tabela de Butcher


    - Consiste em encontrar um ponto inicial "k1" e uma inclinação em um passo intermediário "k2",
    com essa inclinação damos o passo real.

    - Podemos calcular equações de 2 ordem até 4 ordem.

OBS: Se o problema for uma derivada de 2 ordem, teremos 2 passos intermediários ("k1" e "k2)


• Método de 2 ordem:

    - dx/dt = f(t,x)

    - k1 = f(tn, xn)

    - k2 = f(tn + h/2, xn + h/2)

    - x(n+1) = xn + h * k2

ou também;

    - x(n+1) = xn + 1/valor [k1 + k2] * h

• Método de 4 ordem:

    - x(n+1) = xn + 1/valor [k1 + k2 + k3 + k4] * h

Onde cada kn tem uma etapa diferente.
O "valor" depende do métodos que será utilizado.


    • Para escolher o método utilizado deveremos observar a lista de Métodos Runge-Kutta, ou também conhecido como:
TABELAS DE BUTCHER.


"""
"""
    • Método de Runge-Kutta 2 Ordem;
    
Modelo SIR: 3 variáveis.

--------------------
dS/dt = fS(S, I, R)

dI/dt = fI(S, I, R)

dR/dt = fR(S, I, R)
--------------------
k1S = fS(Sn, In, Rn)

k1I = fI(Sn, In, Rn)

k1R = fR(Sn, In, Rn)
---------------------------------------------------------
k2S = fS(Sn + k1S * h/2, In + k1S * h/2, Rn + k1S * h/2)

k2I = fI(Sn + k1S * h/2, In + k1S * h/2, Rn + k1S * h/2)

k2R = fR(Sn + k1S * h/2, In + k1S * h/2, Rn + k1S * h/2)
---------------------------------------------------------
S(n+1) = Sn + k2S

I(n+1) = In + k2I

R(n+1) = Rn + k2R
-----------------

N = 100
I0 = 1
R0 = 0
S0 = 99
gamma = 0.50

Testar os dois Beta;
B = 10  B = 1.2
"""

tf = 20

N = 100
I0 = 1
R0 = 0
S0 = 99
gamma = 0.50


# ╔════════════════════╗
# ║Funções Modelo S.I.R║
# ╚════════════════════╝

def fS(S, I, R, B):
    return (-B * S * I) / N


def fI(S, I, R, B):
    return (B * S * I / N) - (gamma * I)


def fR(S, I, R, B):
    return gamma * I


# ╔══════════════════════════════╗
# ║Método Runge-Kutta 3 Variáveis║
# ╚══════════════════════════════╝

def runge_kutta(S, I, R, B, h=1e-2):
    s = [S]
    i = [I]
    r = [R]
    t = [0]

    n = -1
    while t[-1] <= tf:
        # Calcular k1: k1S = fS(Sn, In, Rn)

        k1_S = fS(s[n], i[n], r[n], B)
        k1_I = fI(s[n], i[n], r[n], B)
        k1_R = fR(s[n], i[n], r[n], B)

        # Calcular o S interediário: Sint = Sn + k1S

        Sint = s[n] + k1_S * h / 2
        Iint = i[n] + k1_I * h / 2
        Rint = r[n] + k1_R * h / 2

        # Calcular k2: k2S = fS(Sint + k1S * h/2, Iint + k1S * h/2, Rint + k1S * h/2)

        k2_S = fS(Sint + k1_S * h / 2, Iint + k1_I * h / 2, Rint + k1_R * h / 2, B)
        k2_I = fI(Sint + k1_S * h / 2, Iint + k1_I * h / 2, Rint + k1_R * h / 2, B)
        k2_R = fR(Sint + k1_S * h / 2, Iint + k1_I * h / 2, Rint + k1_R * h / 2, B)

        # Calcular S(n+1): S(n+1) = Sn + k2S

        S_1 = s[n] + k2_S * h / 2
        I_1 = i[n] + k2_I * h / 2
        R_1 = r[n] + k2_R * h / 2

        s.append(S_1)
        i.append(I_1)
        r.append(R_1)

        t.append(t[-1] + h)

    return s, i, r, t

# B = 10

Ss = runge_kutta(99, 1, 0, 10)[0]
Ii = runge_kutta(99, 1, 0, 10)[1]
Rr = runge_kutta(99, 1, 0, 10)[2]
Tt = runge_kutta(99, 1, 0, 10)[3]

plt.plot(Tt, Ss, color="orange", label="Suscetíveis")
plt.plot(Tt, Ii, color="crimson", label="Infectados")
plt.plot(Tt, Rr, color="seagreen", label="Recuperados")

plt.xlabel("Tempo")
plt.suptitle("Modelo Epidêmico: S.I.R")
plt.title("Sem isolamento social.", x = 0.485, size='medium')
plt.legend()
plt.show()

# B = 1.2

Ss = runge_kutta(99, 1, 0, 1.2)[0]
Ii = runge_kutta(99, 1, 0, 1.2)[1]
Rr = runge_kutta(99, 1, 0, 1.2)[2]
Tt = runge_kutta(99, 1, 0, 1.2)[3]

plt.plot(Tt, Ss, color="orange", label="Suscetíveis")
plt.plot(Tt, Ii, color="crimson", label="Infectados")
plt.plot(Tt, Rr, color="seagreen", label="Recuperados")

plt.xlabel("Tempo")
plt.suptitle("Modelo Epidêmico: S.I.R")
plt.title("Com isolamento social.", x = 0.485, size='medium')
plt.legend()
plt.show()