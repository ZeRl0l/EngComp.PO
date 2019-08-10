from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
  
def geraListaI(size):
    lista = list(range(1, size + 1))
    return lista[::-1]

def partition(lista, st, end):
    i = (st - 1)
    x = lista[end]

    for j in range(st, end):
        if lista[j] <= x:
            i = i + 1
            lista[i], lista[j] = lista[j], lista[i]

    lista[i + 1], lista[end] = lista[end], lista[i + 1]
    return (i + 1)


def quickSort(lista, st, end):
    size = end - st + 1
    pilha = [0] * (size)

    topo = -1

    topo = topo + 1
    pilha[topo] = st
    topo = topo + 1
    pilha[topo] = end

    while topo >= 0:

        end = pilha[topo]
        topo = topo - 1
        st = pilha[topo]
        topo = topo - 1

        x = partition(lista, st, end)

        if x - 1 > st:
            topo = topo + 1
            pilha[topo] = st
            topo = topo + 1
            pilha[topo] = x - 1

        if x + 1 < end:
            topo = topo + 1
            pilha[topo] = x + 1
            topo = topo + 1
            pilha[topo] = end

def QSort(lista):
    quickSort(lista, 0, len(lista)-1)

def desenhaGrafico(x, y, file_name, xl="Entradas", yl="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(file_name)


x = [100000, 200000, 300000, 400000, 500000, 1000000, 2000000]
yI = []
tempoI = []


for i in range(len(x)):
    yI.append(geraListaI(x[i]))

for i in range(len(x)):
    tempoI.append(timeit.timeit("QSort({})".format(yI[i]), setup="from __main__ import QSort",number=1))

desenhaGrafico(x, tempoI, "graphTempo.png")