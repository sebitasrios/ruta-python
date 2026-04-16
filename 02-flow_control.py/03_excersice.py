###
# EJERCICIO
###

from os import system

if system("clear") != 0:
    system("cls")

# Ejercicio 1: Determinar el mayor de dos números
# Pide al usuario que introduzca dos números y muestra un mensaje
# indicando cuál es mayor o si son iguales

a = input("ingrese primer numero:\n")
b = input("ingrese segundo numero:\n")

a = int(a)
b = int(b)

# debo mejorar el ingresar y asignarlos de str a int en una sola linea
# num1 = int(input("introduce el primer numero: "))


if a > b:
    print(f"el numero mayor es: {a}")
elif b > a:
    print(f"el numero mayor es : {b}")
else:
    print("los numeros son iguales")

# Ejercicio 2: Calculadora simple
# Pide al usuario dos números y una operación (+, -, *, /)
# Realiza la operación y muestra el resultado (maneja la división entre zero)

n1 = input("ingrese primer numero:\n")
n2 = input("ingrese segundo numero:\n")
print("seleccione una operacion: suma, resta, division o multiplicacion")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1 - n2
multiplicacion = n1 * n2

if n2 != 0:
    division = n1 / n2
else:
    division = None
    print("no se puede dividir entre 0")
##correccion de la division
# elif operacion(es una variable asiganda) == "/":
#   if n2 == 0:
#       print("error: no se puede divir por 0")
#   else:
#       resultado(variable asignada) = n1 / n2
# else:
#   print("opreacion no valida")
#
# if 'resultado' in locals(): #esto comprueba si la variable resultado existe
#   print(f"el resultado es: {resutlado}")


mensaje = f"""
para los numeros {n1} y {n2},
el resultado de la suma es {suma}.
el resultado de la resta es {resta}.
el resultado de la multiplicacion es {multiplicacion}.
"""
if division is not None:
    mensaje += f"el resultado de la division es {division}.\n"
print(mensaje)


# Ejercicio 3: Año bisiesto
# Pide al usuario que introduzca un año y determina si es bisiesto.
# Un año es bisiesto si es divisible por 4, excepto si es divisible por 100 pero no por 400.

anio = input("ingrese año \n ")
anio = int(anio)
if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
    print("el año es bisiesto")
else:
    print("el año no es bisiesto")


# Ejercicio 4: Categorizar edades
# Pide al usuario que introduzca una edad y la clasifique en:
# - Bebé (0-2 años)
# - Niño (3-12 años)
# - Adolescente (13-17 años)
# - Adulto (18-64 años)5
# - Adulto mayor (65 años o más)


edad = input("ingrese edad: \n")
edad = int(edad)


if edad < 0:
    print("ingrese edad que sea valida o mayor a 0")
elif edad <= 2:
    print("es un bebe\n")
elif edad <= 12:
    print("es un niño")
elif edad <= 17:
    print("es un adolecente")
elif edad <= 64:
    print("es un adulto")
else:
    print("es un adulto mayor")
