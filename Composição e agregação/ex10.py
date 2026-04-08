from dataclasses import dataclass

@dataclass
class Aluno:
    nome: str

class Turma:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno):
        self.alunos.append(aluno)

class Escola:
    def __init__(self, nome):
        self.nome = nome
        self.turmas = []

    def adicionar_turma(self, turma):
        self.turmas.append(turma)

    def exibir(self):
        for t in self.turmas:
            print("Turma:", t.nome)
            for a in t.alunos:
                print("-", a.nome)

a1 = Aluno("Lucca")
a2 = Aluno("João")

t = Turma("1A")
t.adicionar_aluno(a1)
t.adicionar_aluno(a2)

e = Escola("IFRN")
e.adicionar_turma(t)

e.exibir()