# Importar librerias
import pandas as pd
import numpy as np

from os import system

if system("clear") != 0:
    system("cls")

print("Librerias importadas correctamente")
print(f"Pandas version: {pd.__version__}")
print(f"NumPy version: {np.__version__}")


# cargar  data set de casas de california
datos_casas = pd.read_csv("tiempos.csv")


print("Datos cargados exitosamente")
print(f"Dimensiones: {datos_casas.shape}")
print("\nPrimeras 5 filas:")
print(datos_casas.head())

# Informacion basica del dataset de casas
print("INFORMACION DEL DATASET")
print("=" * 30)
print(f"Numero de filas: {len(datos_casas)}")
print(f"Numero de columnas: {len(datos_casas.columns)}")
print(f"Columnas: {list(datos_casas.columns)}")


# EJERCICIO 1: Exploracion basica

print("EJERCICIO 1: EXPLORANDO DATOS")
print("=" * 40)

# Tarea 1: Dimensiones
filas, columnas = datos_casas.shape
print(f"Filas: {filas:,}")
print(f"Columnas: {columnas}")

# Tarea 2: Primeras 3 filas
print("\nPrimeras 3 filas:")
print(datos_casas.head(3))

# Tarea 3: Ultimas 3 filas
print("\nUltimas 3 filas:")
print(datos_casas.tail(3))

# Tarea 4: Total de registros
total = len(datos_casas)
print(f"\nTotal de casas: {total:,}")

# Tarea 5: Lista de columnas
print("\nColumnas disponibles:")
for i, col in enumerate(datos_casas.columns, 1):
    print(f"{i:2d}. {col}")

# EJERCICIO 2: Seleccion y analisis

print("EJERCICIO 2: ANALISIS DE PRECIOS")
print("=" * 40)

# Tarea 1: Seleccionar precios
precios = datos_casas['median_house_value']
print(f"Tipo: {type(precios)}")
print(f"Primeros 5 precios: {precios.head().tolist()}")

# Tarea 2: Coordenadas
ubicaciones = datos_casas[['longitude', 'latitude']]
print(f"\nDimensiones ubicaciones: {ubicaciones.shape}")
print("Primeras 3 coordenadas:")
print(ubicaciones.head(3))

# Tarea 3: Precio promedio
precio_promedio = precios.mean()
print(f"\nPrecio promedio: ${precio_promedio:,.2f}")

# Tarea 4: Precios extremos
precio_max = precios.max()
precio_min = precios.min()
print(f"Precio maximo: ${precio_max:,.2f}")
print(f"Precio minimo: ${precio_min:,.2f}")
print(f"Diferencia: ${precio_max - precio_min:,.2f}")

# Tarea 5: Casas de $500,000
casas_500k = (precios == 500000).sum()
print(f"\nCasas de $500,000: {casas_500k}")

# Informacion extra
print(f"\nPrecio mediano: ${precios.median():,.2f}")
print(f"Desviacion estandar: ${precios.std():,.2f}")