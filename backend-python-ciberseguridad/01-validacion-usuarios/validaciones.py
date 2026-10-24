
def validar_correo(correo):
    correo = correo.strip()

    if not correo:
        return False

    if correo.count("@") != 1:
        return False

    usuario, dominio = correo.split("@")

    if not usuario or not dominio:
        return False

    if "." not in dominio:
        return False

    return True

def validar_contrasena(contrasena):
    if len(contrasena) < 8:
        return False
    return True