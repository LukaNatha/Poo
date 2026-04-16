from dataclasses import dataclass

@dataclass
class Motor:
    potencia: int
    
    def ligar_motor(self):
        return f"Motor de {self.potencia} cavalos"

@dataclass
class Eletrico:
    bateria: int
    
    def carregar(self):
        return f"Carregando bateria de {self.bateria}Ah" #fiqui em duvida da medida e pesquisei e coloquei amperes por hora

@dataclass
class Combustao:
    tanque: int
    
    def abastecer(self):
        return f"Abastecendo tanque de {self.tanque} litros"

@dataclass
class CarroEletrico(Motor, Eletrico):
    def ligar(self):
        return f"{self.ligar_motor()} e {self.carregar()}"

@dataclass
class CarroHibrido(Motor, Eletrico, Combustao):
    def ligar(self):
        return f"{self.ligar_motor()}, {self.carregar()} e {self.abastecer()}"
    
    
    