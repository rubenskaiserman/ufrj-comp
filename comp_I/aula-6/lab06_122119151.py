# Rubens Guedes Kaiserman
# 122119151

# Questão 1
def del_phone(contato:list, phone:str)->bool:
    # Recebe os dados de um contato e um telefone a ser deletado
    # Se o telefone a ser deletado estiver nos números do contato ele será removido
    # Ao final será retornado um valor booleano representando se a função executou corretamente ou não.
    is_deleted = False
    if phone in contato[1]:
        contato[1].remove(phone)
        is_deleted = True

    return is_deleted

# Questão 2
def get_championship_data(championship_table:dict)->dict:
    # É passada uma tabela no formato dict contendo as informações de todos os times do campeonato
    # Esse dict possui uma key que corresponde ao time, e um value que corresponde à pontuação dele.
    # O código retorna o campeão e a média de pontuações em um formato de dict.
    champion = {'club': '', 'points': 0}
    for club, points in championship_table.items():
        if points > champion['points']:
            champion['club'], champion['points'] = club, points

    pontuacoes = championship_table.values()
    pontuacao_media = sum(pontuacoes) / len(pontuacoes)

    data = {
        'campeao': champion,
        'pontuacao_media': pontuacao_media
    }   
    return data

# Admito que não é meu melhor código.
# Sería mais coerente formatar isso de modo que fosse uma lista de dictionaries.
# + O código está bem feio. Preferia compartimentalizar ele em três partes mas você pediu uma função, logo, uma função.