numero = input("Introduce un número: ")
suma = 0

for digito in numero:
    suma += int(digito)

print(f"La suma de los dígitos del número {numero} es {suma}.")