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
Animal = [Cachorro(), Gato()]
for animais in Animal:
    print(animais.emitir_som())