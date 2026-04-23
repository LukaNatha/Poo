class Veículo:
    def mover(self):
        return "Veículo se movendo"

class Carro(Veículo):
    def mover(self):
        return "Carro acelerando"

class Moto(Veículo):
    def mover(self):
        return "Moto empinando"

class Bicicleta(Veículo):
    def mover(self):
        return "Bicicleta pedalando"

veiculos = [Carro(), Moto(), Bicicleta(), Veículo()]
for veiculo in veiculos:
    print(veiculo.mover())