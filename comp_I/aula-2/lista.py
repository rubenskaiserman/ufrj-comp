import math

def questao_1b(a, b, c):
    '''
        Recebe três números, os soma e retorna a divisão por três. Leia-se calcula a média de três numeros
    '''
    return (a + b + c)/3

def questao_1c(a, b, c):
    '''
        Recebe três parêmtros inteiros: a, b e c
        Retorna a diferença entre o maior valor entre os três e a média entre os três
        Isso é feito a partir da diferença entre a função max() que recebe a, b e c, e a função desenvolvida no exercício anterior
    '''
    return max(a, b, c) - questao_1b(a, b, c)

def questao_1d(a, b, c):
    '''
        Exatamente o mesmo processo que a questão anterior porém com soma ao invés de subtração e o uso da função min() ao invés da função max().
    '''
    return min(a, b, c) + questao_1b(a, b, c)

def questao_2a(a, b, c):
    '''
        Recebe três parâmetros, sendo eles os coeficientes de uma equação de segundo grau
        Retorna o valor de delta, ou seja, da descriminante
        delta = b^2 - 4ac
    '''
    return b**2 - 4*a*c

def questao_2b(a, b, c):
    '''
        Retorna a primeira raíz de uma equação de segundo grau
        x_1 = (-b + delta**(1/2))/(2*a)
    '''
    return (-b + questao_2a(a, b, c)**(1/2))/(2*a)

def questao_2c(a, b, c):
    '''
        Retorna a segunda raíz de uma equação de segundo grau
        x_2 = (-b + delta**(1/2))/(2*a)
    '''
    return (-b - questao_2a(a, b, c)**(1/2))/(2*a)

def questao_3b(a_1, a_n, r):
    '''
        O número de termos, ou seja, n, é igual a diferença entre a_n e a_1 dividida pela razão + 1
        + 1 é por conta de que essa divisão não considera a1.
    '''
    return ((a_n - a_1)/r) + 1

def questao_3c(a_1, a_n, r):
    '''
        A soma de uma PA é dada por S = ((a_1 + a_n)*n)/2
        O valor de n pode ser obtido a partir da função questao_3b().
        Logo, basta aplicar ao calculo.
    '''
    return ((a_1 + a_n)*questao_3b(a_1, a_n, r))/2

def questao_4a(x1, y1, x2, y2):
    '''
        A distância entre dois pontos dentro de um plano pode ser dada através do teorema de pitágoras.
        A diferença entre coordenadas em x, e a diferença entre as coordenadas em y são catetos.
        A distância é a hipotenusa.
        Geralmente sería necessário manipular os valores de modo que as distâncias fossem sempre positivas. Contudo, dado que
        ambos os valores serão elevados à um expoente par, conclui-se que os valores considerados serão, já, alterados deste modo.
    '''
    a = x1 - x2
    b = y1 - y2
    return math.sqrt(a**2 + b**2)

def questao_4b(a, b):
    '''
        O perímetro de uma figura plana é a soma de seus lados. 
        Ou seja, a + b + c é a área de um triangulo retangulo onde a e b são catetos e c é a hipotenusa.
        Logo, calculando a hipotenusa basta que se some ela aos catetos para se saber o perímetro.
    '''
    c = math.sqrt(a**2 + b**2)
    return a + b + c

def questao_4c(angulo):
    '''
        Bem direto ao ponto.
        Retornando a soma do quadrado do seno com o quadrado do cosseno do angulo passado por parâmetro
    '''
    return math.sin(angulo)**2 + math.cos(angulo)**2

def questao_5(r, ang=360):
    '''
        A área de um setor circular é o produto entre o angulo do setor e a área por grau do circulo.
        A área do circulo total é pi*r^2. A área por grau é a área total dividida por 360.
        Ou seja, a área total é a área por grau multiplicada por 360.
        Logo, se o angulo do setor for 360, o calculo retornará a área do circulo como um todo.
        OBS: Não está sendo realizado o tratamento de erros, logo se for passado um valor maior do que 360 como
        parâmetro, a função retornará um valor inválido matemáticamente. Até porque foi inserido um valor inválido.
    '''
    return ((math.pi * r**2)/360)*ang