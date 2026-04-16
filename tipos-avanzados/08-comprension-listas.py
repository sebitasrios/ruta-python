usuarios = [["chachito", 4], ["Felipe", 1], ["pulga", 5]]

##sirve para iterar o recorrer el ciclo
##e imprimir el primer elemento del array
# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[0])
# print(nombres)

# es una manera mas simplificada y menos ram
# el nombre comun es map
# nombres = [usuario[0] for usuario in usuarios]

# filtrar - filter
# nombres = [usuario for usuario in usuarios if usuario[1] > 2]

##filtrar y transformar
# nombres = [usuario[0] for usuario in usuarios if usuario[1] > 2]

# utilizando la funcion map
# nombres = list(map(lambda usuario: usuario[0], usuarios))


menosUsuarios = list(filter(lambda usuario: usuario[1] > 2, usuarios))
print(menosUsuarios)
