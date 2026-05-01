contagem = {}

while True:
    entrada = input("Ano de nascimento (Enter para sair): ")
    
    if entrada == "":
        break
    ano = int(entrada)
    
    if ano in contagem:
        contagem[ano] = contagem[ano] + 1
    else:
        contagem[ano] = 1

print("Relatório:")

for ano in contagem:
    quantidade = contagem[ano]
    print("Ano", ano, ":", quantidade, "pessoa(s)")