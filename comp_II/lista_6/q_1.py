# Você foi designado para criar um programa Python que realize a fusão de informações de dois arquivos, contatos.txt (o mesmo arquivo da questão 1) e sangue.txt, e gere um terceiro arquivo chamado contatosSanguineos.txt. O arquivo contatos.txt contém informações de contatos, incluindo nome, telefone e e-mail, separados por vírgulas. O arquivo sangue.txt contém informações de tipo sanguíneo, incluindo nome e tipo sanguíneo, separados por ponto e vírgula. O objetivo é criar um arquivo que contenha as informações de nome, telefone, e-mail e tipo sanguíneo, com os nomes combinados a partir dos dois arquivos.


# Os arquivos estão organizados como colunas. Basta juntar as colunas
# A chave primária/chave estrangeira é a coluna nome
# Esse código está bem pouco otimizado mas está bem legível
# Dado que é só um exemplo, otimização não é um problema
# Dito isso, se fosse pra lidar com grandes massas de dados, não era para ter tantos passos
def merge_files():
    contatos_sanguineos = dict()
    
    try:
        with open('./data/contatos.txt', 'r') as f1, open('./data/sangue.txt', 'r') as f2:
            contatos_array = f1.readlines()
            contatos = dict()
            for contato in contatos_array:
                contatos[contato.split(',')[0]] = contato.rsplit(',')[1:]
                
            sangue_array = f2.readlines()
            sangue = dict()
            for s in sangue_array:
                sangue[s.split(';')[0]] = s.split(';')[1:]
            
            for contato in contatos.keys():
                contatos_sanguineos[contato] = [info.rstrip() for info in contatos[contato]]
                contatos_sanguineos[contato].append(sangue[contato][0].rstrip() if contato in sangue.keys() else 'Tipo sanguíneo ausente')
    except FileNotFoundError:
        print('Arquivo(s) não encontrado(s)')
                     
    with open('./data/contatosSanguineos.txt', 'w') as f:
        for contato in contatos_sanguineos.keys():
            f.write(f"{contato},{','.join(contatos_sanguineos[contato])}\n")
            
            
merge_files()