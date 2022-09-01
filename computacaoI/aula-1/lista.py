def area_retangulo(comp:float, alt:float)->float:
    ''' Função que retorna a área de um, retângulo.
        Recebe dois parâmetros: Comprimento e altura. Ambos float pois podem não ser inteiros.
        Retorna um float que é a área do retângulo. '''
    return comp * alt

def area_superficie_cubo(c:float)->float:
    ''' Função que recebe um parâmetro C, que representa a aresta do cubo
        Retorna a área da superficie de um cubo (6 * c^2)'''
    return 6 * c**2

def area_coroa_circular(r1:float, r2:float)->float:
    ''' Função que retirna a área de uma coroa circular
        Recebe o raio de ambos os circulos como parâmetros
        A área da coroa é dada pela diferença entre a área de ambos os circulos
        Na questão é dado que o r1 > r2 e pi = 3,14'''
    pi = 3.14
    area_circulo_maior = pi * r1**2
    area_circulo_menor = pi * r2**2
    
    return area_circulo_maior - area_circulo_menor

def media(x:float, y:float)->float:
    ''' Média é uma função que recebe dois valores e retorna a média entre eles'''
    return (x + y)/2

def funcao_segundo_grau(a:float, b:float, c:float, x:float)->float:
    ''' Equações do segundo grau são definidas por 4 variáveis: a, b, c e x
        Funções do segundo grau seguem o seguinte formato f(x)=ax^2 + bx + c
        A função recebe os quatro parâmetros de uma função do segundo grau
        A função retorna o resultado da conta'''
    return a * x ** 2 + b * x + c

def media_ponderada(valor1:float, valor2:float, peso1:float, peso2:float)->float:
    ''' A função media_ponderada() recebe quatro parâmetros valor1, valor2, peso1 e peso2.
        Ela retorna (valor1 * peso1 + valor2 * peso2)/(peso1 + peso2)'''
    return (valor1 * peso1 + valor2 * peso2)/(peso1 + peso2)

def erro_pg(q:float, n)->float:
    ''' 
        A soma de uma progressão geométrica infinita é representada por 1/(1-q).
        A soma dos n primeiros termos de uma progressão geométrica é representada por a_1*(q^n - 1)/(q - 1).
        Dada a razão da progressão e a quantidade de termos da progressão dentro da estimativa é possível calcular o erro.
        O erro será a diferença entre a soma real e a estimativa.
        A estimativa segue a equação dos n primeiros termos.
        O valor real segue a equação da soma de uma pg infinita.
        Na questão é dito que o primeiro termo da progressão é 1.
    '''
    soma_pg = 1/(1 - q)
    a_1 = 1
    aproximacao = a_1*(q**n - 1)/(q - 1)
    erro = soma_pg - aproximacao
    return erro

def calculo_gorjeta(conta:float)->float:
    '''
        A gorjeta do garçom é 15% do valor da conta.
        15% de x é x*0.15
        Logo o valor da gorjeta é 0.15 * conta
        Função recebe valor da conta
        Função retorna valor da gorjeta
    '''
    return conta*0.15

def calculo_gorjeta_o_retorno(conta:float, porcentagem:float)->float:
    '''
        Função recebe valor da conta
        Função recebe porcentagem de gorjeta que deve ser dada. 
        Porcentagem deve ser passada como 10 para 10% e não 0.1
        Função retorna valor da gorjeta
    '''
    return conta*porcentagem/100

def calculo_juros(saldo_inicial:float, qtd_meses:int, juros_mensais:float)->float:
    '''
        Função recebe trẽs parâmetros: Saldo inicial, quantidade de meses passados e juros por mês
        Saldo Final = Saldo Inicial(1 + Quantidade de Meses * Juros por mês)
        Retorna saldo final
        Lembrando que porcentagem deve ser passada no formato 10 como 10% e não 0.1
    '''
    return saldo_inicial * (1 + qtd_meses*juros_mensais/100)

def arrasto_barco(vel_correntesa:float, vel_barco:float, larg_rio:float)->float:
    '''
        Assume-se que não há interferência externa no movimento do barco em direção ao outro lado do rio.
        Considera-se que a velocidade tanto do barco quanto da correntesa é uniforme.
        Assume-se que as dimensões do barco são despreziveis com relação ao rio.
        Assume-se que não há resistência do barco com relação a correntesa, ou seja, ele se move junto com a correntesa lateralmente.
        Ou seja, o barco irá cruzar o rio em um tempo previsível.
        O barco será arrastado pela correntesa durante a exata mesma quantidade de tempo a qual ele leva para cruzar o rio.
        Assume-se que a largura do rio é entregue em metros.
        Assume-se que tanto a velocidade do barco quanto da correntesa é passada em m/s
        Portanto a quantidade de tempo para cruzar o rio é igual a largura do rio dividida pela velocidade do barco.
        Sabe-se a distância pela qual o barco foi arrastado é igual a velocidade da correntesa multiplicada pelo tempo de cruzamento.
    '''
    tempo_cruzamento = larg_rio / vel_barco
    distancia_arrasto = tempo_cruzamento * vel_correntesa
    return distancia_arrasto