cubos_numeros=[]
for i in range(10):
    event_numer=2*( i +1)
    cubo=event_numer**3
    cubos_numeros.append(cubo)
    for cubo in cubos_numeros:
        print(cubo)
