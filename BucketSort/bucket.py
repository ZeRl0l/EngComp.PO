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

def bucketSort(lista):

    def quickSort(lista, st, end):
        if st < end:
            aux = randint(st, end)
            x = lista[end]
            lista[end] = lista[aux]
            lista[aux] = x

            p = partition(lista, st, end)
            quickSort(lista, st, p - 1)
            quickSort(lista, p + 1, end)

        return lista

    def partition(lista, st, end):
        aux = randint(st, end)

        lista[end], lista[aux] = lista[aux], lista[end]

        aux_index = st - 1
        for index in range(st, end):
            if lista[index] < lista[end]:
                aux_index = aux_index + 1
                lista[aux_index], lista[index] = lista[index], lista[aux_index]

        x = lista[aux_index + 1]
        lista[aux_index + 1] = lista[end]
        lista[end] = x

        return aux_index + 1

    maior = max(lista)

    tam = len(lista)

    size = maior/tam

    bucket = [[] for _ in range(tam)]

    for i in range(tam):
        j = int(lista[i]/size)
        if j != tam:
            bucket[j].append(lista[i])
        else:
            bucket[tam - 1].append(lista[i])

    for i in range(tam):
        quickSort(bucket[i],0,len(bucket[i])-1)

    result = []

    for i in range(tam):
        result = result + bucket[i]

    return result

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
    tempo.append(timeit.timeit("bucketSort({})".format(y[i]), setup="from __main__ import bucketSort",number=1))

desenhaGrafico(x, tempo, "graphTempo.png")
