from dataclasses import dataclass

@dataclass
class Professor:
    nome: str
    titulacao: str

@dataclass
class Disciplina:
    nome: str
    professor: Professor

    def exibir(self):
        print(self.nome)
        print(self.professor.nome, "-", self.professor.titulacao)

p = Professor("João", "Mestre")
d = Disciplina("Matemática", p)

d.exibir()