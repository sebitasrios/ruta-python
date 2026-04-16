##
# 01 - expresiones regulares
#

import os

os.system("clear")

"""
las expresiones regulares son una secuencia de caracrteres que forman un patron
de busqueda. se utilizan para la busqueda de cadenas de texto, validacion de datos. etc...
"""

"""
¿porque aprender regex?

- busqueda avanzada de: encontrar patrones especificos en textos grandes de foram rapida y precisa. etc. son correctos.

- validacion de datos: asegurate que lso datos que ingresa un usuario con email, telefono, etc. son correctos.

- manipulacion del texto: extraer, reemplazar y modfiicar partes de la cadena de texto facilmente

"""

# 1. importar el modulo de expresiones regulares "re"

import re

# 2. crea un patron, que es una cadena de texto que describe lo que queremos encontrar
pattern = "hola"

# 3. el texto donde queremos buscar
text = "hola mundo"

# 4. usar la funcion de busqueda de "re"
result = re.search(pattern, text)

if result:
    print("he encontrado el patron en el texto")
else:
    print("no he encontrado el patron en el texto")

# - .group() devuelve la cadena que coincide con el pattern
print(result.group())

# - .start(devuelve la posicion inicial de la coincidencia)
print(result.start())

# - .end() devuelve la posicion final de la coincidencia
print(result.end())


# ejercicio 01
# encuentra la primera ocurrencia de la palabra "IA" en el
# siguiente texto
# indica en que posición empeiza y temrina la coincidencia

text = """todo el mundo dice que la IA  nos va a quitar el "
    trabajo. pero solo hace falta ver como la puede cagar con las"
    Regex para ir con cuidado"""


pattern = "IA"

found_ia = re.search(pattern, text)

if found_ia:
    print(
        f"he encontrado el patron en el texto en la posicion {found_ia.start()} y termina en la posicion {found_ia.end()} "
    )
else:
    print("no he encontrado la coincidencia")

    ### vamos a encontrar todas las coincidencia de un patron
    # .findall() devuelve una lista con todas las coincidencias
    #
    # ###

text = "me gusta python, python es lo maximo, aunque python no es tan dificil, ojo con python"
pattern = "python"

matches = re.findall(pattern, text)
print(matches)

print(len(matches))


# -----------------
# iter() devuelve un iterador que contiene todos los
# resultados de la busqueda

text = "me gusta python, python es lo maximo, aunque python no es tan dificil, ojo con python"
pattern = "python"

matches = re.finditer(pattern, text)

for match in matches:
    print(match.group(), match.start(), match.end())

# ejercicio 02

###encuentra todas las ocurrencias de la palabra "midu" en
# el siguiente texto e indica en que posición empieza y termina cada
# coincidencia y cuantas veces se encontro.
###

text = (
    " este es el curso de python de midudev. ¡suscribete "
    "a midudev si te gusta este contenido¡ midu"
)

pattern = "midu"

matches = re.finditer(pattern, text)
print(re.findall(pattern, text))


for match in matches:
    print(match.group(), match.start(), match.end())
