from dataclasses import dataclass
@dataclass
class Animal:
    grupo: str

@dataclass
class Cachorro(Animal):
    grupo = "mamífero"
