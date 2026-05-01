frase = input("Digite uma frase: ")

frase = frase.lower()
pontuacoes = [".", ",", "!", "?", ";"]
for p in pontuacoes:
    frase = frase.replace(p, "")

palavras = frase.split()
unicas = set(palavras)

frequencia = {}
for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] = frequencia[palavra] + 1
    else:
        frequencia[palavra] = 1

print("\nPalavras únicas:")
unicas_ordenadas = sorted(unicas)
for p in unicas_ordenadas:
    print(p)

print("\nFrequência das palavras:")
palavras_na_ordem = sorted(frequencia)
for p in palavras_na_ordem:
    print(p + ":", frequencia[p])
