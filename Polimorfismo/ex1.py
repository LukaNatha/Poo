class Animal:
    def emitir_som(self):
        return "Algum som genérico"

class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au"
    
class Gato(Animal):
    def emitir_som(self):
        return "Miau"

animais = [Cachorro(), Gato(), Animal()]

for animal in animais:
    print(animal.emitir_som())