# 01 · Validación de datos de registro de usuarios

Ejercicio de Python que valida los datos de un registro de usuario (nombre, correo y contraseña) y lo prueba con pruebas unitarias. Es el primero de la ruta [Backend con Python y Ciberseguridad](..).

## Archivos

| Archivo | Qué hace |
|---|---|
| `validaciones.py` | Funciones `validar_correo()` y `validar_contrasena()` |
| `registro_usuarios.py` | Programa de consola que pide los datos y muestra los errores encontrados |
| `test_validaciones.py` | Pruebas con `unittest` (10 casos) |

## Reglas de validación

- **Nombre:** no puede estar vacío.
- **Correo:** un solo `@`, con texto antes y después, y un punto en el dominio. Se ignoran los espacios al inicio y al final.
- **Contraseña:** mínimo 8 caracteres. Se pide con `getpass`, así no se muestra en pantalla ni se imprime al final.

## Cómo ejecutarlo

```bash
python registro_usuarios.py
```

## Cómo correr las pruebas

```bash
python -m unittest -v test_validaciones
```

## Conceptos practicados

Funciones, importación de módulos, validación de entradas, lista de errores, `getpass` y pruebas unitarias con `unittest`.

## Posibles mejoras

- Rechazar dominios como `a@.com` o `a@b.` (hoy pasan la validación).
- Pedir mayúscula, minúscula y número en la contraseña.
- Usar una expresión regular para el correo (ver la carpeta `05_regex`).