from dataclasses import dataclass

@dataclass
class Animal:
    def emitir_som(self):
        return "Algum som genérico"

@dataclass
class Cachorro(Animal):
    def emitir_som(self):
        super().emitir_som()
        return "Au Au"
@dataclass
class Gato(Animal):
    def emitir_som(self):
        super().emitir_som()
        return "Miau"
animais = [Animal(Cachorro, Gato)]
for animal in animais:
    print(animal.emitir_som(Gato, Cachorro))