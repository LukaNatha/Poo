from dataclasses import dataclass

@dataclass
class Jogador:
    nome: str
    posicao: str

@dataclass
class Time:
    nome: str
    jogadores: list

    def listar_jogadores(self):
        for j in self.jogadores:
            print(j.nome, "-", j.posicao)

j1 = Jogador("Neymar", "Atacante")
j2 = Jogador("Casemiro", "Volante")

time = Time("Brasil", [j1, j2])
time.listar_jogadores()