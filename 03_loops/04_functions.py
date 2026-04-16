###
# 04 - funciones
# bloques de codigo reutilizables y parametrizables para hacer tareas especificas
###

# ### definicion de una funcion
# def nombre_de_la_funcion(parametro1, parametro2, ....):
#     #codfigo de la funcion
#     #docstring
#     #cuerpo de la funcion
#     return valor_de_Retorno #opcional


from os import system

if system("clear") != 0:
    system("cls")


# ejemplo de una funcion para imprimir algo en consola
def saludar():
    print("hola")


saludar()


# ejemplo de una funcion con parametro
def saludar_a(name):
    print(f"hola {name}")


saludar_a("sebas")
saludar_a("feliz")
saludar_a("isaac")


# funciones con mas parametros
def sumar(a, b):
    suma = a + b
    return suma


# 1. primer opcion
result = sumar(2, 3)
print(result)

# 2. segundo opcion
print(sumar(2, 5))


# documentar las funciones con docstring
def restar(a, b):
    """resta dos numeros y devuelve el resultado"""
    return a - b


print(restar.__doc__)  # accede a la documentacion de la funcion

# accede a una explicacion del main en la funcion restar
# help(restar)


# parametros por defecto
def multiplicar(a, b=2):
    return a * b


print(multiplicar(2))
print(multiplicar(2, 3))


# argumentos por posicion
def describir_persona(nombre, edad, sexo):
    print(f"soy {nombre}, tengo {edad} años y me identifico como {sexo}")


# argumentos son posicionales
describir_persona("sebas", 25, "humano")
describir_persona("humano", "sebas", 25)

# argumentos por clave
# parametros nombrados
describir_persona(sexo="humano", nombre="sebas", edad=25)


# argumentos de longitud de variable (*args)
def sumar_numeros(*args):
    suma = 0
    for numero in args:
        suma += numero
    return suma


print(sumar_numeros(1, 2, 3, 4, 5))
print(sumar_numeros(1, 2))
print(sumar_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))


# argumentos de clave-valor variable (**kwgars):
def mostrar_informacion_de(**kwargs):
    for clave, valor in kwargs.items():
        print(f"{clave}: {valor}")


mostrar_informacion_de(nombre="sebas", edad=33, sexo="humano")
print("\n")
mostrar_informacion_de(nombre="isaac", edad=7, country="colombia")
print("\n")
mostrar_informacion_de(nombre="milena", es_sub=True, is_rich=True)
print("\n")
mostrar_informacion_de(nombre="aleja", es_modo=True, perros=40)

# ejercicios
# volver a los ejercicios anteriores
# y convertirlos en funciones
# e iterar utilizar todos los casos y conceptos
# que hemos visto hasta ahora
