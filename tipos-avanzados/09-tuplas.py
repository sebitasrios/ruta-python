numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

punto = tuple([1, 2])
print(punto)
##crea una tupla a razi de la primera tupla

# crea una tupla nueva con la condicion
# que nosotros le estamos pasando
menosNumeros = numeros[:2]
print(menosNumeros)

# sirve para desempaquetar las tuplas
primero, segundo, *otros = numeros
print(primero, segundo, otros)

# iterar las tuplas
for n in numeros:
    print(n)

# de esta manera podemos crear una nueva tupla
# a partir de la primera y poder modifcarla
# de lo contrario la tupla nunca se puede modificar
listaNumeros = list(numeros)
listaNumeros[0] = "Chanchito feliz"
print(listaNumeros)
