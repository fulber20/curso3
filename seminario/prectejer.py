while True:
    edad=int(input("ingrese su edad:"))
    if edad<=0 or edad>=100:
        print("!ERROR! no existe esa edad.")
    else:
        break
if edad>=70:
    print("no es obligatorio votar. ")
elif edad>=18:
    print("si puede votar. ")
else:
    print("no puede votar. ")