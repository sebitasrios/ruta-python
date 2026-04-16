"""
En Jurassic Park, se ha observado que los dinosaurios carnívoros, como el temible T-Rex,
depositan un número par de huevos. Imagina que tienes una lista de números enteros
en la que cada número representa la cantidad de huevos puestos por un dinosaurio en el parque.

Importante: Solo se consideran los huevos de los dinosaurios carnívoros (T-Rex) aquellos números que son pares.

Objetivo:
Escribe una función en Python que reciba una lista de números enteros y devuelva la suma total
 de los huevos que pertenecen a los dinosaurios carnívoros
 (es decir, la suma de todos los números pares en la lista).
"""

from os import system

if system("clear") != 0:
    system("cls")


# para ver si un numero es par
# siempre usamos el modulo %
# nos da el resto de la division: eggs % 2 == 0


def count_carnivoro_dinosaur_eggs(egg_list) -> int:
    """
    esta funcion recibe una lista de numeros enteros que representa la cantidad de huevos
    que han puestos difernetes dinoseaurios en el parque jurasico y los de numero par son carnivoros,
    devuelve un numero con la suma de todos los huevos de carnivoros
    """
    total_carnivore_egg = 0

    for eggs in egg_list:
        if eggs % 2 == 0:
            total_carnivore_egg += eggs

    return total_carnivore_egg


egg_list = [3, 4, 7, 5, 8]
print(count_carnivoro_dinosaur_eggs(egg_list))
