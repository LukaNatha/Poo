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

for ano in sorted(contagem):
    print("Data de Nascimento:", ano, "-", "Pessoas:", contagem[ano])