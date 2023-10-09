from abc import ABC, abstractmethod
from typing import Type

class ItemDescricao(ABC):
    @abstractmethod
    def descricao(self):
        pass

    def emprestar(self):
        print(self.descricao(), end=" ")
        print("Foi emprestado.")

    def devolver(self):
        print(self.descricao(), end=" ")
        print("Foi devolvido.") 
        
class Livro(ItemDescricao):
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def descricao(self):
        return f"Livro: {self.titulo} - Autor: {self.autor}"
    
class CD(ItemDescricao):
    def __init__(self, titulo, artista):
        self.titulo = titulo
        self.artista = artista

    def descricao(self):
        return f"CD: {self.titulo} - Artista: {self.artista}"
    
class DVD(ItemDescricao):
    def __init__(self, titulo, diretor):
        self.titulo = titulo
        self.diretor = diretor

    def descricao(self):
        return f"DVD: {self.titulo} - Diretor: {self.diretor}"
    
class Bibliotecario:
    def __init__(self, nome):
        self.nome = nome

    def mostrar_descricao(self, item: Type[ItemDescricao]):
        print(item.descricao())

    def emprestar_item(self, item):
        print(f"{self.nome} está emprestando o item.")
        item.emprestar()
        
class Usuario:
    def __init__(self, nome):
        self.nome = nome

    def devolver_item(self, item):
        print(f"{self.nome} está devolvendo o item.")
        item.devolver()
        
        
livro = Livro("A Arte da Guerra", "Sun Tzu")
cd = CD("Thriller", "Michael Jackson")
dvd = DVD("O Poderoso Chefão", "Francis Ford Coppola")
bibliotecario = Bibliotecario("Martins")
usuario = Usuario("Pedro")
bibliotecario.mostrar_descricao(livro)
bibliotecario.mostrar_descricao(cd)
bibliotecario.mostrar_descricao(dvd)
bibliotecario.emprestar_item(livro)
usuario.devolver_item(livro)
