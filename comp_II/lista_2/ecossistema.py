# Rubens Guedes Kaiserman
# Feito sem consultar o gabarito
# 122119151

# fugindo
class Presa:
    def fugir(self):
        print("Estou fugindo. ó meu deos")

# caçando
class Predador:
    def cacar(self):
        print("O pai foi a caça. Hihi.")
        

class Gato(Predador):
    pass

class Rato(Presa):
    pass

class Hipocondriaco(Presa, Predador):
    pass


# Testes
gato = Gato()
rato = Rato()
hipocondriaco = Hipocondriaco()

gato.cacar()
rato.fugir()
hipocondriaco.cacar()
hipocondriaco.fugir()