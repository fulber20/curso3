import numpy as np

datos = [10, 12, 23, 23, 16, 23, 21, 16]

media = np.mean(datos)

varianza = np.var(datos, ddof=1)

desviacion_estandar = np.std(datos, ddof=1)  

print(f"Datos: {datos}")
print(f"Media: {media}")
print(f"Varianza: {varianza}")
print(f"Desviación Estándar: {desviacion_estandar}")
