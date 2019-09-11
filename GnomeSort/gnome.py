from random import randint
from random import shuffle
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
 
mpl.use('Agg')  

def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista
 
def gnomeSort(lista):
    tam = len(lista)
    x = 0
    while x < tam:
        if x == 0:
            x = x + 1
        if lista[x] >= lista[x - 1]:
            x = x + 1
        else:
            aux = lista[x]
            lista[x] = lista[x-1]
            lista[x-1] = aux
            x = x - 1
    return lista

def desenhaGrafico(x, y, file_name, xl="Entradas", yl="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(file_name)

x = [10000, 20000, 40000, 50000, 100000, 200000]
y = []
tempo = []

for i in range(len(x)):
    y.append(geraLista(x[i]))

for i in range(len(x)):
    tempo.append(timeit.timeit("gnomeSort({})".format(y[i]), setup="from __main__ import gnomeSort",number=1))

desenhaGrafico(x, tempo, "graphTempo.png")