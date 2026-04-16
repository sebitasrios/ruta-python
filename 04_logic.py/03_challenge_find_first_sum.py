"""
Dado un array de números y un número goal, encuentra los dos primeros números del array
que sumen el número goal y devuelve sus índices. Si no existe tal combinación, devuelve None.

nums = [4, 5, 6, 2]
goal = 8

find_first_sum(nums, goal)  # [2, 3]
"""

from os import system

if system("clear") != 0:
    system("cls")


# def find_first_sum(nums, goal):

#     for i in range(len(nums) - 1):
#         for j in range(i + 1, len(nums)):
#             if nums[i] + nums[j] == goal:
#                 return [i, j]

#     return None  # no se encontro ninguna condicion


def find_first_sum(nums, goal):
    seen = {}  # diccionario  para guardar  el numero y su indice

    for index, value in enumerate(nums):
        # ayuda a verificar que hay en la llave y el valor de la llave
        # print(f"index: {index}  value: {value}")
        missing = goal - value
        if missing in seen:
            return [seen[missing], index]
        seen[value] = (
            index  # aca guardamos el numero actual a los vistos, porque no hemos encontrado ninguna combinacion
        )
    return None


nums = [4, 5, 6, 2]
goal = 8
result = find_first_sum(nums, goal)
print(result)


# """
# Tienes dos listas de números, lista_a y lista_b, ambas de la misma longitud.


# Cada número en lista_a se "enfrenta" al número en la misma posición en lista_b.

# - Si el número en lista_a es mayor, su valor se suma al siguiente número en lista_a.
# - Si el número en lista_b es mayor, su valor se suma al siguiente número en lista_b.
# - Si los dos números son iguales, ambos se eliminan y no afectan al siguiente par.

# Debes simular estos enfrentamientos y devolver el resultado final:
# - Si al final queda un número en lista_a, devuelve ese número seguido de la letra "a" (por ejemplo, "3a").
# - Si al final queda un número en lista_b, devuelve ese número seguido de la letra "b" (por ejemplo, "2b").
# - En caso de empate, devuelve la letra "x".

# lista_a = [2, 4, 2]
# lista_b = [3, 3, 4]

# resultado = battle(lista_a, lista_b)  # -> "2b"

# # Explicación:
# # - 2 vs 3: gana 3 (+1)
# # - 4 vs 3+1: empate
# # - 2 vs 4: gana 4 (+2)
# # Resultado: "2b"

# lista_a = [4, 4, 4]
# lista_b = [2, 8, 2]

# resultado = battle(lista_a, lista_b)  # -> "x"

# # Explicación:
# # - 4 vs 2: gana 4 (+2)
# # - 4+2 vs 8: gana 8 (+2)
# # - 4 vs 2+2: empate
# # Resultado: "x"
# """

#intento fallido 
# def battle(lista_a, lista_b):
#     for a, b in zip(lista_a, lista_b):
#         if lista_a[a] > lista_b[b]:
#             diferencia = lista_a[a] - lista_b[b]
#             lista_a[a + 1] += diferencia
#             print(f"{diferencia}a")
#         else:
#             diferencia = lista_b[b] - lista_a[a]
#             lista_b[b + 1] += diferencia
#             print(f"{diferencia}b")

#     print("Lista A:", lista_a)
#     print("Lista B:", lista_b)


# lista_a = [2, 4, 2]
# lista_b = [3, 3, 4]
# battle(
#     lista_a,
#     lista_b,
# )

def battle(lista_a, lista_b):
    puntos_a = sum(lista_a)
    puntos_b = sum(lista_b)

    if puntos_a > puntos_b:
        return f"{puntos_a - puntos_b}a"
    elif puntos_b > puntos_a:
        return f"{puntos_b - puntos_a}b"
    else:
        return "x"
    


lista_a = [4, 4, 4]
lista_b = [2, 8, 2]
winner = battle(lista_a, lista_b)
print(winner)