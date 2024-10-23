import numpy as np

# Datos de ventas en miles de dólares
ventas = [15, 20, 18, 25, 30, 22, 17]

# Calcular medidas de tendencia central
media_ventas = np.mean(ventas)
mediana_ventas = np.median(ventas)

# Calcular medidas de dispersión
rango_ventas = np.ptp(ventas)  # Rango
varianza_ventas = np.var(ventas, ddof=0)
desviacion_estandar_ventas = np.std(ventas, ddof=0)

# Imprimir resultados
print("\nAnálisis de Ventas:")
print(f"Media: {media_ventas:.2f}")
print(f"Mediana: {mediana_ventas:.2f}")
print(f"Rango: {rango_ventas}")
print(f"Varianza: {varianza_ventas:.2f}")
print(f"Desviación Estándar: {desviacion_estandar_ventas:.2f}")

