class Veiculo:
    def acelerar(self):
        return "Veiculo Acelerando"

class Carro(Veiculo):
    def acelerar(self):
        return "Carro Acelerando"

class Moto(Veiculo):
    def acelerar(self):
        return "Moto Acelerando"

veiculos = [Carro(), Moto()]

for v in veiculos:
    print(v.acelerar())