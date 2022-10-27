# Rubens Guedes Kaiserman
# 122119151

from math import pi

#Questão 1
def iterar(iteravel:list|tuple|str, elem:any)->int:
    '''
        Recebe um iteravel e um elemento.
        retorna a quantidade de vezes que esse elemento está presente no iterável.
    '''
    counter = 0
    for value in iteravel:
        if value == elem:
            counter += 1
    
    return counter

# Questão 2
def countar_no_trecho(iteravel:list|tuple|str, elem:any, ini:int, fim:int)->int:
    # Recebe um iteravel, um elemento e dois indices correspondendo o inicio e o final do trecho a ser analisado.
    # Returna a quantidade de incidencias do elemento no determinado trecho do iterável.
    # Assume-se que fim > ini
    if ini < fim and ini < len(iteravel):
        return iterar(iteravel[ini:fim + 1], elem)
    else:
        return 'Erro. Indice inválido para o iterável fornecido'

# Questão 3
def atualiza_mascara(masc:list, actual_word:str, letra_chutada:str)->str:
    # Recebe uma lista mascara, uma palavra e uma letra
    # A mascara corresponde à palavra.
    # A letra tenta adivinhar, a partir da mascara, um dos itens da palavra
    # A função retorna o resultado do chute, ou seja, a mascara atualizada
    word_length = len(actual_word)
    for i in range(word_length):
        if actual_word[i] == letra_chutada:
            masc[i] = letra_chutada
    return masc

# Questão 4
# a)
def somatorio_piano(n:int)->float:
    # Recebe um N
    # Calcula pi/4 com a precisão definida por n a partir da equação apresentada na questão
    # Retorna um quarto de pi
    pi_over_four = 0
    for i in range(n):
        pi_over_four += ((-1)**i)/(2*i + 1)
    return pi_over_four

# b)
def somatorio_piano_preciso()->tuple:
    # Retorna o valor de pi/4 com uma precisão de 0.01
    n = 0
    precisao = 0
    while abs(pi/4 - precisao) > 0.01:
        n += 1
        precisao = somatorio_piano(n)
    
    return (precisao, n)
# O método acima não é o mais eficiente por utilizar a função préviamente construída.
# Uma abordagem mais eficiente sería a apresentada abaixo

def som_piano():
    x = 0
    i = 0
    while abs(pi/4 - x) > 0.01:
        x += ((-1)**i)/((2*i)+1)
        i += 1

    return (x, i)
# Essa abordagem é mais rápida porque não precisa repetir a mesma operação repetidas vezes.
# Toda vez que a função somatorio_piano() é chamada, ela executa toda a iteração novamente.
# Ou seja, enquanto que a função que lhe apresento está em (O)n. A função anterior está em (O)n^2 


