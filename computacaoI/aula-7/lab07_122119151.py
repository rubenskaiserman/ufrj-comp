from random import randint

#Questão 1
def jogar_dados():
    '''
        Simula o lançamento de dois dados
        Retorna quantos lançamentos são necessários para que os dois dados sejam iguais
        void -> int
    '''
    counter = 0
    while True:
        dado_A = randint(1, 6)
        dado_B = randint(1, 6)
        counter += 1
        if dado_A == dado_B:
            return counter

# Um pequeno exercicio adicional à questão 1
# OBS: Se quiser dar um pontinho extra aqui, não recusaria nop. As vezes eu dou uns moles nos forms.
def calculo_probabilidade(nivel_precisao:int)->float:
    '''
        Testa a probabilidade de dois dados cairem iguais.
        O nível de precisão é determinado pela quantidade de testes rodados.
        Quanto mais testes forem feitos mais próximo será o resultado
        int -> float
    '''
    acumulador = []
    for i in range(nivel_precisao):
        acumulador.append(jogar_dados())

    prob_media = sum(acumulador)/len(acumulador)
    return prob_media

# Questão 2

# A)
def buscar_contatos(contatos:list, nome:str)->list:
    '''
        Recebe uma lista de contatos list[list] e uma string nome
        retorna todos os contatos dos quais nome é uma substring do indice 0
        list, str -> list
    '''
    resultado_busca = []
    i, j = 0, 0
    length = len(contatos)
    while i < length:
        if nome.lower() in contatos[i][0].lower():
            resultado_busca.append([])
            resultado_busca[j] = contatos[i]
            j += 1
        i += 1
    return resultado_busca
# Admito que está um pouco forçado
# Provavelmente tem uma abordagem mais elegante do que adicionar um item à lista para substituir esse item apenas para não dar erro de indexação