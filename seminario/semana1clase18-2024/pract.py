def encontrar_palabra(lista_palabras):
    palabra_mas_larga=""
    for palabra in lista_palabras:
        if len(palabra)>len(palabra_mas_larga):
            palabra_mas_larga=palabra
    return palabra_mas_larga
entrada=input("ingreasa la lista de palabras: ")
lista_de_palabras=[palabra.strip() for palabra in entrada.split(" ")]
resultado= encontrar_palabra(lista_de_palabras)
print("la palbra mas larga es : ", resultado)