numero = input("Ingresa los números dejando espacio en cada número: ").split()
repetidos = []

for num in numero:
    if numero.count(num) > 1 and num not in repetidos:
        repetidos.append(num)

if repetidos:
    print("Números repetidos:", repetidos)
else:
    print("No hay números repetidos")
