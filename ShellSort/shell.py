from random import randint
from random import shuffle
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
  
def geraLista(tam):
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista
    
def shellSort(lista): 
 
    n = len(lista) 
    intervalo = n//2

    while intervalo > 0: 
  
        for i in range(intervalo,n): 
  
            aux = lista[i] 
  
            j = i 
            while  j >= intervalo and lista[j-intervalo] >aux: 
                lista[j] = lista[j-intervalo] 
                j -= intervalo 
  
            lista[j] = aux 
        intervalo //= 2

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
    tempo.append(timeit.timeit("shellSort({})".format(y[i]), setup="from __main__ import shellSort",number=1))

desenhaGrafico(x, tempo, "graphTempo.png")