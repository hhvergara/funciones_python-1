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
    print ("Mi nombe es:", nombre, apellido, "\n")

imprimir_nombre(nombre='Francisco', apellido='Perez Chada') # Esto quedó fuera de la función y también está
# Fuera de la función principal main, recorda que las sentencias que queden fuera de las funciones, deben estar
# dentro de la función principal, para evitar comportamientos no deseados :D


# En este lugar debe colocar el "print" e imprimir
    # en pantalla el nombre y apellido que vienen por parámetro
    # print(.....)


def promedio(numeros):
    numeros = range(10) # OJO acá estas sobrescribiendo la variable con el metodo range!
    print('El rango de numeros elegido es:',numeros,"\n")
    sumatoria = sum(numeros)
    print("La sumatoria del rango elegido es:", sumatoria,"\n")
    q_numeros = float(len(numeros))
    print ("la cantidad de numeros para obtener", q_numeros,"\n")
    operacion = sumatoria / q_numeros
    print ( "El promedio es:", operacion,"\n")
    # Tenes que usar el return para devolver el valor al hilo principal :D

promedio(numeros = 5 )

print ("_______________________________________________\n")


    # Alumno:
    # 1) calcule el promedio
    # 2) use "return" para retornar ese valor
    # Cuando termine de implementar está función borrar "pass"


def ej1():
    print('Mi primera funcion \n')
    def imprimir_nombre2(mi_nombre, mi_apellido):
        nombre_2 = str(mi_nombre) + str(mi_apellido)
        return nombre_2

    nombre_completo = imprimir_nombre2(mi_nombre= "Francisco Javier", mi_apellido = " Perez Chada \n")
    print("Mi nombre completo es:", nombre_completo)
    # Excelente! usas funciones anidadas! :D
# Realice una función llamada "imprimir_nombre"
    # la cual reciba dos parámetros, el nombre y el apellido
    # Esa función ya se encuentra a medio armar al principio de este archivo.
    # Debe cumpletar la función para que se imprima en pantalla su nombre y apellido
    # Debe invocar a la función como:
    # Reemplazar por su nombre y apellido los textos


def ej2():
    print('Ejercicio 2 \n')

    def promedio2(numeros):
        sumatoria = 0
        cantidad_num = 0
        for i in numeros:
            sumatoria = sumatoria + i
            cantidad_num = cantidad_num + 1

        operacion2 = sumatoria / cantidad_num
        return operacion2

    print ("El promedio es:", promedio2([48,12],),"\n")

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

    # Luego imprimir en pantalla el valor resultante, tal que:


def ej3():
    print("Ejercicio 3:\n")
    # Ejercicios de listas y métodos
    
    def ordenar (numeros):
        sumatoria = 0
        for i in numeros:
            sumatoria = sumatoria + i
        
        op_ordenar= sorted(numeros)
        return op_ordenar

    print("Lista ordenada de los siguientes numeros:", ordenar([9,3,1,2,6,10,7,4,8,2]),"\n")
        



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


def ej4():
    print("Ejercicio 4:\n")
    # Ejercicios con modulos del sistema    
    # Ejemplo de como obtener un numero aleatorio
    # entre inicio y fin
    # inicio <= numero <= fin
    #numero = random.randrange(inicio, fin+1)
    # Documentación oficial de random
    # https://docs.python.org/3.7/library/random.html
    # Ante cualquier duda preguntar en el campus!

    import random # Por convención se ponen los import al inicio del programa ;D
    
    def lista_aleatoria(inicio, fin, cantidad):
        list_a = []
        for i in range (cantidad):
            numero = random.randrange(inicio, fin+1)
            list_a.append(numero)
        return list_a

    mi_lista = lista_aleatoria(inicio= 1, fin=10, cantidad=5)
    print("El listado aleatorio de la lista es:", mi_lista, "\n")

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


def ej5():
    # Ejercicios de listas y métodos
    print("Ejercicio 5 \n")


    import random # Idem al punto 4 ;D
    
    def lista_aleatoria(inicio, fin, cantidad):
        list_a = []
        for i in range (cantidad):
            numero = random.randrange(inicio, fin+1)
            list_a.append(numero)
        return list_a

    mi_lista = lista_aleatoria(inicio= 1, fin=10, cantidad=5)
    contar = mi_lista.count(3)
    print("El listado aleatorio de la lista es:", mi_lista, "\n")
    print ("El contador nos indica que el numero 3 esta repetido:", contar, "vez / veces \n")
    
    # NOTE: La lista_aleatoria() la podrías definir afuera del ej4() de manera que la puedas reutilizar en el ej5()

    '''
    Utilice la función "lista_aleatoria" para generar
    una lista de 5 números en un rango de 1 a 9 inclusive

    Generar una una nueva funcion que se llame "contar",'
    que cuenta la cantidad de veces que un elemento pasado
    por parámetro se repite en la lista.
    Para saber cuantas veces se repiten el elemento pasado
    en la lista pueden usar bucles o el método nativo de list
    "count"

    '''

    # Por ejemplo creo una lista de 5 elemtnos
    # lista_numeros = lista_aleatoria(...,...,cantidad_numeros)
    # Luego quiero averiguar cuantas veces se repite el numero 3
    # cantidad_tres = contar(lista_numeros, 3)





if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python \n")
    ej1()
    ej2()
    ej3()
    ej4()
    ej5()
