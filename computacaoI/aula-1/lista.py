# Função que retorna a área de um, retângulo.
# Recebe dois parâmetros: Comprimento e altura. Ambos float pois podem não ser inteiros.
# Retorna um float que é a área do retângulo.
def area_retangulo(comp:float, alt:float)->float:
    return comp * alt


# Função que recebe um parâmetro C, que representa a aresta do cubo
# Retorna a área da superficie de um cubo (6 * c^2)
def area_superficie_cubo(c:float)->float:
    return 6 * c**2


# Função que retirna a área de uma coroa circular
# Recebe o raio de ambos os circulos como parâmetros
# A área da coroa é dada pela diferença entre a área de ambos os circulos
# Na questão é dado que o r1 > r2 e pi = 3,14
def area_coroa_circular(r1:float, r2:float)->float:
    pi = 3.14
    area_circulo_maior = pi * r1**2
    area_circulo_menor = pi * r2**2
    
    return area_circulo_maior - area_circulo_menor

# Média é uma função que recebe dois valores e retorna a média entre eles
def media(x:float, y:float)->float:
    return (x + y)/2

# Equações do segundo grau são definidas por 4 variáveis: a, b, c e x
# Funções do segundo grau seguem o seguinte formato f(x)=ax^2 + bx + c
# A função recebe os quatro parâmetros de uma função do segundo grau
# A função retorna o resultado da conta
def funcao_segundo_grau(a:float, b:float, c:float, x:float)->float:
    return a * x ** 2 + b * x + c

# A função media_ponderada() recebe quatro parâmetros valor1, valor2, peso1 e peso2.
# Ela retorna (valor1 * peso1 + valor2 * peso2)/(peso1 + peso2)
def media_ponderada(valor1:float, valor2:float, peso1:float, peso2:float)->float:
    return (valor1 * peso1 + valor2 * peso2)/(peso1 + peso2)


if __name__ == '__main__':
    # res = area_retangulo(5, 7)
    # res = area_retangulo(15, 2)
    # res = area_retangulo(500, 700)
    # res = area_retangulo(5, 0)

    # res = area_coroa_circular(2, 1)
    # res = area_coroa_circular(15, 5)
    # res = area_coroa_circular(100, 0)

    # res = media(-5, 7)
    # res = media(2, -2)
    # res = media(5, 5)
    # res = media(3, 4)
    res = media(3.0, 4.0)

    print(res)