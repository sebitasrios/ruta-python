###
# exercises.py
# Ejercicios para practicar los conceptos aprendidos en las lecciones.
###

from os import system

if system("clear") != 0:
    system("cls")

###

# capturar el nombre y salario de n trabajadores
# mostrar en pantalla

#   1. promedio salarial
#  2. numero de empleados que ganan menos de $2.000.000
# 3. numero de empleados que ganan entre $2.000.000 y $5.000.000
# 4. numero de empleados que ganan mas de $5.000.000

###

n = int(input("ingrese el numero de empleados\n"))
salario = 0
prom = 0
contmenos2 = 0
contentre2y5 = 0
contmas5 = 0

for i in range(1, n + 1, 1):
    nombre = input(f"ingrese el nombre del empleado {i}\n")
    salario = int(input(f"ingrese el salario del empleado {i}\n"))
    prom = salario / n
    if salario < 2000000:
        print(f"el empleado {nombre} gana menos de $2.000.000")
        contmenos2 += 1
    elif salario >= 2000000 and salario <= 5000000:
        print(f"el empleado {nombre} gana entre $2.000.000 y $5.000.000")
        contentre2y5 += 1
    else:
        print(f"el empleado {nombre} gana mas de $5.000.000")
        contmas5 += 1
print(f"el promedio salarial es: {prom}")
