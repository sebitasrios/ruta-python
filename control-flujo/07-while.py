# numero = 1
# while numero < 100:
#     print (numero)
#     numero *= 2

comando = ""

while comando.lower() != "salir":
    comando = input("")
    print(comando)


while True:
    comand = input("$ ")
    print(comand)
    if comand.lower() == "salir":
        break
