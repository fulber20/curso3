#deasrrolle  un algoritmo para encontrar la palabra mas larga de una lista de palbras ingresada.
def encontrar_palabra(lista_palabras):
    palabra_mas_larga = ""
    for palabra in lista_palabras:
        if len(palabra) > len(palabra_mas_larga):
            palabra_mas_larga = palabra      
    return palabra_mas_larga
entrada = input("Ingresa litas de palabras: ")
lista_de_palabras = [palabra.strip() for palabra in entrada.split(",")]
resultado = encontrar_palabra(lista_de_palabras)
print("La palabra más larga es:", resultado)
