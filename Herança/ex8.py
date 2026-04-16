from dataclasses import dataclass
#coloquei algo no motor e no Motor eletrico para não deixar sem nada(pass)
class Motor:
    def potencia(self):
        return 0

@dataclass
class Carro:
    motor: Motor

class MotorEletrico(Motor):
    def potencia(self):
        return 100

@dataclass
class CarroEletrico(Carro):
    motor: MotorEletrico
    