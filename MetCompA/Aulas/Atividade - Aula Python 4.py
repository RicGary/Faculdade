"""
Equação.

v(t) = - vterm ( 1 - exp ( - t/tao ) )

t - de 0.5 e 0.5 até 10.

vterm = 20 m/s
y(0) = 150m
tao = 5s

"""
from numpy import exp

# Variáveis
vterm = 20
y0 = 150
tao = 5


deslocamento_dados = []
aceleracao_dados = []
tempo_dados = []

t = 0
for i in range(21):

    y = y0 - vterm * t - tao * (vterm * exp(- t/tao ))

    a = (- vterm * exp(- t/tao )) / tao

    deslocamento_dados.append(y)
    aceleracao_dados.append(a)
    tempo_dados.append(t)

    t += 0.5


print(deslocamento_dados)
print('-='*10)
print(aceleracao_dados)
print('-='*10)
print(tempo_dados)
