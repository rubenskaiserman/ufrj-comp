# Você foi contratado para desenvolver um sistema simples de gerenciamento para uma
# biblioteca. O objetivo principal é acompanhar quais livros estão disponíveis, quais estão
# emprestados e a capacidade de emprestar e retornar livros. Deve apresentar

# 1. Classe Livro:
# Cada livro tem os seguintes atributos:
# - `titulo`: Uma string representando o título do livro.
# - `autor`: Uma string representando o autor do livro.
# - `status`: Uma string que pode ser "disponível" ou "emprestado".
# A classe Livro deve ter os seguintes métodos:
# - `emprestar()`: Altera o status do livro para "emprestado".
# - `retornar()`: Altera o status do livro para "disponível".
# 2. Classe Biblioteca:
# A biblioteca tem o seguinte atributo:
# - `livros`: Uma lista contendo todos os livros disponíveis na biblioteca.
# A classe Biblioteca deve ter os seguintes métodos:
# - `adicionar_livro(livro)`: Adiciona um livro à lista de livros.
# - `listar_livros()`: Exibe todos os livros e seus respectivos status.
# - `emprestar_livro(titulo)`: Procura um livro pelo título e, se disponível, o empresta.
# - `retornar_livro(titulo)`: Procura um livro pelo título e o retorna, se estiver emprestado.
# Tarefa:
# Crie as classes `Livro` e `Biblioteca` e implemente seus métodos. Depois, crie uma interface
# simples para o usuário, onde ele pode adicionar livros à biblioteca, listar todos os livros,
# emprestar e retornar livros.
# Mesmo que não seja ideal, a resolução é simples e a biblioteca tem apenas um exemplar de
# cada título.

class Livro:
    def __init__(self, titulo, autor, status):
        self.titulo = titulo
        self.autor = autor
        self.status = status if status in ['disponível', 'emprestado'] else None
        # Sem maior descrição do sistema é impossível definir um comportamento padrão para 
        # situação onde Livro não foi definido como um dos valores possíveis
        # PS: Deveria ser um boolean
        
    def emprestar(self):
        self.status = "emprestado"
        
    def retornar(self):
        self.status = "disponível"
        
class Biblioteca:
    def __init__(self, livros: list[Livro]=[], ):
        self.livros = livros
        
    def adiciona_livro(self, livro: Livro):
        self.livros.append(livro)
        
    def listar_livros(self):
        return self.livros
    
    def emprestar_livro(self, titulo:str):
        for i in range(len(self.livros)):
            if self.livros[i].titulo == titulo and self.livros[i].status == 'disponível':
                self.livros[i].emprestar()
                break
            
    def retornar_livro(self, titulo: str):
        for i in range(len(self.livros)):
            if self.livros[i].titulo == titulo and self.livros[i].status == 'emprestado':
                self.livros[i].retornar()
                break
    # Não pediu para fazer nada se não achasse o título. Vou assumir que tá la mesmo
    

biblioteca = Biblioteca()
answer = 0

while answer != 5:
    print("\n"*10)
    print("1. Inserir Livro")
    print("2. Emprestar Livro")
    print("3. Devolver Lívro")
    print("4. Listar livros")
    print("5. Sair", end="\n\n\n")
    
    answer = int(input())
    
    if(answer == 1):
        titulo = input("Título: ")
        autor = input("Autor: ")
        status = input("Status: ")
        
        livro = Livro(titulo, autor, status)
        biblioteca.adiciona_livro(livro)
    elif(answer == 2):
        titulo = input('titulo: ')
      
        biblioteca.emprestar_livro(titulo)
    elif(answer == 3):
        titulo = input('titulo: ')
      
        biblioteca.retornar_livro(titulo)
    elif(answer == 4):
        for livro in biblioteca.livros:
            print(livro.__dict__)
        
    