from dataclasses import dataclass

@dataclass
class Motor:
    potencia: int
    
    def ligar_motor(self):
        return f"Motor de {self.potencia} cavalos"
    
    def exibir_info(self):
        return f"Potência: {self.potencia} cavalos"

@dataclass
class Eletrico:
    bateria: int
    
    def carregar(self):
        return f"Carregando bateria de {self.bateria}Ah" 
    def exibir_info(self):
        return f"Bateria: {self.bateria} Ah" 

@dataclass
class Combustao:
    tanque: int
    
    def abastecer(self):
        return f"Abastecendo tanque de {self.tanque} Litros"
    
    def exibir_info(self):
        return f"Tanque: {self.tanque} Litros"

@dataclass
class CarroEletrico(Motor, Eletrico):
    def ligar(self):
        return f"{self.ligar_motor()} e {self.carregar()}"
    
    def exibir_info(self):
        return f"{Motor.exibir_info(self)}, {Eletrico.exibir_info(self)}"

@dataclass
class CarroHibrido(Motor, Eletrico, Combustao):
    def ligar(self):
        return f"{self.ligar_motor()}, {self.carregar()} e {self.abastecer()}"
    
    def exibir_info(self):
        return f"{Motor.exibir_info(self)}, {Eletrico.exibir_info(self)}, {Combustao.exibir_info(self)}"