# Rubens Guedes Kaiserman
# 122119151
from sys import path
path.append('/home/kaiserman/dev/ufrj/computacaoI/aula-2') # Diretório onde está o arquivo da segunda lista
from lista import questao_2a # Importa função que calcula o delta dados a, b e c

# Questão 1
def modulo(value:float)->float:
    # Retorna o valor absoluto de um value
    return (value.real**2 + value.imag**2)**(1/2)

# Questão 2
def quantas_raizes(a, b, c):
    # Recebe os coeficientes de uma função do segundo grau
    # Retorna quantas raízes essa função apresenta
    if questao_2a(a, b, c) == 0:
        return 1
    elif questao_2a(a, b, c) > 0: 
        return 2
    else:
        return 0

# questao3
def string_repetida(n:int, string):
    # Retorna uma string repetida n vezes
    return string * int(n)
# Nota: Tendo em vista que o senhor não citou estruturas de repetição, nem recursividade, mas citou multiplicação de strings,
# suponho que o que o senhor deseja seja a string repetida da maneira apresentada acima.

# Questão 4
def formata_data(dia, mes, ano):
    # recebe 3 ints dia, mes e ano, respectivamente. Retorna uma string com a formatação de data coerente com os valores recebidos
    return str(dia) + '/' + str(mes) + '/' + str(ano) # Faria com fstring mas suponho que não seja a resposta desejada

# Questão 5
def funcao_inflexada(x):
    # Recebe o valor x da f(x)
    # Retorna o valor de f(x)
    # x = 0 --> f(x) = 0
    # 0 <= x < 2 --> f(x) = x
    # 2 <= x <= 3.5 --> f(x) = 2
    # 3.5 < x < 5 --> f(x) = 3
    # x >= 5 --> f(x) = x^2 - 10x + 28   
    if x < 0: 
        return 0
    elif x < 2: 
        return x
    elif x <= 3.5:
        return 2
    elif x < 5: 
        return 3
    else:
        return x**2 - 10*x + 28

# Casos de teste necessários: 
# x < 0
# 0 <= x < 2
# 2 <= x <=3.5
# 3.5 < x < 5
# x >= 5
# Lembrando que a mudança de regras são irrelevantes em pontos de inflexão com exceção do ponto 3.5
# Ou seja: As duas regras que poderiam estar afetando cada pontos geram o mesmo resultado nos pontos 0, 2 e 5.

# São necessários 5 testes
# funcao_inflexada(-1)
# funcao_inflexada(1)
# funcao_inflexada(2.3)
# funcao_inflexada(4)
# funcao_inflexada(7)

# Questão 6

# a)
def desconto_inss(salario_bruto):
    # Recebe o valor o salario bruto do usuário
    # Retorna o desconto do inss
    # Os valores estão de acordo com a tabela do inss
    if salario_bruto <= 2000:
        return salario_bruto*0.06
    elif salario_bruto <= 3000:
        return salario_bruto*0.08
    else:
        return salario_bruto*0.1

# b)
def desconto_ir(salario_bruto):
    # Recebe o salario bruto do usuário
    # Retorna o desconto o imposto de renda
    # Os valores estão de acordo com a tabela do IR
    if salario_bruto <= 2500:
        return salario_bruto*0.11
    elif salario_bruto <= 5000:
        return salario_bruto*0.15
    else:
        return salario_bruto*0.22

# c)
def salario_liquido(salario_bruto):
    # Recebe o salario bruto
    # Retorna o salario liquido de acordo com as reduções derivadas do INSS e do IR
    return salario_bruto - (desconto_inss(salario_bruto) + desconto_ir(salario_bruto))
