def fibonacci(n):
    secuencia = []
    for i in range(n):
        if i == 0:
            secuencia.append(0)  
        elif i == 1:
            secuencia.append(1)  
        else:
            secuencia.append(secuencia[i - 1] + secuencia[i - 2])
    return secuencia
num_terminos = int(input("Ingresa el número de términos de Fibonacci que deseas: "))
resultado = fibonacci(num_terminos)
print("Secuencia de Fibonacci:", resultado)