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
 
def heapify(lista, n, i): 
    maior = i
    e = 2 * i + 1     
    d = 2 * i + 2     

    if e < n and lista[i] < lista[e]: 
        maior = e 
 
    if d < n and lista[maior] < lista[d]: 
        maior = d 
  

    if maior != i: 
        lista[i],lista[maior] = lista[maior],lista[i] 
  
        heapify(lista, n, maior) 
  
def heapSort(lista): 
    n = len(lista) 
  
    for i in range(n, -1, -1): 
        heapify(lista, n, i) 
  
    for i in range(n-1, 0, -1): 
        lista[i], lista[0] = lista[0], lista[i] 
        heapify(lista, i, 0) 

def desenhaGrafico(x, y, file_name, xl="Entradas", yl="Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x, y, label="Melhor Tempo")
    ax.legend(bbox_to_anchor=(1, 1), bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig(file_name)

x = [100000, 200000, 400000, 500000, 1000000, 2000000]
y = []
tempo = []

for i in range(len(x)):
    y.append(geraLista(x[i]))

for i in range(len(x)):
    tempo.append(timeit.timeit("heapSort({})".format(y[i]), setup="from __main__ import heapSort",number=1))

desenhaGrafico(x, tempo, "graphTempo.png")