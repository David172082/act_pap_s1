mayor = 0
edad = int(input("Ingresa una edad (o -1 para terminar): "))

while edad != -1:
    if edad > mayor:
        mayor = edad
    edad = int(input("Ingresa una edad o -1 para terminar: "))

print("La edad mayor ingresada es:", mayor)