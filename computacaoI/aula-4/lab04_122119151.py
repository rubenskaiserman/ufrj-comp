# Rubens Guedes Kaiserman
# 122119151

#Questão 1
def siga(info:tuple)->tuple:
    '''
        Recebe nome e as notas de um aluno e retorna o nome, a média, e o resultado do aluno
        Por alguma razão também retorna uma mensagem de parabéns se ele tiver acabado com uma média superior a 7
        tuple -> tuple
    '''
    nome = info[0]
    notas = info[1:]
    media = round(sum(notas)/len(notas), 1)
    if media >= 7:
        return (nome, media, 'aprovado', 'Parabéns!')
    elif media >= 5:
        return (nome, media, 'aprovado')
    else:
        return (nome, media, 'reprovado')

# Teste
# print(siga(('Rubens', 9, 5, 5)))

# Questão 2
def signo_chines(ano_nascimento:int)->str:
    '''
        Retorna o signo chinês aproximado com base no ano de nascimento de alguém
        A tupla abaixo foi montada com base na tabela de signos. Cada indice corresponde
        ao resto da divisão por 12 que determina o signo.
        int -> str
    '''
    signos = (
        'Macaco', 'Galo', 'Cão',
        'Porco', 'Rato', 'Boi', 
        'Tigre', 'Coelho', 'Dragão',
        'Serpente', 'Cavalo', 'Carneiro'
        )
    id_signo = ano_nascimento % 12
    return signos[id_signo]

# Teste
# print(signo_chines(0))
# print(signo_chines(1))
# print(signo_chines(2))
# print(signo_chines(3))
# print(signo_chines(4))
# print(signo_chines(5))
# print(signo_chines(6))
# print(signo_chines(7))
# print(signo_chines(8))
# print(signo_chines(9))
# print(signo_chines(10))
# print(signo_chines(11))
# print(signo_chines(12))

# Questão 3
def pegar_telefone(telefone:str)->tuple:
    '''
        Recebe uma string que, supostamente, corresponde a um telefone
        os dois primeiros digitos podem ou não ser DDD
        Essa função deve retornar uma tupla contendo DDD e Telefone nessa ordem
        Se não houver DDD deve retornar uma string vazia e telefone
        Se a string passada não for válida, deve retornar uma tupla contendo duas strings vazias
        str -> tuple
    '''
    comprimentos_possiveis = (8, 9, 10, 11)
    comprimento = len(telefone)
    if comprimento in comprimentos_possiveis:
        return ('', telefone) if comprimento < 10 else (telefone[:2], telefone[2:])
    else:
        return ('', '')

# Teste
# print(pegar_telefone('226156782'))

# Questao 4
def formato_data(data:str)->tuple:
    '''
        Essa função deve receber uma data e retornar os padrões aos quais ela pode corresponder
        dd/mm/yy - mm/dd/yy - yy/mm/dd São os padrões possíveis
        Se 0 < dd < 31 então pode ser dia
        Se 0 < mm < 12 Pode ser mês
        Assume-se que a string entregue conterá exatos 8 caracteres onde 2 são barras e o restante são números sem sinal
        str -> tuple
    '''
    validos = []
    componente = (int(data[:2]), int(data[3:5]), int(data[6:]))
    if 0 < componente[0] <= 31 and 0 < componente[1] <= 12:
        validos.append('dd/mm/yy')
    if 0 < componente[0] <= 12 and 0 < componente[1] <= 31:
        validos.append('mm/dd/yy')
    if 0 < componente[1] <= 12 and 0 < componente[2] <= 31:
        validos.append('yy/mm/dd')
    return tuple(validos)

# Teste
# print(formato_data('98/25/07'))
# print(formato_data('01/01/00'))
# print(formato_data('00/10/01'))
# print(formato_data('01/01/01'))