# Você foi encarregado de criar um programa em Python para combinar dados de dois arquivos, arquivo1.txt e arquivo2.txt. Cada arquivo contém uma lista de números separados por vírgulas. Seu objetivo é ler o conteúdo desses arquivos, combinar os números das duas listas em uma única lista, classificá-los em ordem crescente e criar um terceiro arquivo cujo nome é a concatenação dos nomes dos arquivos originais, como "arquivo1arquivo2.txt".

try:
    f1 = open('./data/arquivo1.txt', 'r')
    f2 = open('./data/arquivo2.txt', 'r')
    
    numbers = f1.read().replace(' ', '').split(',')
    numbers += f2.read().replace(' ', '').split(',')
    
    number_file_data = []
    lixo = []
    for number in numbers:
        if '.' in number:
            try:
                number_file_data.append(float(number))
            except ValueError:
                lixo.append(number)
        else:
            try:
                number_file_data.append(int(number))
            except ValueError:
                lixo.append(number)
        
    number_file_data.sort()
    
    with open('./data/arquivo1arquivo2.txt', 'w') as f:
        f.write(','.join([str(number) for number in number_file_data]))
    
    with open('./data/lixo.txt', 'w') as f:
        f.write(','.join(lixo))
    
    print('Números válidos: ', number_file_data)
    print('Arquivo criado com sucesso')
    
    f1.close()
    f1.close()
except FileNotFoundError:
    print('Arquivo(s) não encontrado(s)')