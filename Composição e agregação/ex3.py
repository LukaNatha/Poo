from dataclasses import dataclass

@dataclass
class Autor:
    nome: str

@dataclass
class Livro:
    titulo: str
    autor: Autor

autor = Autor("Machado de Assis")
livro = Livro("Dom Casmurro", autor)

print(livro.titulo, "-", livro.autor.nome)