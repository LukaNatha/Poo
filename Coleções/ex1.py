import random

Loteria = random.sample(range(1, 41), 25)
Loteria.sort()
print(f"Lista de resultados: {Loteria}")