from random import randint
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt

def geraLista(tam):
    lista = []
    for i in range(tam):
        n = randint(1,1*tam)
        if n not in lista: lista.append(n)
    return lista

def bubbleSort(lista):
    count = 0
    if len(lista) <= 1:
        ordenado = lista
    else:
        for j in range(0,len(lista)):
            for i in range(0,len(lista)-1):
                if lista[i]>lista[i+1]:
                    aux = lista[i+1]
                    lista[i+1] = lista[i]
                    lista[i] = aux
                    count+=1
        ordenado = lista
    return count

mpl.use('Agg')
  
def desenhaGrafico(x,y,xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Quantidade de Swaps")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    fig.savefig('graph.png')
   
x2 = [10000,20000,50000,100000]
y = []
x3 = []

for i in x2:
  x3.append(geraLista(i))
  
for i in range(4):
    y.append(timeit.timeit("bubbleSort({})".format(x3[i]),setup="from __main__ import bubbleSort",number=1))  

desenhaGrafico(x2,y)