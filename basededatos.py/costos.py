# ==========================================
# DESCRIPCIÓN ESTADÍSTICA DEL COSTO (COP)
# ==========================================

import numpy as np

# 1. Cargar el archivo CSV
data = np.genfromtxt("tiempos.csv", delimiter=",", dtype=str, skip_header=1)

# 2. Extraer la columna costo_cop (índice 13)
costo = data[:, 13].astype(float)

# 3. Calcular estadísticas descriptivas
costo_min = np.min(costo)
costo_max = np.max(costo)
costo_promedio = np.mean(costo)
costo_mediana = np.median(costo)
costo_desv_std = np.std(costo)
costo_q1 = np.percentile(costo, 25)
costo_q3 = np.percentile(costo, 75)

# 4. Mostrar resultados
print("💰 Descripción Estadística del Costo (COP):")
print(f"- Total de registros: {len(costo)}")
print(f"- Costo mínimo: {costo_min:,.2f} COP")
print(f"- Costo máximo: {costo_max:,.2f} COP")
print(f"- Costo promedio: {costo_promedio:,.2f} COP")
print(f"- Mediana: {costo_mediana:,.2f} COP")
print(f"- Desviación estándar: {costo_desv_std:,.2f} COP")
print(f"- Q1 (25%): {costo_q1:,.2f} COP")
print(f"- Q3 (75%): {costo_q3:,.2f} COP")

# 5. Preparar datos para gráfico
etiquetas = ["Mínimo", "Q1 (25%)", "Mediana", "Promedio", "Q3 (75%)", "Máximo"]
valores = [costo_min, costo_q1, costo_mediana, costo_promedio, costo_q3, costo_max]

# 6. Configurar estilo
plt.figure(figsize=(10, 6))
sns.set_palette("Set2")

# 7. Crear gráfico de barras
barras = plt.bar(etiquetas, valores)

# Agregar los valores sobre cada barra
for barra in barras:
    plt.text(
        barra.get_x() + barra.get_width() / 2,
        barra.get_height(),
        f"{barra.get_height():,.0f}",
        ha="center",
        va="bottom",
    )

# 8. Personalizar gráfico
plt.title("Estadística del Costo de los Envíos (COP)")
plt.ylabel("Costo en COP")
plt.xticks(rotation=30)
plt.grid(axis="y", linestyle="--", alpha=0.6)

# 9. Mostrar gráfico
plt.tight_layout()
plt.show()
