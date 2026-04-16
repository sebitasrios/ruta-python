saludo = "hola global"


def saludar():
    global saludo
    saludo = "hola mundo"


def saludaChanchito():
    saludo = 24
    print(saludo)


print(saludo)
saludar()
saludaChanchito()
print(saludo)
