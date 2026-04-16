###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system

if system("clear") != 0:
    system("cls")

print("\nEjercicio 1: Imprimir mensajes")
print("Escribe un programa que imprima tu nombre y tu ciudad en líneas separadas.")

### Completa aquí
nombre = input("ingresa tu nombre \n")
ciudad = input("en que ciudad vives \n")

print(f"bienvenido {nombre}\n")
print(f"actualmente vives en {ciudad}\n")

print("--------------")

print("\nEjercicio 2: Muestra los tipos de datos de las siguientes variables:")
print("Usa el comando 'type()' para determinar el tipo de datos de cada variable.")
a = 15
b = 3.14159
c = "Hola mundo"
d = True
e = None

### Completa aquí
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

print("--------------")

print("\nEjercicio 3: Casting de tipos")
print('Convierte la cadena "12345" a un entero y luego a un float.')
print("Convierte el float 3.99 a un entero. ¿Qué ocurre?")

### Completa aquí
print(int("12345"))
print(float("12345"))
print(int(3.99))

print("--------------")

print("\nEjercicio 4: Variables")
print("Crea variables para tu nombre, edad y altura.")
print("Usa f-strings para imprimir una presentación.")

# "Hola! Me llamo midudev y tengo 39 años, mido 1.70 metros"

### Completa aquí
name = input("ingresa tu nombre \n")
age = input("ingrese su edad \n")
heigth = input("ingrese su altura \n")

print(f"Hola! Me llamo {name}, y tengo {age}, mido {heigth} metros\n ")

print("--------------")

print("\nEjercicio 5: Números")
print("1. Crea una variable con el número PI (sin asignar una variable)")
print("2. Redondea el número con round()")
print("3. Haz la división entera entre el número que te salió y el número 2")
print("4. El resultado debería ser 1")


pi = float(3.1416)
print(pi)
red = round(pi)
print(red)
div = int(red / 2)
print(div)
