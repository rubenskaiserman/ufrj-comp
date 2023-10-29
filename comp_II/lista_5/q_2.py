class Conta:
    def __init__(self, numero, titular, saldo=0):
        self.__saldo = saldo
        self.numero = numero
        self.titular = titular
        
    @property
    def saldo(self):
        return self.__saldo
            
    def depositar(self, valor):
        try:
            valor = float(valor)
        except ValueError:
            print("Valor inserido inválido inválido.")
            return
        
        if valor <= 0:
            print("Depósito deve ser maior que zero.")
            return
        
        print(f"Depósito de {valor:.2f} realizado com sucesso.")
        
        self.__saldo += valor
        
    def sacar(self, valor):
        try:
            valor = float(valor)
        except ValueError:
            print("Valor inserido inválido inválido.")
            return
        
        if valor > self.__saldo:
            print("Saldo insuficiente.")
            return

        print(f"Saque de {valor:.2f} realizado com sucesso.")
        
        self.__saldo -= valor
        

def main(conta: Conta)->tuple[Conta, bool]:
    print("1 - Ver saldo")
    print("2 - Depositar")
    print("3 - Sacar")
    print("4 - Sair")
    
    try:
        op = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Opção inválida.")
        return conta, False
    
    if op == 1:
        print(f"Saldo: {conta.saldo:.2f}")
        return conta, False
    elif op == 2:
        valor = input("Digite o valor a ser depositado: ")
        conta.depositar(valor)
        return conta, False
    elif op == 3:
        valor = input("Digite o valor a ser sacado: ")
        conta.sacar(valor)
        return conta, False
    elif op == 4:
        return conta, True
    
    
    
if __name__=="__main__":
    conta = Conta(123, "João", 1999.99)
    while True:
        conta, sair = main(conta)
        if sair:
            break
        
        