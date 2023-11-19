import pickle

class Produto:
    def __init__(self, codigo, nome, preco, quantidade):
        self.codigo = codigo
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    @staticmethod
    def cadastrar_produto(codigo, nome, preco, quantidade):
        produtos = Produto.listar_produtos()
        for produto in produtos:
            if produto.codigo == codigo:
                print("Código de produto já existe. Use um código exclusivo.")
                return

        novo_produto = Produto(codigo, nome, preco, quantidade)
        produtos.append(novo_produto)
        Produto.salvar_produtos(produtos)
        print(f"Produto {nome} cadastrado com sucesso.")

    @staticmethod
    def consultar_produto(codigo_ou_nome):
        produtos = Produto.listar_produtos()
        for produto in produtos:
            if produto.codigo == codigo_ou_nome or produto.nome == codigo_ou_nome:
                return produto
        return None

    @staticmethod
    def listar_produtos():
        try:
            with open('produtos.pickle', 'rb') as file:
                produtos = pickle.load(file)
        except (FileNotFoundError, EOFError):
            produtos = []
        return produtos

    @staticmethod
    def alterar_produto(codigo, novo_nome, novo_preco, nova_quantidade):
        produtos = Produto.listar_produtos()
        for produto in produtos:
            if produto.codigo == codigo:
                produto.nome = novo_nome
                produto.preco = novo_preco
                produto.quantidade = nova_quantidade
        Produto.salvar_produtos(produtos)
        print(f"Produto com código {codigo} alterado com sucesso.")

    @staticmethod
    def salvar_produtos(produtos):
        with open('produtos.pickle', 'wb') as file:
            pickle.dump(produtos, file)

# Interface de interação com o usuário
def menu_principal():
    while True:
        print("===== Sistema de Controle de Produtos =====")
        print("1. Cadastrar Produto")
        print("2. Consultar Produto")
        print("3. Listar Produtos")
        print("4. Alterar Produto")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")
        if opcao == '1':
            codigo = int(input("Código do produto: "))
            nome = input("Nome do produto: ")
            preco = float(input("Preço do produto: "))
            quantidade = int(input("Quantidade em estoque: "))
            Produto.cadastrar_produto(codigo, nome, preco, quantidade)
        elif opcao == '2':
            codigo_ou_nome = input("Digite o código ou nome do produto: ")
            produto = Produto.consultar_produto(codigo_ou_nome)
            if produto:
                print(f"Código: {produto.codigo}, Nome: {produto.nome}, Preço: R$ {produto.preco}, Quantidade: {produto.quantidade}")
            else:
                print("Produto não encontrado.")
        elif opcao == '3':
            produtos = Produto.listar_produtos()
            if not produtos:
                print("Nenhum produto cadastrado.")
            else:
                print("Lista de Produtos:")
                for produto in produtos:
                    print(f"Código: {produto.codigo}, Nome: {produto.nome}, Preço: R$ {produto.preco}, Quantidade: {produto.quantidade}")
        elif opcao == '4':
            codigo = int(input("Digite o código do produto que deseja alterar: "))
            produto = Produto.consultar_produto(codigo)
            if produto is None:
                print("Produto não encontrado.")
            else:
                novo_nome = input("Novo nome do produto: ")
                novo_preco = float(input("Novo preço do produto: "))
                nova_quantidade = int(input("Nova quantidade em estoque: "))
                Produto.alterar_produto(codigo, novo_nome, novo_preco, nova_quantidade)
        elif opcao == '5':
            print("Encerrando o programa.")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    menu_principal()
