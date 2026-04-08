from dataclasses import dataclass

@dataclass
class Processador:
    modelo: str
    velocidade: float

@dataclass
class Memoria:
    capacidade: int

class Computador:
    def __init__(self, modelo_cpu, velocidade, capacidade):
        self.processador = Processador(modelo_cpu, velocidade)
        self.memoria = Memoria(capacidade)

    def exibir_configuracao(self):
        print(self.processador.modelo, "-", self.processador.velocidade, "GHz")
        print(self.memoria.capacidade, "GB")

pc = Computador("i5", 3.2, 16)
pc.exibir_configuracao()