# Considere a seguinte situação: você está desenvolvendo um sistema simples de gerenciamento de animais para um abrigo. Cada animal pode ser do tipo "Cachorro" ou "Gato". Cada animal tem um nome, idade, e a capacidade de fazer um som característico. Cachorro tem raça e gato tem cor

# CHEGA DE ANIMAL 

# Implemente um sistema em Python utilizando classes, herança, e persistência de dados com Pickle para atender a essa necessidade.

# Crie uma classe abstrata chamada Animal. Esta classe deve ter um método abstrato chamado fazer_som() e atributos comuns a todos os animais, como nome e idade.

# Implemente duas classes, Cachorro e Gato, que herdam da classe Animal. Cada uma dessas classes deve

# implementar o método fazer_som() de acordo com as características do animal. Desenvolva funções para cadastrar, listar, excluir e alterar animais. Essas funções devem interagir com o usuário para coletar informações necessárias e persistir os dados em um arquivo usando Pickle

# Crie um menu principal que permita ao usuário realizar as seguintes operações:
# - Cadastrar um novo animal (informando se é um cachorro ou gato).
# - Listar todos os animais cadastrados.
# - Excluir um animal pelo nome.
# - Alterar informações de um animal pelo nome.
# - Sair do programa.

import pickle
from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    @abstractmethod
    def fazer_som(self):
        pass
    
    def __str__(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Som: {self.fazer_som()}"
    
class Cachorro(Animal):
    
    def fazer_som(self):
        return "AUAUAU"

class Gato(Animal):
    
    def fazer_som(self):
        return "MIAU"
        

class Operador:
    animais = []
    
    @staticmethod
    def salvar_animais():
        with open('animais.pickle', 'wb') as file:
            pickle.dump(Operador.animais, file)
    
    @staticmethod
    def listar_animais():
        with open('animais.pickle', 'rb') as file:
            Operador.animais = pickle.load(file)
            
        for animal in Operador.animais:
            print(animal)
            
    @staticmethod
    def cadastrar_animal(nome, idade, tipo):
        if tipo == 'cachorro':
            animal = Cachorro(nome, idade)
        elif tipo == 'gato':
            animal = Gato(nome, idade)
        else:
            print('Tipo de animal inválido')
            return
        
        Operador.animais.append(animal)
        Operador.salvar_animais()
        
    @staticmethod
    def excluir_animal(nome):
        for animal in Operador.animais:
            if animal.nome == nome:
                Operador.animais.remove(animal)
                Operador.salvar_animais()
                return
        print('Animal não encontrado')
        
    @staticmethod
    def update_animal(nome):
        for animal in Operador.animais:
            if animal.nome == nome:
                animal.nome = input('Novo nome: ')
                animal.idade = input('Nova idade: ')
                Operador.salvar_animais()
                return
        print('Animal não encontrado')
        
if __name__ == "__main__":
    while True:
        print('1. Cadastrar animal')
        print('2. Listar animais')
        print('3. Excluir animal')
        print('4. Alterar animal')
        print('5. Sair')
        
        opcao = input('Escolha uma opção: ')
        
        if opcao == '1':
            nome = input('Nome: ')
            idade = input('Idade: ')
            tipo = input('Tipo: ')
            Operador.cadastrar_animal(nome, idade, tipo)
        elif opcao == '2':
            Operador.listar_animais()
        elif opcao == '3':
            nome = input('Nome: ')
            Operador.excluir_animal(nome)
        elif opcao == '4':
            nome = input('Nome: ')
            Operador.update_animal(nome)
        elif opcao == '5':
            print('Encerrando o programa')
            break
        else:
            print('Opção inválida')
    
    