f = open("nomes.txt", "w")
for i in range(5):
    nome = input(f"Digite o {i + 1}º nome: ")
    f.write(nome + "\n")
f.close()