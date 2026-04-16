# Código simple para análizar CSV con Pandas, NumPy y Seaborn
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from datetime import datetime
import warnings
import re

warnings.filterwarnings("ignore")

from os import system

if system("clear") != 0:
    system("cls")


# Configuración básica para gráficos más bonitos
plt.style.use("default")
sns.set_palette("Set2")
plt.rcParams["figure.figsize"] = (10, 6)

# ========================================
# 1. CARGAR TU ARCHIVO CSV
# ========================================
# CAMBIA 'tu_archivo.csv' por el nombre de tu archivo
archivo = "tiempos.csv"


try:
    df = pd.read_csv(archivo)
    print(f"✅ Archivo cargado exitosamente: {archivo}")
    print(f"Dimensiones: {df.shape[0]} filas, {df.shape[1]} columnas")
except FileNotFoundError:
    print(f"❌ No se encontró el archivo: {archivo}")
    print("Asegúrate de que el archivo esté en la misma carpeta")
    exit()

# ========================================
# 2. EXPLORAR LOS DATOS
# ========================================
print("\n" + "=" * 50)
print("INFORMACIÓN DE LOS DATOS")
print("=" * 50)

# Ver las primeras filas
print("\n📋 Primeras 5 filas:")
print(df.head())

# Ver nombres de columnas
print(f"\n📊 Columnas disponibles:")
for i, col in enumerate(df.columns, 1):
    print(f"  {i}. {col}")

# Información general
print(f"\n📈 Información general:")
print(df.info())

# Estadísticas básicas
print(f"\n📊 Estadísticas descriptivas:")
print(df.describe())

# ========================================
# 3. GRÁFICOS DE BARRAS AUTOMÁTICOS
# ========================================


def grafico_barras_simple(dataframe, columna, titulo="Gráfico de Barras"):
    """Crea un gráfico de barras simple"""
    plt.figure(figsize=(10, 6))

    if dataframe[columna].dtype == "object":  # Si es texto/categoría
        conteos = dataframe[columna].value_counts().head(10)
        sns.barplot(x=conteos.values, y=conteos.index)
        plt.xlabel("Frecuencia")
    else:  # Si es numérico, hacer bins
        plt.hist(dataframe[columna].dropna(), bins=20, alpha=0.7)
        plt.xlabel(columna)
        plt.ylabel("Frecuencia")

    plt.title(titulo)
    plt.tight_layout()
    plt.show()


def grafico_barras_doble(dataframe, col_x, col_y, titulo="Gráfico de Barras"):
    """Crea gráfico de barras con dos columnas"""
    plt.figure(figsize=(12, 6))

    if dataframe[col_x].dtype == "object":
        # Agrupar datos por categoría
        datos_agrupados = (
            dataframe.groupby(col_x)[col_y].mean().sort_values(ascending=False).head(10)
        )
        sns.barplot(x=datos_agrupados.index, y=datos_agrupados.values)
        plt.xticks(rotation=45)
    else:
        sns.scatterplot(data=dataframe, x=col_x, y=col_y)

    plt.title(titulo)
    plt.xlabel(col_x)
    plt.ylabel(col_y)
    plt.tight_layout()
    plt.show()


# ========================================
# 4. CREAR GRÁFICOS AUTOMÁTICAMENTE
# ========================================

print("\n" + "=" * 50)
print("GENERANDO GRÁFICOS AUTOMÁTICOS")
print("=" * 50)

# Obtener columnas numéricas y categóricas
columnas_numericas = df.select_dtypes(include=[np.number]).columns.tolist()
columnas_categoricas = df.select_dtypes(include=["object"]).columns.tolist()

print(f"\n📊 Columnas numéricas encontradas: {columnas_numericas}")
print(f"📝 Columnas categóricas encontradas: {columnas_categoricas}")

# Gráficos para columnas categóricas
if columnas_categoricas:
    print(f"\n🎯 Creando gráficos para columnas categóricas...")
    for col in columnas_categoricas[:3]:  # Solo las primeras 3
        grafico_barras_simple(df, col, f"Grafico de {col}")

# Gráficos para columnas numéricas
if columnas_numericas:
    print(f"\n📈 Creando gráficos para columnas numéricas...")
    for col in columnas_numericas[:3]:  # Solo las primeras 3
        grafico_barras_simple(df, col, f"Grafico de {col}")

# Gráfico combinado (si hay ambos tipos)
if columnas_categoricas and columnas_numericas:
    print(f"\n🔄 Creando gráfico combinado...")
    grafico_barras_doble(
        df,
        columnas_categoricas[0],
        columnas_numericas[0],
        f"{columnas_numericas[0]} por {columnas_categoricas[0]}",
    )

# ========================================
# 5. ANÁLISIS RÁPIDO CON NUMPY
# ========================================

if columnas_numericas:
    print("\n" + "=" * 50)
    print("ANÁLISIS ESTADÍSTICO CON NUMPY")
    print("=" * 50)

    for col in columnas_numericas[:3]:
        datos = df[col].dropna()  # Quitar valores nulos
        print(f"\n📊 Análisis de {col}:")
        print(f"  • Promedio: {np.mean(datos):.2f}")
        print(f"  • Mediana: {np.median(datos):.2f}")
        print(f"  • Desviación estándar: {np.std(datos):.2f}")
        print(f"  • Valor mínimo: {np.min(datos):.2f}")
        print(f"  • Valor máximo: {np.max(datos):.2f}")

# ========================================
# 6. MATRIZ DE CORRELACIÓN (SEABORN)
# ========================================
import seaborn as sns

if len(columnas_numericas) > 1:
    print(f"\n🔗 Creando matriz de correlación...")
    plt.figure(figsize=(10, 8))

    # Calcular correlaciones
    correlaciones = df[columnas_numericas].corr()

    # Crear heatmap
    sns.heatmap(
        correlaciones, annot=True, cmap="coolwarm", center=0, square=True, fmt=".2f"
    )
    plt.title("Matriz de Correlación entre Variables Numéricas")
    plt.tight_layout()
    plt.show()

    print("Correlaciones calculadas y visualizadas ✅")

# ========================================
# 7. RESUMEN FINAL
# ========================================

print("\n" + "=" * 60)
print("RESUMEN DEL ANÁLISIS")
print("=" * 60)
print(f"📁 Archivo analizado: {archivo}")
print(f"📊 Total de filas: {df.shape[0]:,}")
print(f"📋 Total de columnas: {df.shape[1]}")
print(f"🔢 Columnas numéricas: {len(columnas_numericas)}")
print(f"📝 Columnas categóricas: {len(columnas_categoricas)}")

# Mostrar valores nulos
nulos = df.isnull().sum()
if nulos.sum() > 0:
    print(f"\n⚠️  Valores faltantes encontrados:")
    for col, cantidad in nulos[nulos > 0].items():
        print(f"  • {col}: {cantidad} valores nulos")
else:
    print(f"\n✅ No hay valores faltantes")

print(f"\n🎉 Análisis completado exitosamente!")

# ========================================
# INSTRUCCIONES DE USO
# ========================================

print("\n" + "=" * 60)
print("INSTRUCCIONES PARA PERSONALIZAR")
print("=" * 60)
print(
    """
🔧 PARA USAR CON TU ARCHIVO:
1. Cambia la línea: archivo = 'tu_archivo.csv'
2. Pon el nombre real de tu archivo CSV
3. Ejecuta el script

📊 PARA GRÁFICOS ESPECÍFICOS:
1. Usa: grafico_barras_simple(df, 'nombre_columna')
2. Usa: grafico_barras_doble(df, 'columna_x', 'columna_y')

💡 EJEMPLOS:
• grafico_barras_simple(df, 'categoria')
• grafico_barras_doble(df, 'mes', 'ventas')
• df.groupby('categoria')['precio'].mean()
"""
)
