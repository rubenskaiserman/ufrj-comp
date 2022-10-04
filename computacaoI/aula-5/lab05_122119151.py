# Rubens Guedes Kaiserman
# 122119151

# Questão 1
'''
contatinhosApp

    informações dos contatos registradas em listas
    nome é a unica informação obrigatória
    contato do usuário está em uma lista
    email e instagram também são salvos
    [nome, [telefone1, telefone2, telefone3...telefoneN], email, instagram]
'''

# a)
from distutils.log import info


def criar_contato(nome:str, telefone:str, email:str, instagram:str)->list:
    '''
    Recebe os dados do usuário e retorna um usuário no modelo definido
    str, str, str, str -> list
    '''
    return [nome, [telefone], email, instagram]

# b)
def modificar_contato(info:list, update_id:int, new_info:str)->list:
    '''
        Assume-se que será passado um update_id do tipo int
        Assume-se que será passado um valor coerente com o tipo de informação que se espera
        Atualiza dada lista de informações sobre um contato
        list, int, str->list
    '''
    if update_id == 1 and new_info not in info[1]:
        info[1].append(new_info)
        return True
    elif 0 <= update_id <= 3:
        info[update_id] = new_info
        return True
    else:
        return False
    # Não sei se é padrão colocar um else mesmo quando não é necessário.
    # Mas um dos lemas do Python é que explicito é melhor que implicito.
    # Logo, estou explicitando que se não for nenhum dos casos acima, aí sim não ocorreu alteração.
    # Em C eu suponho que seja padrão não utilizar o else quando se pode apenas retornar.
    # Se quiser me dar sua visão nesse pequeno detalhe o qual fiquei dissertando a respeito, gostaria de ouvir.

# Questão 2
def traduz_rna(cadeia:str)->str:
    '''
        str -> str # Acho que vou parar de colocar isso nos comentários, já coloco no código mesmo
        Recebe uma cadeia de aminoacidos em string
        Traduz isso para os nomes dos aminoacidos utilizando a tabela abaixo
    '''
    tabela_amino = {
        'UUU': 'Phe',
        'CUU': 'Leu',
        'UUA': 'Leu',
        'AAG': 'Lisina',
        'UCU': 'Ser',
        'UAU': 'Tyr',
        'CAA': 'Gln'
    }
    amino_blocos = [cadeia[0:3], cadeia[3:6], cadeia[6:]]
    aminoacidos = [tabela_amino[aminoacido] for aminoacido in amino_blocos]
    return '-'.join(aminoacidos)