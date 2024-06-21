from usuario import Usuario

class Player(Usuario):
    
    id_jugadores = 1
 
    def __init__(self, nombre):
        super().__init__(nombre)
        self._puntos = 0
        self._retirado = False
        self._id = Player.id_jugadores
        Player.id_jugadores += 1 

    @property
    def puntos(self):
        return self._puntos
    
    @puntos.setter
    def puntos(self,puntos_nuevo):
        self._puntos = puntos_nuevo
        
    @property
    def retirado(self):
        return self._retirado
    
    @retirado.setter
    def retirado(self,retirado_nuevo:bool):
        self._retirado = retirado_nuevo


    @property
    def id(self):
        return self._id
    
    def agregar_puntos(self, valor):
        self.puntos = self.puntos + valor
        return self.puntos
    
    
    