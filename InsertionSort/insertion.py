from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt


def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1, 1 * tam)
        if n not in lista: lista.append(n)
    return lista
  
def geraListaI(tam):
    lista =[]
    while tam:
      lista.append(tam)
      tam-=1
    return lista  

def insertionSort(lista):
    count = 0
    for i in range(1, len(lista)):
        x = lista[i]
        j = i-1
        while j >=0 and x<lista[j]:
            lista[j+1] = lista[j]
            j = j-1
            count += 1
        lista[j+1] = x
        
    return count
  

mpl.use('Agg')


def desenhaGrafico(x, y, y2, file_name, xl="Entradas", yl="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Lista Normal")
    ax.plot(x, y2, label="Lista Invertida")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(file_name)


x = [10000, 20000, 50000, 100000]
y = []
yI = []
tempo = []
tempoI = []
swap = []
swapI = []

for i in range(len(x)):
    y.append(geraLista(x[i]))
    yI.append(geraListaI(x[i]))

for i in range(len(x)):
    tempo.append(timeit.timeit("insertionSort({})".format(y[i]), setup="from __main__ import insertionSort", number=1))
    tempoI.append(timeit.timeit("insertionSort({})".format(yI[i]), setup="from __main__ import insertionSort", number=1))

desenhaGrafico(x, tempo, tempoI, "graphTempo.png")
    
for i in range(len(x)):
  swap.append(insertionSort(geraLista(x[i])))
  swapI.append(insertionSort(geraListaI(x[i])))  
    
desenhaGrafico(x, swap, swapI, "graphSwap.png")
