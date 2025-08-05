import random

numero_secreto = random.randint(1, 10)
adivinza = 0

while adivinza != numero_secreto:
    adivinza = int(input("Adivina el número secreto entre 1 y 10: "))

print("¡Felicidades! Has adivinado el número secreto:", numero_secreto)