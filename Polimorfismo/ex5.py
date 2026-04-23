from abc import ABC, abstractmethod
from dataclasses import dataclass
import math

class FormaGeometria(ABC):
    @abstractmethod
    def calcular_area(self):
        pass

@dataclass
class Circulo(FormaGeometria):
    raio: float
    
    def calcular_area(self):
        return math.pi * self.raio ** 2

@dataclass
class Retangulo(FormaGeometria):
    largura: float
    altura: float
    
    def calcular_area(self):
        return self.largura * self.altura

@dataclass
class Triangulo(FormaGeometria):
    base: float
    altura: float
    
    def calcular_area(self):
        return (self.base * self.altura) / 2

formas = [Circulo(3), Retangulo(4, 5), Triangulo(6, 2)]

for forma in formas:
    print(forma.calcular_area())
    