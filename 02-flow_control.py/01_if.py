###
# 01 - sentencias condicionales (if, elif, else)
# permiten ejecutar bloques de codigo solo si se cumplne ciertas condiciones.
###

import os

os.system("clear")

print("\n sentencia simple condicional")

edad = 18

if edad >= 18:
    print("eres mayor de edad")
    print("¡felicidades!")

edad = 15

if edad >= 18:
    print("eres mayor de edad")
    print("¡felicidades!")

print("\n sentencia con else")

edad = 15
if edad >= 18:
    print("eres mayor de edad")
else:
    print("eres menor de edad")

print("\n sentencia condiconal con elif")

nota = 7
if nota >= 9:
    print("sobresaliente")
elif nota >= 7:
    print("notable")
elif nota >= 5:
    print("aprobado")
else:
    print("no esta calificado")


print("\n condicioones multiples ")

edad = 25
tiene_carnet = True

# javaScript
# && -> and
# || -> or
if edad >= 18 and tiene_carnet:
    print("puedes conducir")
else:
    print("POLICIA ¡¡¡¡¡1¡¡¡¡")

# un pueblo de valencia

if edad >= 18 and tiene_carnet:
    print("puedes conducir en la isla")
else:
    print("paga al policia y te deja conducir¡¡¡")


# un pueblo de isla margarita

if edad >= 18 or tiene_carnet:
    print("puedes conducir en la isla")
else:
    print("paga al policia y te deja conducir¡¡¡")


es_fin_de_Semana = False
# javaScript -> !
if not es_fin_de_Semana:
    print("sebas venga que hay que estudiar")


print("\n anidar condicionales")

edad = 20
tiene_dinero = True
if edad >= 18:
    if tiene_dinero:
        print("puedes ir a la discoteca")
    else:
        print("quedate en casa")
else:
    print("no puedes entrar a la discotec")

# mas facil de esta manera
if edad < 18:
    print("no puedes entrar a la disco")
elif tiene_dinero:
    print("puedes ir a la discoteca")
else:
    print("quedate en caca")


numero = 5
if numero:  # True
    print("el numero no es cero")
numero = 0
if numero:  # False
    print("aqui no entrara nunca")

nombre = ""
if nombre:
    print("el nombre no es vacio")


numero = 3  # asignacion
es_el_tres = numero == 3  # comparacion

if es_el_tres:
    print("el numero es 3")

print("\nla condicion ternaria:")
# es una forma concisa de un if-else en una linea de codigo
# (codigo si cumple cla condicion) if [condicion] else [codigo si no cumple]

edad = 17
mensaje = "es mayor de edad" if edad >= 18 else "es menor de edad"
print(mensaje)
