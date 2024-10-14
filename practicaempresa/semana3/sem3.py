import numpy as np
import pandas as pd
from scipy import stats

# Crear un conjunto de datos de ejemplo
data = {
    'Edad': [20, 21, 22, 23, 22, 21, 24, 25, 20, 21],
    'Satisfaccion': ['Alta', 'Media', 'Alta', 'Baja', 'Media', 'Alta', 'Media', 'Alta', 'Baja', 'Alta']
}

# Crear un DataFrame de pandas
df = pd.DataFrame(data)

# Calcular medidas de tendencia central
media_edad = np.mean(df['Edad'])
mediana_edad = np.median(df['Edad'])
moda_edad = stats.mode(df['Edad'])[0][0]

# Calcular medidas de dispersión
rango_edad = np.ptp(df['Edad'])  # Rango
varianza_edad = np.var(df['Edad'], ddof=0)  # Varianza
desviacion_estandar_edad = np.std(df['Edad'], ddof=0)  # Desviación estándar

# Imprimir resultados
print("Análisis de Edad:")
print(f"Media: {media_edad}")
print(f"Mediana: {mediana_edad}")
print(f"Moda: {moda_edad}")
print(f"Rango: {rango_edad}")
print(f"Varianza: {varianza_edad}")
print(f"Desviación Estándar: {desviacion_estandar_edad}")

# Calcular la frecuencia de satisfacción
frecuencia_satisfaccion = df['Satisfaccion'].value_counts()

print("\nFrecuencia de Satisfacción:")
print(frecuencia_satisfaccion)
