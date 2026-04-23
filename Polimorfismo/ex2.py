from dataclasses import dataclass

@dataclass
class Animal:
    def emitir_som(self):
        return "Algum som genérico"

@dataclass
class Cachorro(Animal):
    def emitir_som(self):
        som_original = super().emitir_som()
        print("Som original:", som_original)
        return "Cachorro:Au Au"

@dataclass
class Gato(Animal):
    def emitir_som(self):
        som_original = super().emitir_som()
        print("Som original:", som_original)
        return "Gato: Miado"
    
animais = [Cachorro(), Gato(), Animal()]
for animal in animais:
    print()
    print(animal.emitir_som())
