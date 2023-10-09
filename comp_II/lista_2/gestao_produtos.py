class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco
        
    def exibir_detalhes(self):
        print('Nome: ' + self.nome)
        print('Preço: ' + str(self.preco))
        
class Eletronico(Produto):
    def __init__(self, nome, preco, garantia, marca):
        self.garantia = garantia
        self.marca = marca
        super().__init__(nome, preco)
        
    def mostrar_garantia(self):
        print('Garantia: ' + str(self.garantia))
        
class Smartphone(Eletronico):
    def __init__(self, nome, preco, garantia, marca, sistema_operacional, capacidade_armazenamento):
        self.sistema_operacional = sistema_operacional
        self.capacidade_armazenamento = capacidade_armazenamento
        super().__init__(nome, preco, garantia, marca)
        
    def exibir_especificacoes(self):
        self.exibir_detalhes()
        self.mostrar_garantia()
        print("Marca: " + self.marca)
        print('Sistema operacional: ' + self.sistema_operacional)
        print('Capacidade de armazenamento: ' + str(self.capacidade_armazenamento))
        
        
produto = Produto("Cadeira", 50)
produto.exibir_detalhes()
notebook = Eletronico("Notebook", 860, 2, "Dell")
notebook.exibir_detalhes()
notebook.mostrar_garantia()
celular = Smartphone("Pixel", 608, 2, "Google", "Android", 128)
celular.exibir_especificacoes()



