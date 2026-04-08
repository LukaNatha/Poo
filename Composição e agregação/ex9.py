from dataclasses import dataclass

@dataclass
class ItemPedido:
    produto: str
    quantidade: int
    preco: float

class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, produto, quantidade, preco):
        item = ItemPedido(produto, quantidade, preco)
        self.itens.append(item)

    def calcular_total(self):
        total = 0
        for i in self.itens:
            total += i.quantidade * i.preco
        return total

p = Pedido()
p.adicionar_item("Mouse", 2, 50)
p.adicionar_item("Teclado", 1, 100)

print(p.calcular_total())