import re
def contraseña_valida(contraseña):
    if len(contraseña) < 6 or len(contraseña) > 16:
        return False
    elif not re.search(r'[a-z]', contraseña):
        return False
    elif not re.search(r'[A-Z]', contraseña):
        return False
    elif not re.search(r'[0-9]', contraseña):
        return False
    elif not re.search(r'[$#@]', contraseña):
        return False
    return True
contraseña = input("Ingresa una contraseña: ")
if contraseña_valida(contraseña):
    print("La contraseña es válida.")
else:
    print("La contraseña no es válida.")
