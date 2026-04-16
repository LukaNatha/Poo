class Nadador:
    def mover(self):
        return "Nadar"

class Corredor:
    def mover(self):
        return "Correr"

class Triatleta(Nadador, Corredor):
    def mover(self):
        return f"{Nadador.mover(self)} e {Corredor.mover(self)}"

t = Triatleta()
print(t.mover())