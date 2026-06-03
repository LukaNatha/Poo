arquivo = open("convidados.txt", "r")

linhas = arquivo.readlines()
total_linhas = len(linhas)

arquivo.close()

print(f"O arquivo possui o total de {total_linhas} linhas.")