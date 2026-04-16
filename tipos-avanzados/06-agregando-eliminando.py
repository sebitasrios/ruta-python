mascotas = ["wolfgang", "pelusa", "pulga", "Felipe", "pulga", "chanchito feliz"]

mascotas.insert(1, "melvin")
mascotas.append("chanchito triste")


mascotas.remove("pulga")
# para remover algun elemento con indice
mascotas.pop(1)
# para remover indicando el numero del arreglo
del mascotas[0]
# para borrar indicando el numero dentro del arreglo
mascotas.clear()
# para limpiar toda la lista
print(mascotas)
