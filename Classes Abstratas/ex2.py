from abc import ABC, abstractmethod

class DispositivoEletronico(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass

class Carregavel(ABC):
    @abstractmethod
    def carregar(self):
        pass

class Smartphone(DispositivoEletronico, Carregavel):
    def ligar(self):
        return "Smartphone: Ligando..."
    def desligar(self):
        return "Smartphone: Desligando..."
    def carregar(self):
        return "Smartphone: Carregando bateria..."

class Notebook(DispositivoEletronico, Carregavel):
    def ligar(self):
        return "Notebook: Ligando..."
    def desligar(self):
        return "Notebook: Desligando..."
    def carregar(self):
        return "Notebook: Carregando bateria..."

class FoneDeOuvido(DispositivoEletronico):
    def ligar(self):
        return "Fone de Ouvido: Ligando..."
    def desligar(self):
        return "Fone de Ouvido: Desligando..."

celular = Smartphone()
laptop = Notebook()
fones = FoneDeOuvido()

lista_dispositivos = [celular, laptop, fones]
lista_carregaveis = [celular, laptop]

print("Ligar e desligar")
for d in lista_dispositivos:
    print(d.ligar())
    print(d.desligar())

print("\nCarregar")
for c in lista_carregaveis:
    print(c.carregar())