###
# 02 - bucles (for)
# permiten ejecutar un bloque de codigo repetidamente mientras ITERA un iterable o un  alista
###

from os import system

if system("clear") != 0:
    system("cls")

print("bucle for:")

# iterar una lista
frutas = ["manazana", "pera", "mandarina"]

for fruta in frutas:
    print(frutas)

# iterar sobre cualquier cosa que sea iterable
cadena = "sebas"
for caracter in cadena:
    print(caracter)

# enumerate()
fruta = ["manazana", "pera", "mandarina"]
for index, fruta in enumerate(frutas):
    print(f"el indice es {index} y la fruta es {fruta}")

# fruta = ["manazana", "pera", "mandarina"]
# puede ser cualquier name que le pongas
# for idx, value in enumerate(frutas):
#     print(f"el indice es {idx} y la fruta es {value}")

# bucles anidados
letras = ["A", "B", "C"]
numeros = [1, 2, 3]

for letra in letras:
    for numero in numeros:
        print(f"{letra}{numero}")

# break
print("\nbreak:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for indx, animal in enumerate(animales):
    print(animal)
    if animal == "loro":
        print(f"el loro esta escondido en el indice {indx}")
    break

# continue
print("\ncontinue:")
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
for indx, animal in enumerate(animales):
    if animal == "loro":
        continue
    print(animal)

# comrpension en listas(list comprehension)
animales = ["perro", "gato", "raton", "loro", "pez", "canario"]
animales_mayus = [animal.upper() for animal in animales]
print(animales_mayus)

# muestra los numero pares de una lista
pares = [num for num in [1, 2, 3, 4, 5, 6] if num % 2 == 0]

###
# EJERCICIOS (for)
###

# Ejercicio 1: Imprimir números pares
# Imprime todos los números pares del 2 al 20 (inclusive) usando un bucle for.
print("\nEjercicio 1:")
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for i, numero in enumerate(lista):
    pares = [numero for numero in lista if numero % 2 == 0]
print(pares)


# Ejercicio 2: Calcular la media de una lista
# Dada la siguiente lista de números:
# numeros = [10, 20, 30, 40, 50]
# Calcula la media de los números usando un bucle for.
print("\nEjercicio 2:")
numeros = [10, 20, 30, 40, 50]
sum_tot = 0
media = 0

for i, numero in enumerate(numeros):
    sum_tot = sum_tot + numero
    i += 1
    media = sum_tot / i
print(f"la media de la lista {numeros} es: {media}")


# Ejercicio 3: Buscar el máximo de una lista
# Dada la siguiente lista de números:
# numeros = [15, 5, 25, 10, 20]
# Encuentra el número máximo en la lista usando un bucle for.
print("\nEjercicio 3:")
# primer forma
print("primer forma con el metodo sorted(ordenamiento de menor a mayor)")
numeros = [15, 5, 25, 10, 20]
num = sorted(numeros)
print(num[-1])

# segunda forma
print("segunda forma con ciclo for y comparando uno por uno")
numeros = [15, 5, 25, 10, 20]
a = 0

for i, numero in enumerate(numeros):
    if a <= numero:
        a = numero
    else:
        continue
print(a)


# Ejercicio 4: Filtrar cadenas por longitud
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna"]
# Crea una nueva lista que contenga solo las palabras con más de 5 letras
# usando un bucle for y list comprehension.
print("\nEjercicio 4:")

palabras = ["casa", "arbol", "sol", "elefante", "luna"]
new_list = []

for char in palabras:
    if len(char) >= 5:
        new_list.append(char)
print(new_list)

# Ejercicio 5: Contar palabras que empiezan con una letra
# Dada la siguiente lista de palabras:
# palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
# Pide al usuario que introduzca una letra.
# Cuenta cuántas palabras en la lista empiezan con esa letra (sin diferenciar mayúsculas/minúsculas).
print("\nEjercicio 5:")

lista_palabras = ["casa", "arbol", "sol", "elefante", "luna", "coche"]
letra_usuario = input("ingresa una letra: \n")
contador = 0
for palabra in lista_palabras:
    for letra in palabra[0]:
        if letra_usuario == palabra[0]:
            contador += 1
        else:
            continue
print(contador)
