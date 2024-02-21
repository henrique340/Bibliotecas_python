import random

numero_aleatorio = random.randint(1, 100)
elemento_aleatorio = random.choice([1, 2, 5, 7, 12, 51, 99])
lista = [1, 3, 5, 12, 15, 16, 71, 132]
embaralhar = random.shuffle(lista)

print(numero_aleatorio)
print(elemento_aleatorio)
print(lista)