import random
from carta import Carta
cantidad_cartas = 3

class Mazo():
    def __init__(self):
        self._mazo_cartas = []
        self.armar_mazo(cantidad_cartas)

    @property
    def mazo_cartas(self):
        return self._mazo_cartas
    
    @mazo_cartas.setter
    def mazo_cartas(self,mazo_cartas_nuevo):
        self._mazo_cartas = mazo_cartas_nuevo

    def armar_mazo(self,cant_cartas):
        for i in range(cant_cartas):
            valor_carta = random.randint (-10,10)
            carta = Carta(valor_carta+i-i)
            self._mazo_cartas.append(carta)

    def sacar_carta(self):
        if len(self.mazo_cartas) > 0:
            return self.mazo_cartas.pop()
        else:
            return None