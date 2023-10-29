class TransacaoBancariaException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)
        

class ContaBancaria:
    def __init__(self, titular, saldo=0):
        if saldo < 0:
            raise TransacaoBancariaException("Saldo inicial não pode ser negativo.")
        
        self.__saldo = saldo
        self.titular = titular
        
    def __str__(self):
        return f"Conta de {self.titular} - Saldo {self.saldo:.2f}."
    
    @property
    def saldo(self):
        return self.__saldo
            
    def depositar(self, valor):
        try:
            valor = float(valor)
        except:
            raise TransacaoBancariaException("Valor inserido inválido.")
        
        if valor <= 0:
            raise TransacaoBancariaException("Não se pode transferir valores negativos nem zero!")
        
        print(f"Depósito de {valor:.2f} realizado com sucesso.")
        
        self.__saldo += valor
        
    def sacar(self, valor):
        try:
            valor = float(valor)
        except:
            raise TransacaoBancariaException("Valor inserido inválido.")
        
        if not (0 < valor < self.__saldo):
            raise TransacaoBancariaException("Saldo insuficiente ou valor negativo inserido.")

        print(f"Saque de {valor:.2f} realizado com sucesso.")
        
        self.__saldo -= valor
        

class ContaPoupanca(ContaBancaria):
    def __init__(self, titular:str, saldo:float, taxa_juros:float):
        super().__init__(titular, saldo)
        
        if taxa_juros < 0 or taxa_juros > 1:
            raise ValueError("Taxa de juros deve ser maior que zero e menor que 1.")
        self.taxa_juros = taxa_juros
    
    def __str__(self):
        return f"Conta Poupança de {self.titular} - Saldo: R$ {self.saldo} - Taxa de Juros: {self.taxa_juros}"
    
    def calcular_juros(self, meses):
        if not (1 <= meses):
            raise TransacaoBancariaException("Mês deve estar entre 1 e 12.")
        
        juros_acumulados = (((1 + self.taxa_juros) ** meses) * self.saldo) - self.saldo
        
        return juros_acumulados
        
if __name__ == "__main__":
    conta_poupanca = ContaPoupanca("Maria", 100, 0.01)
    
    while True: 
        print("1 - Ver saldo")
        print("2 - Depositar")
        print("3 - Sacar")
        print("4 - Calcular juros")
        print("5 - Sair")

        try:
            op = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida.")
            continue
        
        if op == 1:
            print(f"Saldo: {conta_poupanca.saldo:.2f}")
        elif op == 2:
            try: 
                valor = float(input("Digite o valor a ser depositado: "))
                try:
                    conta_poupanca.depositar(valor)
                except TransacaoBancariaException as e:
                    print(e)
            except ValueError:
                print("Valor inválido.")
            finally:
                    print("Transação realizada com sucesso.")
            
        elif op == 3:
            try: 
                valor = float(input("Digite o valor a ser sacado: "))
                try:
                    conta_poupanca.sacar(valor)
                except TransacaoBancariaException as e:
                    print(e)
            except ValueError:
                print("Valor inválido.")
            finally:
                print("Operação realizada com sucesso.")
        elif op == 4:
            try: 
                meses = int(input("Digite o número de meses: "))
                try:
                    juros = conta_poupanca.calcular_juros(meses)
                    print(f"Juros acumulados: {juros:.2f}")
                except TransacaoBancariaException as e:
                    print(e)
            except ValueError:
                print("Valor inválido.")
            finally:
                print("Transação realizada com sucesso.")
        elif op == 5:
            break