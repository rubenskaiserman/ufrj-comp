from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.lower_bound = 3
        self.upper_bound = 8
    
    @abstractmethod
    def emitir_som(self):
        pass
    
    def dormir(self):
        return f"{self.nome} está dormindo"
    
    def fase_vida(self):
        if self.idade <= self.lower_bound:
            return f"{self.nome} tem {self.idade} anos e é jovem"
        elif self.idade <= self.upper_bound:
            return f"{self.nome} tem {self.idade} anos e é adulto"
        else:
            return f"{self.nome} tem {self.idade} anos e é idoso"
    
class Cachorro(Animal):
    def emitir_som(self):
        return "Au Au"
        
class Gato(Animal):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)
        self.lower_bound = 4
        self.upper_bound = 10
    
    def emitir_som(self):
        return "Miau"
        
cachorro1 = Cachorro("Rex", 2)
print(cachorro1.emitir_som()) # Saída: Au Au
print(cachorro1.dormir()) # Saída: Rex está dormindo
print(cachorro1.fase_vida()) # Saída: Rex tem 2 anos e é jovem
gato1 = Gato("Whiskers", 6)
print(gato1.emitir_som()) # Saída: Miau
print(gato1.dormir()) # Saída: Whiskers está dormindo
print(gato1.fase_vida()) # Saída: Whiskers tem 6 anos e é adulto
