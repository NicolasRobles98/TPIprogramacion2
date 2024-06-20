from usuario import Usuario

class Player(Usuario):
    
    id_counter = 1
 
    def __init__(self, nombre):
        super().__init__(nombre)
        self._puntos = 0
        self._id = Player.id_counter
        Player.id_counter += 1 

    @property
    def puntos(self):
        return self._puntos
    
    @puntos.setter
    def puntos(self,puntos_nuevo):
        self._puntos = puntos_nuevo

    @property
    def id(self):
        return self._id
    
    def agregar_puntos(self, valor):
        self.puntos = self.puntos + valor
        return self.puntos
    
    
    