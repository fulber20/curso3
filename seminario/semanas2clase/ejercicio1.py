def lista_datos(lista):
  numeros_visto=set()
  for numero in lista:
    complemento= -numero
    if complemento in numeros_visto:
      return(numero,complemento)
    numeros_visto.add(numero)
  return None
lista_datos_num=[5, 2, 3, 8,-5, -8, 1]
resultado=lista_datos(lista_datos_num)
if resultado:
    print(f"numeros que suman cero {resultado[0]} y {resultado[1]}")
else:
    print("no se encontraron numeros que suman cero")