###
# 03 - variables
# las variables sirven para guardar
# datos en memoria
# python es un lendguaje de tipado dinamico
# y de tipado fuerte
###

# asignar un avariable
# solo ahce falta poner esto
my_name = "sebas"
print(my_name)

# las variables se pueden reasignar
age = 32
print(age)

age = 39
print(age)

# tipado dinamico:
# el tipo de dato se puede determinar en tiempo de ejecucion
# que no tienes que declararlo explicitamente
name = "sebas"
print(type(name))

name = 32
print(type(name))


# tipado fuerte:
# python no realiza conversiones de tipo automatico
# print(10 + "2")

# f - string (literal de cadena de formato)
print(f"hola {my_name}, tengo {age + 5} años")

# no recomendada forma de asignar variables
name, age, city = "sebas", 32, "medellin"

# convenciones de nombres de variables
mi_nombre_de_variable = "ok"  # snake_case
nombre = "ok"

MiNomrbreDeVariable = "ko"  # pascalcase
minombredevariable = "ko"  # todojunto
mi_nombre_de_variable_123 = "ok"
MI_CONSTANTE = 3.14  # UPPER_CASE - constantes

# nombres no validos de variables
# 132456_variable = "ko"
# mi-variable = "ko"
# mi variable ="ko"
# True = False


# is_user_logged_in = bool = True
# print(is_user_logged_in)

# # esto es para comentar la varibale
# is_user_logged_in = 42
# print(is_user_logged_in)
