# Importar librerias
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

from os import system

if system("clear") != 0:
    system("cls")

print("Librerias importadas correctamente")
print(f"Pandas version: {pd.__version__}")
print(f"NumPy version: {np.__version__}")

# carga data set de cargo-data colombia
data_carga = pd.read_csv("tiemposlogisticos.csv")


print("Datos cargados exitosamente")
print(f"Dimensiones: {data_carga.shape}")
print("\nPrimeras 5 filas:")
print(data_carga.head())


# Informacion basica del dataset de cargo
print("INFORMACION DEL DATASET")
print("=" * 30)
print(f"Numero de filas: {len(data_carga)}")
print(f"Numero de columnas: {len(data_carga.columns)}")
print(f"Columnas: {list(data_carga.columns)}")
print("\nINFORMACION DETALLADA:")
data_carga.info()

# EJERCICIO 1: Exploracion basica

print("EJERCICIO 1: EXPLORANDO DATOS")
print("=" * 40)

# Tarea 1: Dimensiones
filas, columnas = data_carga.shape
print(f"Filas: {filas:,}")
print(f"Columnas: {columnas}")

# Tarea 2: Primeras 3 filas
print("\nPrimeras 3 filas:")
print(data_carga.head(3))

# Tarea 3: Ultimas 3 filas
print("\nUltimas 3 filas:")
print(data_carga.tail(3))

# Tarea 4: Total de registros
total = len(data_carga)
print(f"\nTotal de campos: {total:,}")

# Tarea 5: Lista de columnas
print("\nColumnas disponibles:")
for i, col in enumerate(data_carga.columns, 1):
    print(f"{i:2d}. {col}")

# EJERCICIO 2: Seleccion y analisis

print("EJERCICIO 2: ANALISIS DE TIEMPOS")
print("=" * 40)

# Tarea 1: Seleccionar tiempo
tiempos = data_carga["tiempo_real_horas"]
print(f"Tipo: {type(tiempos)}")
print(f"Primeros 5 tiempos: {tiempos.head().tolist()}")

# seleccion de costos
costos = data_carga["costo_cop"]
print(f"Tipo: {type(costos)}")
print(f"Primeros 5 costos: {costos.head().tolist()}")

# Tarea 3: costo promedio
costos_promedio = costos.mean()
print(f"\nPrecio promedio: ${costos_promedio:,.2f}")
