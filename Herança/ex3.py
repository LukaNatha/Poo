from dataclasses import dataclass
@dataclass
class Animal:
    def fazer_som(self):
        return "Som do animal"
@dataclass
class Cachorro(Animal):
    def fazer_som(self):
        return "Latido"