"""
exercises.py
Ejercicios para practicar los conceptos aprendidos en las lecciones.
leer un numero y hallar su facotorial
5|= 5*4*3*2*1 = 120
utilice la estructura for y while
"""

from os import system

if system("clear") != 0:
    system("cls")


n = int(input("ingrese un numero\n"))
factorial = 1
for i in range(1, n + 1, 1):
    factorial *= i
print(f"el factorial de {n} es: {factorial}")


n = int(input("ingrese un numero\n"))
factorial = 1
while n > 1:
    factorial *= n
    n -= 1
print(f"el factorial de {n} es: {factorial}")
