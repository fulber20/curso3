def mostrarlista(lista, len):
    listaordenado=""
    for i in range(0,len):
        listaordenado+=str(lista[i])+" "
    print(listaordenado)
arreglo=[5,6,8,2,4,3,1,7]
for i in range(1,len(arreglo)):
    clave=arreglo[i]
    j=i-1
    while (j>=0 and arreglo[j] > clave):
        arreglo[j+1] = arreglo[j]
        j=j-1 
        arreglo[j+1] = clave
    mostrarlista(arreglo, len(arreglo))