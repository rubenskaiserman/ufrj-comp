# Aluno: Rubens Guedes Kaiserman
# DRE: 122119151

# Questão 1
def solicita_lancamentos()->list:
    '''Solicita uma série de inputs que correspondem a um lancamento de dados e retorna a lista composta pelos valores inseridos'''
    lancamento = None
    lancamentos = []
    while True:
        lancamento = input("Insira o valor do dado no lancamento atual. (Press enter sem valor para não inserir mais): ")
        if lancamento == "":
            return lancamentos
        lancamentos.append(int(lancamento))

def conta_series_repetidas()->int:
    '''Conta quantas séries de números repetidos existe em uma lista'''
    repetidos = set()
    lancamentos = solicita_lancamentos()
    length = len(lancamentos)
    item_anterior = lancamentos[0]
    for i in range(1, length):
        if lancamentos[i] == item_anterior:
            repetidos.add(lancamentos[i])
        item_anterior = lancamentos[i]
    print(len(repetidos))
    return len(repetidos)

# Questão 2
def area_trapezio(B, b, h)->float:
    '''Retorna área do trapézio'''
    return ((B + b)*h)/2

def mostrar_quadrados(numeros: list)->None:
    '''Imprime o número seguido de seu quadrado para cada número entregue na função'''
    for num in numeros:
        print(f"{num}: {num**2}")

def media_aritmetica(values: list)->float:
    '''Retorna a média aritmética dos valores da lista entregue'''
    return sum(values)/len(values)

def soma_quebrada(valores: tuple)->int:
    '''Imprime a soma de inteiros entre dois valores intervalados pelo terceiro valor'''
    return sum(range(valores[0], valores[1] + 1, valores[2]))

def resultado_opcional(i, a, b, c):
    '''Executa uma ação de acordo com o codigo i entregue (condições descritas na questão)'''
    if i == 1:
        print(area_trapezio(a, b, c))
    elif i == 2:
        mostrar_quadrados([a, b , c])
    elif i == 3:
        print(media_aritmetica([a, b, c]))
    elif i == 4:
        print(soma_quebrada((a, b, c)))

# Questão 3
def solicita_matriz()->list:
    '''Exercicío adicional para a questão 3
    Adicionar a solicitação da matriz'''
    matriz =[]
    while True:
        nome = input("Nome: ")
        if nome == "sair":
            break
        email = input("Código: ")
        if email == "sair":
            break
        setor = input("Setor: ")
        if setor == "sair":
            break
        numero = input("Numero: ")
        if numero == "sair":
            break
        matriz.append([nome, email, setor, numero])

def busca_por_setor(matriz:list, setor:str)->list:
    '''Retorna as linhas da matriz cujo indice 2 corresponde ao setor entregue na chamada da função'''
    resultado = []
    for linha in matriz:
        if matriz[2] == setor:
            resultado.append(linha)
    return linha
# O método de combinar essas duas da questão 3 sería, como parâmetro chamar a função solicita_matriz().
