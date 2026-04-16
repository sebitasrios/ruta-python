def palindromo(texto):
    if texto.isnumeric():
        print(f"{texto} es un numero. ")
        return None
    texto = texto.lower().replace(" ", "").replace(",", "").replace(".", "")
    return texto == texto[::-1]


texto1 = input("ingresa un texto: ")
print(f"el texto ingresado es: {texto1}")
resultado = palindromo(texto1)
if resultado is None:
    pass  # ya se imprimio el mensaje de "es un numero"
elif resultado:
    print(f"{texto1} es un palindromo")
else:
    print(f"{texto1} no es palindromo")
