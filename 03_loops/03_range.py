###
# 03 - range ( )
# permite crear una secuencia de numero, puede ser util para for, pero no solo para eso
###

from os import system

if system("clear") != 0:
    system("cls")

# generando una secuencia de numeros del 0 al 10
# for num in range(10):
#     print(num)

# range (inicio, fin)
for num in range(5, 10):
    print(num)

# range(inicio, fin, paso)
for num in range(0, 1000, 5):
    print(num)

# range para numero negativos
for num in range(-5, 0):
    print(num)

for num in range(10, 0, -1):
    print(num)

nums = range(10)
list_of_nums = list(nums)
print(list_of_nums)

# seria para hacerlo 5 veces con while
contador = 0
while contador <= 5:
    print("hacer 5 veces algo")
    contador += 1

# seria para hcerlo mejor que el while en linea mas corta
for _ in range(5):
    print("ahcer 5 veces")


###
# EJERCICIOS (range)
###

# Ejercicio 1: Imprimir números del 1 al 10
# Imprime los números del 1 al 10 (inclusive) usando un bucle for y range().
print("\nEjercicio 1:")

for _ in range(1, 11):
    print(_)

for num in range(1, 11):
    print(num)

# Ejercicio 2: Imprimir números impares del 1 al 20
# Imprime todos los números impares entre 1 y 20 (inclusive) usando un bucle for y range().
print("\nEjercicio 2:")

for num_impar in range(1, 20, 2):
    print(num_impar)

# Ejercicio 3: Imprimir múltiplos de 5
# Imprime los múltiplos de 5 desde 5 hasta 50 (inclusive) usando un bucle for y range().
print("\nEjercicio 3:")

for num in range(5, 51, 5):
    print(num)

# Ejercicio 4: Imprimir números en orden inverso
# Imprime los números del 10 al 1 (inclusive) en orden inverso usando un bucle for y range().
print("\nEjercicio 4:")

for num_inverso in range(10, 0, -1):
    print(num_inverso)

# Ejercicio 5: Suma de números en un rango
# Calcula la suma de los números del 1 al 100 (inclusive) usando un bucle for y range().
print("\nEjercicio 5:")
sum_total = 0
for num in range(0, 101):
    sum_total = sum_total + num
print(sum_total)

# Ejercicio 6: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle for y range().
print("\nEjercicio 6:")

num = int(input("ingrese numero"))

for tabla in range(1, 11):
    res = num * tabla
    print(f"{num} * {tabla} = {res}")
