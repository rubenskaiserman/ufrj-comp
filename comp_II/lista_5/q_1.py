def get_number(msg="Número: "):
    try:
        n = float(input(msg))
    except ValueError:
        print("Valor inserido inválido.", end="\n\n")
        n = get_number()
    return n

def division(num, den):
    try:
        return num / den
    except ZeroDivisionError:
        print("Não é possível dividir por zero.", end="\n\n")
        return division(num, get_number("Novo denominador: "))

def calculator():
    print("Calculadora: ...")
    num = get_number("Numerador: ")
    den = get_number("Denominador: ")
    div = division(num, den)
    
    print(f"Resultado: {div}", end="\n\n")
    
    
if __name__ == "__main__":
    calculator()
    