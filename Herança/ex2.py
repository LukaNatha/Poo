from dataclasses import dataclass

@dataclass
class Animal:
    grupo: str = ""

@dataclass
class Cachorro(Animal):
    def __init__(self):
        super().__init__("mamífero")