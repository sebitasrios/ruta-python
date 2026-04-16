print("Bienvenidos a nuestra calculadora")
print("para salir, escriba salir")
print("las opreaciones que puede utilizar son: suma, resta, multi, div")

# n1 = print("ingrese numero")
# n1 = int(n1)
# op = ""
resultado = ""

while True:
    if not resultado:
        resultado = input("Ingrese numero: ")
        if resultado.lower() == "salir":
            break
        resultado = int(resultado)
    op = input("ingrese operacion: ")
    if op.lower() == "salir":
        break
    n2 = input("ingresa siguiente numero: ")
    if n2.lower() == "salir":
        break
    n2 = int(n2)

    if op.lower() == "suma":
        resultado += n2
    elif op.lower() == "resta":
        resultado -= n2
    elif op.lower() == "multi":
        resultado *= n2
    elif op.lower() == "div":
        resultado /= n2
    else:
        print("opreacion no valida")
        break

    print(f"el resultado es: {resultado}")


# if n1 > 0:
#     while op.lower() == "suma":
#         op = input("$ ")
#         n2 = print("ingrese siguiente numero")
#         n2 = int(n2)
#         suma = n1 + n2
#         resul = suma
#         break
#     print("el resultado de la suma es: " + suma)
