import numpy as np
import matplotlib.pyplot as plt
import imageio


class PhiCalc:

    def __init__(self, n, L):
        self.X = np.linspace(0, L, num=100)
        self.n = n
        self.phi = np.sin(np.pi * self.n * self.X)


def ProbDensity(t, phi_1, phi_2, sinal=1, sinal2=1):
    h = 1.05e-34
    m = 9.1e-31
    w = h * (np.pi ** 2) / (2 * m)

    conjugado = (phi_1 * np.exp(1j * w * t) + sinal * sinal2 * phi_2 * np.exp(4j * w * t))
    normal = (phi_1 * np.exp(-1j * w * t) + sinal * phi_2 * np.exp(-4j * w * t))

    return conjugado * normal


def toGif(timeList, phi1, phi2, gifName, sinal=1, sinal2=1, ylabel='|\u03A8(x,t)|²'):

    filenames = []

    for i, t in enumerate(timeList):
        Y = ProbDensity(t, phi1, phi2, sinal, sinal2)
        plt.plot(X, Y)
        plt.xlabel('X')
        plt.ylabel(ylabel)
        plt.xlim((0, 1))
        plt.ylim((0, 3.5))
        plt.savefig(f'./Imagens_ATE2_a/{i}.png')
        plt.cla()
        filenames.append(f'./Imagens_ATE2_a/{i}.png')

    with imageio.get_writer(f'{gifName}.gif', mode='I') as writer:
        for file in filenames:
            image = imageio.imread(file)
            writer.append_data(image)

    print("Finalizado.")


Phi_1a = PhiCalc(n=1, L=1).phi
Phi_2a = PhiCalc(n=2, L=1).phi

X = np.linspace(0, 1, num=100)

T = np.linspace(0, 10000, num=100)


def ExPart1():
    toGif(T, Phi_1a, Phi_2a, 'Gif 1.a', sinal=1)
    toGif(T, Phi_1a, Phi_2a, 'Gif 1.b', sinal=-1)
    toGif(T, Phi_1a, Phi_2a, 'Gid 1.c', sinal=1j, sinal2=-1)


def meanX1(t):
    h = 1.05e-34
    m = 9.1e-31
    w = h * (np.pi ** 2) / (2 * m)
    return 1/2 - (16/(9*np.pi**2)) * np.cos(3 * w * t)


def meanX3(t):
    h = 1.05e-34
    m = 9.1e-31
    w = h * (np.pi ** 2) / (2 * m)
    return 2/4 + (8j/(9 * np.pi ** 2)) * (np.exp(-3j * w * t) - np.exp(3j * w * t))


plt.plot(T, meanX1(T))
plt.title('<x>(t) para função 1')
plt.show()

plt.plot(T, meanX3(T))
plt.title('<x>(t) para função 3')
plt.show()