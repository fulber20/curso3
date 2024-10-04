import numpy as np
def lista_datos(lista):
    array= np.array(lista)
    for numero in array:
        if -numero in array:
            return(numero,  -numero)
    return None
lista_num=[5, 2, 3, 8, -8, 1]
resultado=lista_datos(lista_num)
if resultado:
    print(f"los numeros que suman cero son: {resultado[0]} y {resultado[1]}.")
else:
    print("no se encontraron los nueros que suman cero.")        