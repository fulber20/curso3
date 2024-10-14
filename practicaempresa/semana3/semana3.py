import pandas as pd

# Clasificaciones de estudiantes
clasificaciones = ['A', 'B', 'A', 'C', 'B', 'A', 'C', 'B', 'A', 'C']

# Crear un DataFrame
df_clasificaciones = pd.DataFrame(clasificaciones, columns=['Clasificacion'])

# Calcular la frecuencia de cada clasificación
frecuencia_clasificaciones = df_clasificaciones['Clasificacion'].value_counts()

# Imprimir resultados
print("\nFrecuencia de Clasificaciones:")
print(frecuencia_clasificaciones)
