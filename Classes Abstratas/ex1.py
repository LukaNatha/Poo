from abc import ABC, abstractmethod
from dataclasses import dataclass

@dataclass
class DispostivoEletronico(ABC):
    @abstractmethod
    def ligar(self):
        pass
    @abstractmethod
    def desligar(self):
        pass

@dataclass
class Carregavel(ABC):
