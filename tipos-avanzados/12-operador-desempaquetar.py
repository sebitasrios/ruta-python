# lista1 = [1, 2, 3, 4]
# # print(1, 2, 3, 4)
# # print(*lista)

# lista2 = [5, 6]

# combinada = [*lista1, *lista2]
# print(combinada)

# combinada = ["hola", *lista1, "mundo", *lista2, "chanchito"]
# print(combinada)

##desempaquetar por medio de diccionarios
punto1 = {"x": 19}
punto2 = {"y": 15}

nuevopunto = {**punto1, "lala": "hola mundo", **punto2, "z": "mundo"}
print(nuevopunto)
