from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    salario: float
    
    def exibir_dados(self):
        return f"Nome: {self.nome} e Salário: {self.salario}"

@dataclass
class Gerente(Funcionario):
    bonus: float = 0.0
    
    def exibir_dados(self):
        return f"Nome: {self.nome}, Salário: {self.salario} e Bônus: {self.bonus}"

@dataclass
class Desenvolvedor(Funcionario):
    linguagem: str = ""
    
    def exibir_dados(self):
        return f"Nome: {self.nome}, Salário: {self.salario} e Linguagem: {self.linguagem}"

g = Gerente("José", 5000, 700)
d = Desenvolvedor("Lucca", 3500, "Python")

print(g.exibir_dados())
print()
print(d.exibir_dados())