class AluguelException(Exception):
    def __init__(self, mensagem):
        super().__init__(mensagem)

class Veiculo:
    def __init__(self, placa, modelo):
        self.placa = placa
        self.modelo = modelo
        self.disponivel = True
    
    def __str__(self):
        return f"Veiculo: {self.modelo} - Placa: {self.placa} - Disponível: {self.disponivel}"
    
    def alugar(self):
        if not self.disponivel:
            raise AluguelException("Veículo não disponível para aluguel!")
        
        self.disponivel = False
        
    def devolver(self):
        if self.disponivel:
            raise AluguelException("Veículo já está disponível!")
        
        self.disponivel = True
        

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.veiculos_alugados = []
       
    def __str__(self):
        return f"Cliente: {self.nome} - Veículos alugados: {self.veiculos_alugados}"
    
    def alugar_veiculo(self, veiculo):
        if len(self.veiculos_alugados) >= 2:
            raise AluguelException("Cliente não pode alugar mais veículos!")
        
        if not veiculo.disponivel:
            raise AluguelException("Veículo não disponível para aluguel!")
        
        veiculo.alugar()
        self.veiculos_alugados.append(veiculo)
        
    def devolver_veiculo(self, veiculo):
        if veiculo not in self.veiculos_alugados:
            raise AluguelException("Cliente não alugou este veículo!")
        
        veiculo.devolver()
        self.veiculos_alugados.remove(veiculo)
    
    
class Garagem:
    def __init__(self, veiculos=[]):
        self.veiculos = veiculos
        
    def __str__(self):
        return f"Garagem: {len(self.veiculos)} veículos disponíveis."
    
    def adicionar_veiculo(self, veiculo):
        self.veiculos.append(veiculo)
    
    def listar_veiculos(self):
        for veiculo in self.veiculos:
            print(veiculo)
            

if __name__ == "__main__":
    garagem = Garagem()
    garagem.adicionar_veiculo(Veiculo("ABC-1234", "Fusca"))
    garagem.adicionar_veiculo(Veiculo("DEF-5678", "Fiat Uno"))
    garagem.adicionar_veiculo(Veiculo("GHI-9101", "Fiat Palio"))
    garagem.adicionar_veiculo(Veiculo("JKL-1213", "Fiat Toro"))
    garagem.adicionar_veiculo(Veiculo("MNO-1415", "Fiat Argo"))
    garagem.adicionar_veiculo(Veiculo("PQR-1617", "Fiat Mobi"))
    garagem.adicionar_veiculo(Veiculo("STU-1819", "Fiat Punto"))
    
    cliente = Cliente("João")
    
    while True:
        print("1 - Alugar veículo")
        print("2 - Devolver veículo")
        print("3 - Listar veículos disponíveis")
        print("4 - Sair")
        
        try:
            op = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Opção inválida.")
            continue
        
        if op == 1:
            try:
                placa = input("Digite a placa do veículo: ")
                veiculo = None
                for v in garagem.veiculos:
                    if v.placa == placa:
                        veiculo = v
                        break
                
                if veiculo == None:
                    print("Veículo não encontrado.")
                    continue
                
                cliente.alugar_veiculo(veiculo)
            except AluguelException as e:
                print(e)
        elif op == 2:
            try:
                placa = input("Digite a placa do veículo: ")
                veiculo = None
                for v in garagem.veiculos:
                    if v.placa == placa:
                        veiculo = v
                        break
                
                if veiculo == None:
                    print("Veículo não encontrado.")
                    continue
                
                cliente.devolver_veiculo(veiculo)
            except AluguelException as e:
                print(e)
        elif op == 3:
            garagem.listar_veiculos()
        elif op == 4:
            break
            
        