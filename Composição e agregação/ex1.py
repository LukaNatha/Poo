from dataclasses import dataclass

@dataclass
class Cidade:
    __nome: str
    
    @property
    def nome(self):
        return self.__nome


@dataclass
class Pessoa:
    __nome: str
    __cidade: Cidade
    
    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def cidade(self):
        return self.__cidade

    @cidade.setter
    def cidade(self, valor):
        self.__cidade = valor


@dataclass
class Animal:
    __nome: str
    __dono: Pessoa

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, valor):
        self.__nome = valor

    @property
    def dono(self):
        return self.__dono

    @dono.setter
    def dono(self, valor):
        self.__dono = valor


C = Cidade("Ceara-Mirim")
P = Pessoa("Lucca", C)
A = Animal("Gato", P)

print(A.dono.nome)
print(A.dono.cidade.nome)
print(A.nome)