import numpy as np
from scipy import stats


# Calificaciones de un examen
calificaciones = [85, 90, 78, 92, 88, 76, 95]

# Calcular medidas de tendencia central
media_calificaciones = np.mean(calificaciones)
mediana_calificaciones = np.median(calificaciones)
moda_calificaciones = stats.mode(calificaciones)[0][0]

# Calcular medidas de dispersión
varianza_calificaciones = np.var(calificaciones, ddof=0)
desviacion_estandar_calificaciones = np.std(calificaciones, ddof=0)

# Imprimir resultados
print("\nAnálisis de Calificaciones:")
print(f"Media: {media_calificaciones:.2f}")
print(f"Mediana: {mediana_calificaciones:.2f}")
print(f"Moda: {moda_calificaciones}")
print(f"Varianza: {varianza_calificaciones:.2f}")
print(f"Desviación Estándar: {desviacion_estandar_calificaciones:.2f}")
