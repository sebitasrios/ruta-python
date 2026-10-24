
import unittest
from validaciones import validar_correo, validar_contrasena


class TestValidarCorreo(unittest.TestCase):

    def test_correo_valido(self):
        self.assertTrue(validar_correo("sebas@gmail.com"))

    def test_correo_sin_arroba(self):
        self.assertFalse(validar_correo("sebasgmail.com"))

    def test_correo_vacio(self):
        self.assertFalse(validar_correo(""))

    def test_dominio_sin_punto(self):
        self.assertFalse(validar_correo("carlos@hotmailcom"))

    def test_correo_sin_usuario(self):
        self.assertFalse(validar_correo("@gmail.com"))

    def test_correo_sin_dominio(self):
        self.assertFalse(validar_correo("sebas@"))

    def test_correo_con_espacios_externos(self):
        self.assertTrue(validar_correo(" sebas@gmail.com "))

    def test_contraseña_valida(self):
        self.assertTrue(validar_contrasena("clave123"))

    def test_contraseña_corta(self):
        self.assertFalse(validar_contrasena("abc123"))

    def test_contraseña_vacia(self):
        self.assertFalse(validar_contrasena(""))
if __name__ == "__main__":
    unittest.main()
