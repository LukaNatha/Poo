def adicionar_valor():
    inicial = int(input("Valor incial: "))
    adicional = int(input("Valor adicional: "))
    if adicional <= 0:
        raise Exception ("Somente valores positivos devem ser adicionados ao valor inicial")
    return inicial + adicional

print("Teste com valor positivo")
try:
    resultado = adicionar_valor()
    print(f"Resultado: {resultado}")
except Exception as erro:
      print(f"Erro: {erro}")
    
print("Teste com valor negativo")

try:
     resultado = adicionar_valor()
     print(f"Resultado: {resultado}")
except Exception as erro:
    print(f"Erro: {erro}")     