from abc import ABC, abstractclassmethod
from typing import Type

class Produto(ABC):
    def __init__(self, codigo, nome, preco):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
    
    @abstractclassmethod
    def descricao(self):
        pass
    
    
class Eletronico(Produto):
    def __init__(self, codigo, nome, preco, voltagem):
        super().__init__(codigo, nome, preco)
        self.voltagem = voltagem
    
    def descricao(self):
        return f"Eletronico: {self.nome} - Voltagem: {self.voltagem}"
    
class Alimento(Produto):
    def __init__(self, codigo, nome, preco, validade):
        super().__init__(codigo, nome, preco)
        self.validade = validade
    
    def descricao(self):
        return f"Alimento: {self.nome} - Validade: {self.validade}"
    
class Estoque:
    def __init__(self):
        self.produtos = []
    
    def adicionar_produto(self, produto: Type[Produto]):
        self.produtos.append(produto)
    
    def listar_produtos(self):
        for produto in self.produtos:
            print(produto.descricao())
    
    def buscar_produto(self, codigo):
        print(f"Buscando produto pelo código: {codigo}")
        for produto in self.produtos:
            if produto.codigo == codigo:
                print(f"Produto encontrado: {produto.descricao()}")
                return
        print("Produto não encontrado.")

produto_eletronico = Eletronico("E123", "Televisão Samsung",
2999.90, "220V")
produto_alimento = Alimento("A456", "Barra de Chocolate", 5.99,
"25/12/2023")
estoque = Estoque()
estoque.adicionar_produto(produto_eletronico)
estoque.adicionar_produto(produto_alimento)
estoque.listar_produtos()
estoque.buscar_produto("E123")
estoque.buscar_produto("A789")