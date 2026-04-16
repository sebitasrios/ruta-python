###
# 03 - listas
# secuencia notables de elementos
# pueden contener elementos de diferentes tipos.
###

from os import system

if system("clear") != 0:
    system("cls")

# creacion de listas
print("\ncrear listas")
lista1 = [1, 2, 3, 4, 5]  # lista de enteros
lista2 = ["manzanas", "peras", "platanos"]  # lsita de cadenas
lista3 = [1, "hola", 3.14, True]  # lista de tipos mixtos

lista_vacia = []
lista_de_listas = [[1, 2], [3, 4]]
matrix = [[1, 2], [2, 3], [4, 5]]

print(lista1)
print(lista2)
print(lista3)
print(lista_vacia)
print(lista_de_listas)
print(matrix)

# Acceso a elementos por indiceprint("\nacceso a elementos por indice")
print(lista2[0])  # manzanas
print(lista2[1])  # peras
print(lista2[-1])  # platanos (envia datos al reves de la lista)
print(lista2[-2])  # peras (envia el dato peniultimo de la lsita)

print(lista_de_listas[1][0])

# slicing(rebanado de listas)
lista1 = [1, 2, 3, 4, 5]
print(lista1[1:4])  # slicing [2, 3, 4]
print(lista1[:3])  # slicing [1, 2, 3]
print(lista1[3:])  # [4, 5]
print(lista1[:])  # copia exacta

# hay mas magia
# print(lista1[desde:hasta:paso])

lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista1[::2])  # indices pares
print(lista1[::-1])  # para devocler indices inversos

# modificar una lista
lista1[0] = 20
print(lista1)

# añadir elementos auna lista
lista1 = [1, 2, 3]

# forma larga y menos eficiente
lista1 = lista1 + [4, 5, 6]
print(lista1)

# forma corta y mas eficiente
lista1 += [7, 8, 9]
print(lista1)

# recuperar longitud de una lista
print("longitud de la lista es", len(lista1))


###
# EJERCICIOS
###

# Ejercicio 1: El mensaje secreto
# Dada la siguiente lista:
# mensaje = ["C", "o", "d", "i", "g", "o", " ", "s", "e", "c", "r", "e", "t", "o"]
# Utilizando slicing y concatenación, crea una nueva lista que contenga solo el mensaje "secreto".

lista_mensaje = ["C", "o", "d", "i", "g", "o", "", "s", "e", "c", "r", "e", "t", "o"]
nueva_lista = " ".join(lista_mensaje)
print(nueva_lista)


# Ejercicio 2: Intercambio de posiciones
# Dada la siguiente lista:
# numeros = [10, 20, 30, 40, 50]
# Intercambia la primera y la última posición utilizando solo asignación por índice.

lista_numeros_ejercicio = [10, 20, 30, 40, 50]
lista_numeros_ejercicio[0] = 50
lista_numeros_ejercicio[4] = 10
print(lista_numeros_ejercicio)

# solucion mejor
# numeros = [10, 20, 30, 40, 50]
# numeros[0], numeros[-1] = numeros[-1], numeros[0] # Intercambio en una sola línea.
# print(numeros)


# Ejercicio 3: El sándwich de listas
# Dadas las siguientes listas:
# pan = ["pan arriba"]
# ingredientes = ["jamón", "queso", "tomate"]
# pan_abajo = ["pan abajo"]
# Crea una lista llamada sandwich que contenga el pan de arriba, los ingredientes y el pan de abajo, en ese orden.

lista_pan = ["pan arriba"]
lista_ingredientes = ["jamon", "queso", "tomate"]
lista_pan_abajo = ["pan abajo"]
lista_sandwich = lista_pan + lista_ingredientes + lista_pan_abajo
print(lista_sandwich)

# Ejercicio 4: Duplicando la lista
# Dada una lista:
# lista = [1, 2, 3]
# Crea una nueva lista que contenga los elementos de la lista original duplicados.
# Ejemplo: [1, 2, 3] -> [1, 2, 3, 1, 2, 3]

list_copia = [1, 2, 3]
list_copia += [1, 2, 3]
print(list_copia)


# Ejercicio 5: Extrayendo el centro
# Dada una lista con un número impar de elementos, extrae el elemento que se encuentra en el centro de la lista utilizando slicing.
# Ejemplo: lista = [10, 20, 30, 40, 50] -> El centro es 30

lista_centro = [10, 20, 30, 40, 50]
print(lista_centro[2])

# lista = [10, 20, 30, 40, 50]
# centro = len(lista) // 2
# print(lista[centro])

# Ejercicio 6: Reversa parcial
# Dada una lista, invierte solo la primera mitad de la lista (utilizando slicing y concatenación).
# Ejemplo: lista = [1, 2, 3, 4, 5, 6] -> Resultado: [3, 2, 1, 4, 5, 6]

lista_ordenada = [1, 2, 3, 4, 5, 6]
nueva_lista = lista_ordenada[:3]
print(nueva_lista[::-1])
print(nueva_lista[::-1] + lista_ordenada[3:])
