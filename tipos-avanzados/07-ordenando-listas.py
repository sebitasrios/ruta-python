numeros = [2, 4, 10, 15, 85, 52, 14, 75]

# numeros.sort.()
# organiza la lista en orden
# numeros.sort(reverse=True)
# es para organizar la lista de forma descenedente

numeros2 = sorted(numeros)
# es para organizar en una nueva lista

numeros3 = sorted(numeros, reverse=True)
# es para organizar la nueva lista al reves

print(numeros)
print(numeros2)
print(numeros3)

# ejemplo de lista ordenada
# usuarios = [[4, "chachito"], [1, "Felipe"], [5, "pulga"]]
# print(usuarios)

# ejemplo de lista no ordenada y que debemos ordenar por medio del id
usuarios = [["chachito", 4], ["Felipe", 1], ["pulga", 5]]


# funcion que recibe elemento y retorna elemento
def ordena(elemento):
    return elemento[1]


# ordena de manera ordenada el id
usuarios.sort(key=ordena)
print(usuarios)


# funcion que recibe elemento y retorna elemento
def ordena_reves(elemento2):
    return elemento2[1]


# ordena de manera ordenada pero descendente
usuarios.sort(key=ordena_reves, reverse=True)
print(usuarios)


##se puede hacer mas simplificada


# funcion que recibe elemento y retorna elemento
def ordena(elemento):
    return elemento[1]


# ordena de manera ordenada pero descendente
usuarios.sort(key=lambda el: el[1], reverse=True)
print(usuarios)
