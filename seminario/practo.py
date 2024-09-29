def fibonacci(n):
    secuencia=[]
    for i in range(n):
        if i==0:
         secuencia.append(0)
        elif i==1:
           secuencia.append(1)
        else: 
           secuencia.append(secuencia[i -1] + secuencia[i-2])
    return secuencia
num_termino=int(input("ingrese el numero de secuencias que deseas: "))
resulatado=fibonacci(num_termino)
print("secuencia de fibonaci: ",resulatado)