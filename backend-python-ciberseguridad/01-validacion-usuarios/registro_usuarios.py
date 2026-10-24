
from getpass import getpass
from validaciones import validar_correo, validar_contrasena


nombre = input("Ingrese su nombre: ").strip()
correo = input("Ingrese su correo: ").strip()
contrasena = getpass("Ingrese su contraseña: ")

errores = []

# Validar el nombre
if not nombre:
    errores.append("El nombre no puede estar vacío.")

# Validar el correo
if not validar_correo(correo):
    errores.append("El correo no tiene un formato válido.")

# Validar la contraseña
if not validar_contrasena(contrasena):
    errores.append("La contraseña debe tener al menos 8 caracteres.")

# Mostrar el resultado
if errores:
    print("\nSe encontraron errores:")
    for error in errores:
        print(f"- {error}")
else:
    print("\nLos datos superaron las validaciones.")

# No mostrar la contraseña
print(f"Nombre: {nombre}")
print(f"Correo: {correo}")
