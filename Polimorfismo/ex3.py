class Animal:
    def emitir_som(self):
        return "Som genérico"

class Cachorro(Animal):
    def emitir_som(self):
        return "Latido: Au Au"

class Gato(Animal):
    def emitir_som(self):
        return "Miado: Miau"

animais = [Cachorro(), Gato(), Animal()]
for animal in animais:
    print(animal.emitir_som())
