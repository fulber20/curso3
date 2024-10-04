altura=[4,5]
for i in range(altura[0]):
    print("* " * (i+1))
for i in range(altura[1]):
    print("* " * (altura[1]-i))

import numpy as np
numeros=np.arange(2,21,2)
cubo=np.power(numeros, 3)
print(cubo)