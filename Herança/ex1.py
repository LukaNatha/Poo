from dataclasses import dataclass

@dataclass
class Computador:
    processador: str
    memoria: int
    
@dataclass
class Laptop(Computador):
    bateria_watts: int = 0
    
@dataclass
class Desktop(Computador):
    gabinete: str = ""