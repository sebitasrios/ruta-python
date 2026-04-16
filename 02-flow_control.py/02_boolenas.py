###
# 02 - booleans
# valores logico: True(verdadero) y false (falso)
# fundamentos para el control de flujo y la logica en programacion
###

import os

os.system("clear")

# los booleans representan valores de verdad: True o False.
print("\n valores booleans basicos")
print(True)
print(False)

# operadores de comparacion: devuelven un valor booleano.
print("\n operadores de comparacion:")
print("5 > 3:", 5 > 3)  # True
print("5 < 3:", 5 < 3)  # False
print("5 == 3:", 5 == 3)  # True(igualdad)
print("5 != 3:", 5 != 3)  # True(desigualdad)
print("5 >= 3:", 5 >= 3)  # True(mayor o igual que)
print("5 <= 3:", 5 <= 3)  # True(menor o igual que)

print("\ncomparaciones de cadenas")
print("manzana < pera", "manzana" < "pera")  # True
print("'Hola' < 'hola'", "manzana" < "pera")  # False

# operadores logicos: and, or, not
print("True and True:", True and True)  # True
print("True and False:", True and False)  # False
print("True or False:", True or False)  # True
print("False or False;", False or False)  # False
print("not True:", not True)  # False
print("not False:", not False)  # True

# tablas de verdad (para referencia):
print("\ntablas de verdad:")
print("and:")
print("A       B     A and B")
print("True    True ", True and False)
print("True    False", True and False)
print("False   True ", False and True)
print("False   False", False and False)

print("\n or:")
print("or:")
print("A       B     A and B")
print("True    True ", True or False)
print("True    False", True or False)
print("False   True ", False or True)
print("False   False", False or False)

print("\n not:")
print("A    not A")
print("True ", not True)
print("False", not False)
