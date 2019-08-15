from random import randint
from random import shuffle
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
  
def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista


def mergeSort(lista): 
    if len(lista) >1: 
        meio = len(lista)//2  
        E = lista[:meio]   
        D = lista[meio:] 
  
        mergeSort(E)  
        mergeSort(D)  
  
        i = j = k = 0

        while i < len(E) and j < len(D): 
            if E[i] < D[j]: 
                lista[k] = E[i] 
                i+=1
            else: 
                lista[k] = D[j] 
                j+=1
            k+=1    
          
        while i < len(E): 
            lista[k] = E[i] 
            i+=1
            k+=1
          
        while j < len(D): 
            lista[k] = D[j] 
            j+=1
            k+=1

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
    tempo.append(timeit.timeit("mergeSort({})".format(y[i]), setup="from __main__ import mergeSort",number=1))

desenhaGrafico(x, tempo, "graphTempo.png")