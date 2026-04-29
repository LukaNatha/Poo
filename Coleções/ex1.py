import random

Loteria = random.sample(range(1, 41), 40)
for numero in Loteria:
    print(f"Número sorteado: {numero}")

resultado = list(Loteria)
resultado.sort()
print(f"Lista de resultados: {resultado}")