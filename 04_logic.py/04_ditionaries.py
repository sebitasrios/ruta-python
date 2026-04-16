###
# 04 - Dictionaries
# los diccionarios son colecciones de pares clave-valor
# sirven para almancenar datos relacionados
###

from os import system

if system("clear") != 0:
    system("cls")

# ejemplo tipico de un diccionario

persona = {
    "nombre": "sebas",
    "edad": 33,
    "es_estudiante": True,
    "calificaciones": [7, 8, 9],
    "socials": {"twitter": "@sebas", "instagram": "@sebas", "facebook": "sebitas10"},
}

# para acceder a los valores
print(persona["nombre"])
print(persona["calificaciones"][2])
print(persona["socials"]["twitter"])

# cambiar valores al acceder
persona["nombre"] = "sebastian"
persona["calificaciones"][2] = 10

# esto imprime todo el diccionario
# print(persona)

# para eliminar completamente una propiedad

del persona["edad"]
# print(persona)

# este metodo es para devolver y eliminar la clave
es_estudiante = persona.pop("es_estudiante")
print(f"es_estudiante: {es_estudiante}")
print(persona)

# sobreescribir un diccionario con otro diccionario
a = {"name": "sebas", "age": 33}
b = {"name": "sebastian", "es_estudiante": True}

# el update actualiza la informacion y si la propiedad no esta el la asigna en la actualizacion
a.update(b)
print(a)

# comprobar si hay una propiedad
print("name" in persona)
print("nombre" in persona)

# otros metodos para obtener todas las claves
print("\nkeys: ")
print(persona.keys())

# para obtener todos los valores
print("\nvalues: ")
print(persona.values())


# para obtener todos los items(tanto clave como valor)
print("\nitems: ")
print(persona.items())

for key, value in persona.items():
    print(f"{key}: {value}")
