# Rubens Guedes Kaiserman
# Feito sem consultar o gabarito
# 122119151

class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        
    def partir(self):
        print("Modelo: ", self.modelo)
        print("Marca: ", self.marca)
        print("VrumVrum... Zoooom")
        
class Eletrico(Veiculo):
    def __init__(self, marca, modelo, ano, autonomia, recharge_time):
        Veiculo.__init__(self, marca, modelo, ano)
        self.autonomia = autonomia
        self.recharge_time = recharge_time
        
    def alterar_autonomia(self, novaAutonomia):
        print("Autonomia antiga: ", self.autonomia)
        print("Autonomia nova: ", novaAutonomia)
        self.autonomia = novaAutonomia
        
class Motorizado(Veiculo):
    def __init__(self, marca, modelo, ano, potencia, combustivel):
        Veiculo.__init__(self, marca, modelo, ano)
        self.potencia = potencia
        self.combustivel = combustivel
        
    def alterar_combustivel(self, novo_combustivel):
        print("Combustivel antigo: ", self.combustivel)
        print("Combustivel novo: ", novo_combustivel)
        self.combustivel = novo_combustivel
        
class Hibrido(Eletrico, Motorizado):
    def __init__(self, marca, modelo, ano, potencia, combustivel, autonomia, recharge_time, tanque_combustivel, consumo):
        Eletrico.__init__(self, marca, modelo, ano, autonomia, recharge_time)
        Motorizado.__init__(self, marca, modelo, ano, potencia, combustivel)
        self.tanque_combustivel = tanque_combustivel
        self.consumo = consumo

    
carro_motorizado = Motorizado("Chevrolet", "Onix LT", 2022, "100cv","Gasolina")
carro_motorizado.alterar_combustivel("Etanol")
carro_motorizado.partir()
carro_eletrico = Eletrico("Tesla", "Model 3", 20620, 500, 30)
carro_eletrico.alterar_autonomia(600)
carro_eletrico.partir()
carro_hibrido = Hibrido("Toyota", "Prius", 2019, "100hp", "Gasolina", 200, 25, 40, 15)
carro_hibrido.partir()
carro_hibrido.alterar_combustivel("Etanol")
carro_hibrido.alterar_autonomia(220)