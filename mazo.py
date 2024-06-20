import random
from carta import Carta

cantidad_cartas = 4

class Mazo():
    def __init__(self):
        self._cartas = []
        self.armar_mazo(cantidad_cartas)

    @property
    def cartas(self):
        return self._cartas
    
    @cartas.setter
    def mazo_cartas(self,mazo_cartas_nuevo):
        self._cartas = mazo_cartas_nuevo

    def armar_mazo(self,cant_cartas):
        for i in range(cant_cartas):
            valor_carta = random.randint (-10,10)
            carta = Carta(valor_carta)
            self._cartas.append(carta)

    def sacar_carta(self):
        if len(self._cartas) > 0:
            return self._cartas.pop()
        else:
            return None