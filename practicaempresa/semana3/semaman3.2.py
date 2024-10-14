import numpy as np

# Datos de temperaturas en grados Celsius
temperaturas = [22, 24, 20, 19, 23, 21, 25]

# Calcular medidas de tendencia central
media_temp = np.mean(temperaturas)
mediana_temp = np.median(temperaturas)

# Calcular medidas de dispersión
varianza_temp = np.var(temperaturas, ddof=0)
desviacion_estandar_temp = np.std(temperaturas, ddof=0)

# Imprimir resultados
print("Análisis de Temperaturas:")
print(f"Media: {media_temp:.2f}")
print(f"Mediana: {mediana_temp:.2f}")
print(f"Varianza: {varianza_temp:.2f}")
print(f"Desviación Estándar: {desviacion_estandar_temp:.2f}")
