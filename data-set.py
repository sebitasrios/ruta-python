# Importar librerías necesarias
import pandas as pd                    # Librería para manejo de bases de datos
import seaborn as sns                  # Librería para visualización gráfica
import matplotlib.pyplot as plt        # Librería para gráficos
from mpl_toolkits.mplot3d import Axes3D  # Para gráficos 3D

# Configurar visualización en español (opcional)
plt.rcParams['figure.figsize'] = (10, 6)
sns.set_style("whitegrid")

print("Librerías importadas correctamente")

# Cargar el dataset de tiempos logísticos
try:
    df_logisticos = pd.read_excel("tiempos.xlsx   ")  # Asegúrate de que el archivo esté en la carpeta correcta
    print("Archivo de tiempos logísticos leído correctamente")
    print(f"Dimensiones: {df_logisticos.shape}")
    print("\nPrimeras 5 filas del dataset de tiempos logísticos:")
    print(df_logisticos.head())
    
    print("\nInformación general del dataset:")
    print(df_logisticos.info())
    
    print("\nEstadísticas descriptivas:")
    print(df_logisticos.describe())
    
except FileNotFoundError:
    print("Archivo 'tiemposlogisticos.csv' no encontrado.")
    print("Verifica que esté en la carpeta correcta.")
except Exception as e:
    print(f"Error al cargar el archivo: {e}")