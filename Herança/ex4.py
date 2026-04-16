from dataclasses import dataclass

class Forma:
    def area(self):
        return 0
    
@dataclass
class Retangulo(Forma):
    largura: int
    altura: int
    
    def area(self):
        return self.largura * self.altura