def promedio(numeros):
    sumatoria = 0
    for i in numeros:
        sumatoria = sumatoria + i
    
    prom = sumatoria / len(numeros)
    return prom
print ("El promedio es:", promedio([50,10,50,50]))


import random

def lista_aleatoria(inicio, fin, cantidad):
    lista = []
    for i in range (0,15):
        i = lista
        mi_lista = random.randrange(start= 0, stop= 15)
        return mi_lista

print("Aqui esta el listado en forma aleatoria:\n", lista_aleatoria(inicio=0, fin=10, cantidad=5))

import random

a = [1,2,3,4,5,6,7,8,9,10,11]

for i in a:
    a = random.randrange(start= 0, stop=11, step = 2)
    i = a
    print (i)






