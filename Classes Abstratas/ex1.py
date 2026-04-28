from abc import ABC, abstractmethod

class Controlavel(ABC):
    @abstractmethod
    def mover(self):
        pass

class Jogador(Controlavel):
    def mover(self):
        print("Jogador se movendo")

class Volante(Controlavel):
    def mover(self):
        print("Volante girando")

meu_jogador = Jogador()
meu_volante = Volante()

meu_jogador.mover()
meu_volante.mover()