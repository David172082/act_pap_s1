contador = 0
palabra = ""

while palabra != "fin":
    palabra = input("Introduce una palabra o 'fin' para terminar: ")
    if palabra != "fin":
        contador += 1

        print("Se ingresaron", contador, "palabras.")