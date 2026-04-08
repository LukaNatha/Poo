from dataclasses import dataclass
@dataclass
class Motor:
    potencia: int
    
    def ligar(self):
        print(f"Motor de {self.potencia} cavalos ligado")
        
@dataclass
class Carro:
    modelo: str
    motor: Motor
    
    def ligar_carro(self):
        print(f"Ligando o carro {self.modelo}")
        self.motor.ligar()

m = Motor(150)
c = Carro("Civic", m)

c.ligar_carro()
