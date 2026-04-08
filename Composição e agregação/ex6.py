from dataclasses import dataclass

@dataclass
class Comodo:
    nome: str
    tamanho: int

class Casa:
    def __init__(self):
        self.comodos = []

    def adicionar_comodo(self, nome, tamanho):
        c = Comodo(nome, tamanho)
        self.comodos.append(c)

    def listar(self):
        for c in self.comodos:
            print(c.nome, "-", c.tamanho)

casa = Casa()
casa.adicionar_comodo("Quarto", 12)
casa.adicionar_comodo("Sala", 20)

casa.listar()