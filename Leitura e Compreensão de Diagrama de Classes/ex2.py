class Carro:
    def __init__(self, marca: str, modelo: str, ano: int):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano

    def ligar(self):
        print("O carro está ligado!")

    def desligar(self):
        print("O carro está desligado!")

meu_carro = Carro("Toyota", "Corolla", 2026)
print(f"Carro: {meu_carro.marca} {meu_carro.modelo} ({meu_carro.ano})")
meu_carro.ligar()
meu_carro.desligar()
