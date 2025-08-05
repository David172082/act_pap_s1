n = int(input("Ingrese un número: "))
factorial = 1
contador = 1

while contador <= n:
    factorial *= contador
    contador += 1

print(f"El factorial de {n} es: {factorial}")