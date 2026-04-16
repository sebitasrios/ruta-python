####
# 04- listas metodos
# los metodos mas importantes para trabajar con listas
###

from os import system

if system("clear") != 0:
    system("cls")

lista1 = ["a", "b", "c", "d"]

# esto añade un elemento al final
lista1.append("e")  # añade un elemento al final, pero solo un parametroacepta el metodo
print(lista1)

# pero si quiero insertar en cualquier lugar
lista1.insert(1, "@")  # inserta un elemento en la
# posicion que le indiquemos como primer argumento
print(lista1)

# añade varios elementos
lista1.extend(["s", "f"])  # agrega elementos al final de la lista
print(lista1)


# eliminar elementos de la lista(conociendo el elemto dentrosde la lista)
lista1.remove("@")  # eliminar la primera aparicion de la cadena de texto
print(lista1)

# eliminar el ultimo elemento de la lista y ademas te lo devuelve
ultimo = lista1.pop()  # eliminar el ultimo elemento
print(ultimo)
print(lista1)

lista1.pop(1)  # elimina el segundo elemento de la lista con el indice
# es el indice 1
print(lista1)

# eliminar por lo bestia
del lista1[-1]
print(lista1)

lista1.clear()  # eliminar todos los elementos de la lista
print(lista1)

# eliminar un rango de elemento
lista1 = ["cat", "dog", "bear", "elefanth"]
del lista1[2:]
print(lista1)

# mas metodos utiles
print("ordenar listas modificando la original")
numbers = [3, 10, 2, 8, 99, 101]
numbers.sort()
print(numbers)
sorted_numbers = sorted(numbers)
print(sorted_numbers)
print(numbers)

print("ordenar listas con cadenas de textos todo en minuscula")
frutas = ["manzana", "pera", "limon", "manzana", "pera", "limon"]
sorted_frutas = sorted(frutas)
print(sorted_frutas)

print(
    "ordenar listas con cadenas de textos (mezaclas mayusculas y minusculas)"
)  # primero solo asigna las mayusculas y luego minusculas
frutas = ["manzana", "Pera", "Limon", "manzana", "pera", "limon"]
sorted_frutas = sorted(frutas)
print(sorted_frutas)
frutas.sort(key=str.lower)
print(frutas)

# mas metodos utiles
animals = ["dog", "cat", "dog", "gato"]
print(len(animals))  # tamaño de la lista
print(animals.count("dog"))  # cuantas veces aparece el elemento
print("gato" in animals)  # valida si hay ese elemnto en la lista
print("roy" in animals)  # valida si hay ese elemnto en la lista


###
# EJERCICIOS
# Usa siempre que puedas los métodos que has aprendido
###

# Ejercicio 1: Añadir y modificar elementos
# Crea una lista con los números del 1 al 5.
# Añade el número 6 al final usando append().
# Inserta el número 10 en la posición 2 usando insert().
# Modifica el primer elemento de la lista para que sea 0.

lista_numeros = [1, 2, 3, 4, 5]
lista_numeros.append(6)
print(lista_numeros)
lista_numeros.insert(2, 10)
print(lista_numeros)
lista_numeros.pop(0)
lista_numeros.insert(0, 0)
print(lista_numeros)

##correcion
# modificacion del primer elemento
# lista_numeros [0] = 0 mas eficaz


# Ejercicio 2: Combinar y limpiar listas
# Crea dos listas:
# lista_a = [1, 2, 3]
# lista_b = [4, 5, 6, 1, 2]
# Extiende lista_a con lista_b usando extend().
# Elimina la primera aparición del número 1 en lista_a usando remove().
# Elimina el elemento en el índice 3 de lista_a usando pop(). Imprime el elemento eliminado.
# Limpia completamente lista_b usando clear().

lista_a = [1, 2, 3]
lista_b = [4, 5, 6, 1, 2]
lista_a.extend(lista_b)
print(lista_a)
lista_a.remove(1)
print(lista_a)
elemento_eliminado = lista_a.pop(3)
print(elemento_eliminado)
lista_b.clear()
print(lista_b)

# Ejercicio 3: Slicing y eliminación con del
# Crea una lista con los números del 1 al 10.
# Utiliza slicing y del para eliminar los elementos desde el índice 2 hasta el 5 (sin incluir el 5).
# Imprime la lista resultante.

list_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
del list_numbers[2:5]
print(list_numbers)


# Ejercicio 4: Ordenar y contar
# Crea una lista con los siguientes números: [5, 2, 8, 1, 9, 4, 2].
# Ordena la lista de forma ascendente usando sort().
# Cuenta cuántas veces aparece el número 2 en la lista usando count().
# Comprueba si el número 7 está en la lista usando in.

list_des = [5, 2, 8, 1, 9, 4, 2]
list_des.sort()
print(list_des)
print(len(list_des))
print(list_des.count(2))
print(7 in list_des)


# Ejercicio 5: Copia vs. Referencia
# Crea una lista llamada original con los números [1, 2, 3].
# Crea una copia de la lista original llamada copia_1 usando slicing.
# Crea otra copia llamada copia_2 usando copy().
# Crea una referencia a la lista original llamada referencia.
# Modifica el primer elemento de la lista referencia a 10.
# Imprime las cuatro listas (original, copia_1, copia_2, referencia) y observa los cambios.

original = [1, 2, 3]
print(original)
copia1 = original[:]
print(copia1)
copia2 = original.copy()
print(copia2)
referencia = original
print(referencia)
referencia.pop(0)
referencia.insert(0, 10)
print(original, copia1, copia2, referencia)


# Ejercicio 6: Ordenar strings sin diferenciar mayúsculas y minúsculas.
# Crea una lista con las siguientes cadenas: ["Manzana", "pera", "BANANA", "naranja"].
# Ordena la lista sin diferenciar entre mayúsculas y minúsculas.

cadena = ["Manzana", "pera", "BANANA", "naranja"]
cadena.sort(key=str.lower)
print(cadena)
