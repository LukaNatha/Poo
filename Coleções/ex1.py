import random

Loteria = random.sample(range(1, 41), 25)
resultado = list(Loteria)
resultado.sort()
print(f"Lista de resultados: {resultado}")