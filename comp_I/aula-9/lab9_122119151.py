# Rubens Guedes Kaiserman
# 122119151

def numTimesMatrix(matrix:list[list], num:float)->list[list]:
    '''
        recebe um número e uma matriz e retorna o produto dos dois
    '''
    result = matrix.copy()
    for i in range(len(result)):
        result[i] = [result[i][j]*num for j in range(len(result[i]))]
    
    return result

def getMatches(users:dict)->list[tuple]:
    '''
        Recebe um dicionário composto por uma key que representa o usuário e uma list de quem ele curtiu.
        Retorna os matches.
    '''
    matches = []
    for key, value in users.items():
        for person in value:
            if key in users[person] and (person, key) not in matches:
                matches.append((key, person))
    return matches
 
def whoCalled(agenda:list[list], numero:str):
    '''
        Recebe uma lista de listas que corresponde a agenda de contatos
        Cada contato segue o modelo primeiramente introduzido no lab5
        Retorna o contato que ligou.
    '''
    for contato in agenda:
        if numero in contato[1]:
            return contato
    return []

