def mostrarlista(lista, len):
    listaordenada=""
    for i in range(0,len):
        listaordenada+=str(lista[i])+" "
    print(listaordenada)
arreglo=[5,4,3,2,1]
for i in range(1,len(arreglo)):
    clave=arreglo[i]
    j=i-1
    while (j>=0 and arreglo[j] > clave):
         arreglo[j+1]=arreglo[j]
         j=j-1
         arreglo[j+1]=clave
    mostrarlista(arreglo,len(arreglo))