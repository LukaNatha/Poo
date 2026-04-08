from dataclasses import dataclass

@dataclass
class Livro:
    titulo: str
    autor: str

class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar(self, livro):
        self.livros.append(livro)

    def listar_livros(self):
        for l in self.livros:
            print(l.titulo, "-", l.autor)

l1 = Livro("1984", "Orwell")
l2 = Livro("O Hobbit", "Tolkien")

b = Biblioteca("Central")
b.adicionar(l1)
b.adicionar(l2)

b.listar_livros()