

def traduzP(word: str) -> str:
    vogais = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'ã', 'õ', 'â', 'ê', 'î', 'ô', 'û', 'à', 'è', 'ì', 'ò', 'ù']
    
    translated_word = ''
    for letter in word:
        translated_word += letter
        if letter in vogais:
            translated_word += 'p' + letter
        
    return translated_word
    
print(traduzP('caderno'))