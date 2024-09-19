def mostrarlista(lista, len):
    listaordenada=""
    for i in range(0,len):
        listaordenada+=str(lista[i])+" "
        print(listaordenada)
arreglo=[10,3,4,5,6,7,9,8,1]
for i in range(1,len(arreglo)):
    clave=arreglo[i]
    j=i-1
    while (j>=0 and arreglo[j]> clave):
        arreglo[j+1]=arreglo[j]
        j=j-1
        arreglo[j+1] = clave
    mostrarlista(arreglo, len(arreglo))
mostrarlista(arreglo, len(arreglo))

