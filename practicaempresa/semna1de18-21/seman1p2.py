import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Datos de ejemplo
x = np.random.rand(100, 2)
#modelo kMeans
KMeans=KMeans(n_clusters=3)
KMeans.fit(x)
# obtener etiquetas cluters
labels=KMeans.labels_

#vizualizacion
plt.scatter(x[:, 0], x[:, 1], c=labels, cmap='viridis')
plt.title('k-Means clustering')
plt.show()