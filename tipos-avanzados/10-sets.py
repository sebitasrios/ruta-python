# set significa grupo o conjunto
primer = {1, 1, 2, 2, 3, 4}
segundo = [3, 4, 5]
segundo = set(segundo)

# unifica el primer set y el segundo
print(primer | segundo)

# imprime solo los datos repetidos dentro de
# ambos sets
print(primer & segundo)

# imprime solo datos de diferentes en los set
print(primer - segundo)

# diferencia simetrica
print(primer ^ segundo)

if 5 in segundo:
    print("hola mundo")
