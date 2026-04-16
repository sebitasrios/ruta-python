# ==========================================
# DESCRIPCIÓN ESTADÍSTICA DEL PESO (kg)
# ==========================================

import numpy as np

# 1. Cargar el archivo
data = np.genfromtxt("tiempos.csv", delimiter=",", dtype=str, skip_header=1)

# 2. Extraer la columna peso_kg (índice 8)
peso = data[:, 8].astype(float)

# 3. Calcular estadísticas descriptivas
peso_min = np.min(peso)
peso_max = np.max(peso)
peso_promedio = np.mean(peso)
peso_mediana = np.median(peso)
peso_desv_std = np.std(peso)
peso_q1 = np.percentile(peso, 25)
peso_q3 = np.percentile(peso, 75)

# 4. Mostrar resultados
print("📊 Descripción Estadística del Peso (kg):")
print(f"- Total de registros: {len(peso)}")
print(f"- Peso mínimo: {peso_min:.2f} kg")
print(f"- Peso máximo: {peso_max:.2f} kg")
print(f"- Peso promedio: {peso_promedio:.2f} kg")
print(f"- Mediana: {peso_mediana:.2f} kg")
print(f"- Desviación estándar: {peso_desv_std:.2f} kg")
print(f"- Q1 (25%): {peso_q1:.2f} kg")
print(f"- Q3 (75%): {peso_q3:.2f} kg")