# Imagine um cenário futurista onde robôs são programados para batalhar entre si em um
# campeonato de máquinas.

# Requisitos:
# Classe Robô:
# Cada robô possui os seguintes atributos:
# nome: Uma string representando o nome do robô.
# pontos_de_vida (PV): Um valor inteiro que inicia com um máximo de 50. Se um robô tentar
# ser instanciado com mais de 50 PV, uma mensagem de erro deve ser exibida e o robô não
# deve ser criado.
# energia: Um valor inteiro que sempre começa em 100.
# status: Uma string que pode ser "operante" ou "inoperante". Um robô inicia como
# "operante", mas se seus PV caírem para 0 ou menos, seu status deve mudar para
# "inoperante".

# A classe Robô deve ter os seguintes métodos:
# atacar(outro_robo, classe_de_ataque): Permite que um robô ataque outro robô. O dano do
# ataque é aleatório e depende da classe de ataque escolhida.

# energizar(): Permite que um robô recupere energia. # Quanta?
# recuperar(): Permite que um robô recupere PV à custa de energia. # Quanto custa e quanto recupera por unidade?
# implodir(outro_robo): Um robô pode se auto-destruir para causar dano ao oponente. #Ok

# Ataque:
# Os robôs podem atacar em três classes diferentes, que determinam a quantidade de dano e
# energia consumida.
# Classe 1: Dano entre 1 e 8, consome 10 de energia.
# Classe 2: Dano entre 2 e 12, consome 20 de energia.
# Classe 3: Dano entre 4 e 24, consome 40 de energia.

# Energizar e Recuperar:
# energizar(): Recupera 20 de energia.
# recuperar(): Gasta 10 de energia para recuperar 10 de PV. Os PVs não podem exceder o
# valor inicial do robô.

# Implodir:
# Um robô pode decidir se autodestruir com o método implodir(), causando dano a si mesmo
# igual a todos os seus PVs e causando um dano aleatório entre 10 a 50 ao oponente.
# Implodir gasta 40 de energia.

# Não saquei qual é a vantagem de se implodir? É só pra ganhar com estilo? Ou pro caso de você ter quase certeza
# que perdeu daí essa é sua ultima tentativa de empatar?

# Tarefa:
# Com base nos requisitos fornecidos, crie a classe Robo e instancie dois robôs, escolha o
# nome de cada um. Em seguida, simule uma batalha entre eles usando os métodos
# fornecidos até que um dos robôs se torne "inoperante". Ao final, anuncie o vencedor da
# batalha.

from random import randint

class Robo:
    def __init__(self, nome:str, pontos_de_vida:int, ):
        self.nome = nome,
        self.pontos_de_vida = pontos_de_vida
        self.energia = 100
        self.status = 'operante' # Deveria ser boolean

    def atacar(self, alvo, classe_ataque):
        if self.energia < 40 and classe_ataque == 3:
            return False
        elif self.energia < 20 and classe_ataque == 2:
            return False
        elif self.energia < 10:
            return False
        
        if classe_ataque == 1:
            lower_bound = 1
            upper_bound = 8
            self.energia -= 10
        elif classe_ataque == 2:
            lower_bound = 2
            upper_bound = 12
            self.energia -=20
        elif classe_ataque == 3:
            lower_bound = 4
            upper_bound = 24
            self.energia -= 40
            
        dano = randint(lower_bound, upper_bound)
        alvo.pontos_de_vida -= dano
        
        return True

    def energizar(self):
        self.energia += 20
        return True
    
    def recuperar(self):
        if self.energia < 10: return False
        
        self.pontos_de_vida += 10 if (50 - self.pontos_de_vida < 50) else 50
        self.energia -= 10
        return True
    
    def implodir(self, alvo):
        if self.energia < 40:
            return False
        
        self.energia -= 40
        self.pontos_de_vida = 0
        
        alvo.pontos_de_vida -= randint(0, 40)
        return True

# Após cada método utilizado o sistema deve responder o máximo possível de informações
# sobre os robôs para acompanhamento (PV atual, energia atual...).

# Dica: Utilize o módulo random do Python para gerar valores aleatórios para os ataques e
# danos

# NOTA: Admiro o esforço pra elaborar esse enunciado enorme.
# NOTA2: Bastante trabalho pra fazer isso até. Deu até preguiça.

def print_status(robos):
    for robo in robos:
        print(f"Nome: {robo.nome}")
        print(f'Pontos de vida: {robo.pontos_de_vida}')
        print(f"Energia: {robo.energia}")
        print("\n"*2)

def battle(robo):
    print(f"Robô: {robo.nome}")
    print("1. Atacar ")
    print("2. Energizar ")
    print("3. Recuperar ")
    print("4. Implodir ", end='\n\n')
    
    answer = int(input(''))
    
    if answer == 1:
        classe_ataque = int(input("Classe Ataque: [1, 2 ou 3]"))
        success = robo.atacar(robos[i - 1], classe_ataque)
    elif answer == 2:
        success = robo.energizar()
    elif answer == 3:
        success = robo.recuperar()
    elif answer == 4:
        success = robo.implodir(robos[i - 1])
    
    return success

if __name__ == '__main__':
    robos = [Robo(nome='1', pontos_de_vida=50,), Robo(nome='2', pontos_de_vida=50,)]
    
    while True:
        print_status(robos)
        
        for i in range(len(robos)):
            while True:
                success = battle(robos[i])
                if success: break
            
        if(robos[0].pontos_de_vida <= 0 and robos[1].pontos_de_vida > 0):
            print_status(robos)
            print(f"Robô {robos[1].nome} Venceu")
            break
        elif(robos[0].pontos_de_vida > 0 and robos[1].pontos_de_vida <= 0):
            print_status(robos)
            print(f"Robô {robos[0].nome} Venceu")
            break
        elif(robos[0].pontos_de_vida <= 0 and robos[1].pontos_de_vida <= 0):
            print_status(robos)
            print(f"EMPATE")
            break
        