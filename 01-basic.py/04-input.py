###
# 05 - entrada de ususario (input()) - version simplificada
# la funcion input() permite obtener datos del usuarioa traves de la consola
###


nombre = input("hola, ¿como te llamas?\n")
print(f"hola {nombre}, encantado de conocerte")

age = input("¿cuantos años tienes? \n")
age = int(age)
print(f"tienes {age} años")

print("obtener multiples variables")

country, city = input(
    "¿en que pais y ciudad vives? \n"
).split()  # el split hace que cada entrada del usuario
# se asigne de acuerdo al orden de las variables declaradas
print(f"vives en {country}, {city}")
