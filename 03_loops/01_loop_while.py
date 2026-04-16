###
# 01 - bucles (while)
# permiten ejecutar un bloque de codigo repetidamente mientras se cumpla una condicion
#

from os import system

if system("clear") != 0:
    system("cls")


print("bucle infitnito")

# bucle con una simple condicion
contador = 0

while contador <= 5:
    print(contador)
    contador += 1  # es super importante para evitar un bucle infinito

# utilizando la palabara break, para romper el ciclo

print("\n bucle while con break")
contador = 0

while contador <= 100:
    contador += 1
    print(contador)
    if contador % 5 == 0:
        print("el numero es multiplo de 5")
        break  # sale del bucle

# continue, que lo ahce es saltar esa iteracion en concreto
# y continuar con el bucle

print("\n bucle con continue")
contador = 0

while contador < 10:
    contador += 1

    if contador % 2 == 0:
        continue
    # el codigo no lo rompe hasta cumplir la condicion
    print(contador)

# else, esta condicion cuando se ejecuta?

print("\n bucle while con else:")
contador1 = 0
while contador1 < 5:
    print(contador1)
    contador1 += 1
else:
    print("el bucle ha terminado")


# pedirle al usuario un numero que tiene
# que ser positivo si no, no lo dejamos en paz

# numero = -1
# while numero < 0:
#     numero = int(input("escribe un numero positivo: "))
#     if numero <= 0:
#         print("el numero debe ser positivo, intenta otra vez, jajaja: ")
# print(f"el numero que has introducido es: {numero}")
# se puede hacer mejor para evitar errores con ingresos de usuarios

numero = -1
while numero < 0:
    try:
        numero = int(input("escribe un numero positivo: "))
        if numero <= 0:
            print("el numero debe ser positivo, intenta otra vez, jajaja: ")
    except:
        print("lo que introduces debe ser un numero, vuelve a intentar")

print(f"el numero que has introducido es: {numero}")

###
# EJERCICIOS (while)
###

# Ejercicio 1: Cuenta atrás
# Imprime los números del 10 al 1 usando un bucle while.
print("\nEjercicio 1:")

contador = 10
while contador > 0:
    print(contador)
    contador -= 1


# Ejercicio 2: Suma de números pares (while)
# Calcula la suma de los números pares entre 1 y 20 (inclusive) usando un bucle while.
print("\nEjercicio 2:")

suma_total = 0
contador = 0

while contador <= 20:
    if contador % 2 == 0:
        suma_total = contador + suma_total
    contador += 1
print(f"la suma total es: {suma_total}")

# Ejercicio 3: Factorial de un número
# Pide al usuario que introduzca un número entero positivo.
# Calcula su factorial usando un bucle while.
# El factorial de un número entero positivo es el producto de todos los números del 1 al ese número. Por ejemplo, el factorial de 5
# 5! = 5 x 4 x 3 x 2 x 1 = 120.
print("\nEjercicio 3:")

numero = int(input("ingrese un numero positivo:"))
contador2 = 1
factorial = 1
while contador2 <= numero:
    if numero >= 1:
        factorial = factorial * contador2
        print(factorial)
        contador2 += 1
    else:
        print("ingrese un numero positivo")
print("ingrese numero valido o positivo")

# Ejercicio 4: Validación de contraseña
# Pide al usuario que introduzca una contraseña.
# La contraseña debe tener al menos 8 caracteres.
# Usa un bucle while para seguir pidiendo la contraseña hasta que cumpla con los requisitos.
# Si la contraseña es válida, imprime "Contraseña válida".
print("\nEjercicio 4:")

while True:
    contraseña = input("ingrese una contraseña de 8 caracteres: ")
    if len(contraseña) <= 8 and len(contraseña) >= 5:
        print("contraseña valida")
        break
    else:
        print("la contraseña debe tener entre 5 a 8 caracteres")
    continue


# Ejercicio 5: Tabla de multiplicar
# Pide al usuario que introduzca un número.
# Imprime la tabla de multiplicar de ese número (del 1 al 10) usando un bucle while.
print("\nEjercicio 5:")

num = int(input("ingrese un numero"))
contador = 0
resultado = 0

while contador < 10:
    contador += 1
    if num > 1:
        resultado = num * contador
        print(f"{num} * {contador} = {resultado}")
    else:
        print("ingrese un numero positivo o numero valido")


# Ejercicio 6: Números primos hasta N
# Pide al usuario que introduzca un número entero positivo N.
# Imprime todos los números primos menores o iguales que N usando un bucle while.

print("\nEjercicio 6:")
n = int(input("Introduce un número entero positivo N: "))

numero = 2
while numero <= n:
    es_primo = (
        True  # Asumimos que el número es primo hasta que se demuestre lo contrario
    )
    divisor = 2
    while (
        divisor * divisor <= numero
    ):  # Optimizamos: no es necesario probar divisores hasta numero
        if numero % divisor == 0:
            es_primo = False  # Si encontramos un divisor, no es primo
            break  # Salimos del bucle interior
        divisor += 1
    if es_primo:
        print(numero)

    numero += 1
