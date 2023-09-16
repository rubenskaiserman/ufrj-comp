# Você foi contratado para modelar uma televisão em Python. A televisão possui as seguintes características e funcionalidades:

# Características:

# Polegadas (inteiro)
# Marca (string)
# Preço (float)
# Estado (inicialmente desligada)
# Canal (sempre começa em 1 quando a TV é ligada)
# Volume (inicia em 1 da primeira vez e depois mantém o último valor definido pelo usuário, mesmo que a TV seja ligada ou desligada)
# Funcionalidades:

# Ligar e desligar a TV
# Verificar se está ligada ou desligada
# Mudar de canal (entre 1 e 4999)
# Mudar o volume (entre 1 e 99). Se o volume for superior a 80, deve alertar o usuário sobre o som alto.
# Mostrar todos os dados simultaneamente (canal, volume e marca). Se o volume estiver entre 81 e 99, indicar que o volume está alto.
# Crie a classe Televisao para representar essas características e funcionalidades.

from typing import Any


class Televisao():
    def __init__(self, polegada: int, marca: str, preco: float, estado:bool=False, canal:int=1, volume:int=1 ):
        self.polegada = polegada 
        self.marca = marca
        self.preco = preco
        self.estado = estado
        self.canal = canal
        self.volume = volume
    
    def ligar(self) -> None:
        # Estado devia ser chamada "isActive", "isUp", "ligada" ou algo assim
        self.estado = not self.estado # Essa boolean expression ficou bem feia em python
        
    def isLigada(self):
        # Namoral?
        return self.estado
    
    def mudarCanal(self, canal: int):
        if not (1 <= canal <= 4999):
            return "Canal inválido"
        self.canal = canal
        
    def mudarVolume(self, novoVolume: int):
        if not (1 <= novoVolume <= 99):
            return "Volume inválido"
        
        self.volume = novoVolume
        
    def get_attributes(self):
        return {
            "canal": self.canal,
            "volume": self.volume,
            "marca": self.marca,
            "Volume Alto": self.volume >= 81 
        }
        