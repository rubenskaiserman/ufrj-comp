def sucessor(num: float) -> float:
    return num + 1

def questao():
    num = float(input('Número: '))
    print(sucessor(num))

if __name__ == '__main__':
    questao()