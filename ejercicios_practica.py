#!/usr/bin/env python
'''
Funciones [Python]
Ejercicios de práctica
---------------------------
Autor: Inove Coding School
Version: 1.2

Descripcion:
Programa creado para poner a prueba los conocimientos
adquiridos durante la clase
'''

__author__ = "Inove Coding School"
__email__ = "alumnos@inove.com.ar"
__version__ = "1.2"

import random


def imprimir_nombre(nombre, apellido):
    pass # --> Sacalo si no se usa :D
    # En este lugar debe colocar el "print" e imprimir
    # en pantalla el nombre y apellido que vienen por parámetro
    # print(.....)

    print("Nombre completo: {}{}".format(nombre,apellido))



def promedio(numeros):
    # Alumno:
    # 1) calcule el promedio
    # 2) use "return" para retornar ese valor
    # Cuando termine de implementar está función borrar "pass"

    """     for n in numeros:
                n += numeros
    
            promedio = n / len(numeros) """

    promedio = sum(numeros) / len(numeros)
    return promedio
    #realizado



def ordenar(numeros):
    
    numeros.sort()
    print(numeros) # Utiliza el return, y asigná el resultado a una nueva variable :D



lista_aleatoria_plus = [] # Las variables globales ponelas arriba de todo, debajo de los import y antes de las funciones.
# las variables globales generalmente van en mayusculas, tipo LISTA_ALEATORIA_PLUS :D
def lista_aleatoria(inicio,fin,cantidad,lista_aleatoria_plus):
    
    for i in range(cantidad):
        num_aleatorio = random.randrange(inicio,fin+1)
        lista_aleatoria_plus.append(num_aleatorio)
    print(lista_aleatoria_plus) # Usa return :D



def contar(lista,num):

    rep = 0
    for i in lista:
        if i == num:
            rep += 1
    print("El número {} se repite {} veces!".format(num,rep))
    # Acá también estaría bueno que uses el return así te devuelve el número de repeticiones :D


def ej1():
    print('Mi primera funcion')
    # Realice una función llamada "imprimir_nombre"
    # la cual reciba dos parámetros, el nombre y el apellido
    # Esa función ya se encuentra a medio armar al principio de este archivo.
    # Debe completar la función para que se imprima en pantalla su nombre y apellido
    # Debe invocar a la función como:
    imprimir_nombre('Nahuel','Arrascaeta')
    # Reemplazar por su nombre y apellido los textos
    #realizado



def ej2():
    # Ejercicios con funciones del sistema
    numeros = [2, 6, 4, 8, 10, 12]

    '''
    Realice una funcion llamada "promedio" la cual
    reciba como parámetro una lista de números y calcule
    el promedio de ella como:
    promedio = sumatoria_numeros / cantidad_numeros

    Resuelva la sumatoria y la cantidad con las herramientas
    que desee, recomendamos usar las funciones disponibles
    de Python para ello o en tal caso realizar un bucle.
    Puede utilizar la función "sum" y la función "len"
    sum --> obtener la sumatoria de números
    len --> obtener la cantidad de números
    promedio = sumatoria_numeros / cantidad_numeros

    La función debe retornar (return) el promedio calculado
    La función debe contemplar si se le pasa una lista vacia
    (es decir, de "0" elementos)

    Utilice esa función para calcular el promedio y luego
    imprima en pantalla el resultado

    '''
    # La función ya se encuentra definida arriba de todo en el archivo,
    # busque al princpio de todo "def promedio"
    # Ya la función fue preparada para que usted le pase "numeros"
    # como parámetro, falta que calcule el promedio y retorne el valor
    # resultante.

    # Llamar a la función en este lugar y capturar el valor del retorno
    # promedio_re
    print(promedio(numeros))
    # Luego imprimir en pantalla el valor resultante, tal que:
    #realizado



def ej3():
    # Ejercicios de listas y métodos
    numeros = [23, 2, 4444, 1, 11, 14]


    '''
    Generar una una nueva funcion que se llame "ordenar",
    que utilizaremos para odernar la lista de numeros.
    Dentro de la función puede ordenar la lista
    usando bucles o las funciones nativas de Python (sort)

    Aproveche el ejemplo de "promedio" para crear una función
    similar, la debe crear y escribir abajo de ella.
    '''

    # Luego de crear la función invocarla en este lugar:
    # lista_ordenada = ordenar(numeros)
    # Imprimir en pantalla "lista_ordenada" que tendrá
    # los valores retornado por la función ordenar
    ordenar(numeros) # Acá te decía que los retornes :D
    #realizado



def ej4():
    # Ejercicios con modulos del sistema
    inicio = 0
    fin = 10
    cantidad = 5

    # Ejemplo de como obtener un numero aleatorio
    # entre inicio y fin
    # inicio <= numero <= fin
    numero = random.randrange(inicio, fin+1)
    # Documentación oficial de random
    # https://docs.python.org/3.7/library/random.html
    # Ante cualquier duda preguntar en el campus!

    '''
    Realice una funcion llamada "lista_aleatoria" la cual
    reciba como parámetro el rango de aceptación de la lista
    "inicio y fin" y la cantidad de elementos que deseamos que
    contenga la lista, es decir, la cantidad de elementos random a generar.

    --> def lista_aleatoria (inicio, fin, cantidad)

    Para ello dentro de la función deberá realizar un bucle que repita "cantidad"
    veces esta operacion:
    numero = random.randrange(inicio, fin+1)

    Cada valor generado lo debe guardar en una lista, recuerde:
    1) Iniciar y crear esa lista vacia.
    2) Para agregar nuevos elementos en la lista utiliza "append"

    Finalmente dicha función debe retornar la lista de elementos random generados.
    '''

    # Invocar lista_aleatoria
    # mi_lista_aleatorio = lista_aleatoria(inicio, fin, cantidad)
    # print(mi_lista_aleatorio)
    
    lista_aleatoria(inicio,fin,cantidad,lista_aleatoria_plus) # Esto funciona porque la lista es GLOBAL, pero tene en cuenta una cosa:
    # ¿Qué pasa si mi variable se ve afectada por otra función mientras estoy operandola con esta función?
    # Las variables globales pueden ser accedidas por todas las funciones, entonces tenes que tener cuidado de en qué momento estas modificandola
    # con otras funciones, porque podes traer problemas en tu programa. Supone que esta variable la usas para un proceso, y antes de este proceso sin querer la modifica otra
    # función, entonces vas a estar usando la variable para tu proceso con un valor modificado accidentalmente. Ojo con eso. El ejercicio está perfecto, solo te lo comento
    # para que cuando uses esta técnica lo hagas sabiendo que eso te puede pasar. A veces es deseado (si usas la variable global como un control de estado de algo), otras no.
    print(lista_aleatoria_plus)
    #realizado



def ej5():
    # Ejercicios de listas y métodos
    cantidad_numeros = 5
    inicio = 1
    fin = 9
    '''
    Utilice la función "lista_aleatoria" para generar
    una lista de 5 números en un rango de 1 a 9 inclusive

    Generar una una nueva funcion que se llame "contar",
    que cuenta la cantidad de veces que un elemento pasado
    por parámetro se repite en la lista.
    Para saber cuantas veces se repiten el elemento pasado
    en la lista pueden usar bucles o el método nativo de list
    "count"
    '''
    lista_aleatoria(inicio,fin,cantidad_numeros,lista_aleatoria_plus)

    # Por ejemplo creo una lista de 5 elemtnos
    # lista_numeros = lista_aleatoria(...,...,cantidad_numeros)
    # Luego quiero averiguar cuantas veces se repite el numero 3
    # cantidad_tres = contar(lista_numeros, 3)
    contar(lista_aleatoria_plus,3)
    #realizado


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    # ej1()
    # ej2()
    # ej3()
    # ej4()
    # ej5()
