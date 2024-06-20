from usuario import Usuario

class Player(Usuario):
    def __init__(self, nombre,id):
        super().__init__(nombre)
        self._puntos = 0
        self._id = id

    @property
    def puntos(self):
        return self._puntos
    
    @puntos.setter
    def puntos(self,puntos_nuevo):
        self._puntos = puntos_nuevo

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,id_nuevo):
        self._id = id_nuevo

    def modificar_puntos(self, valor):
        self.puntos = self.puntos + valor
        return self.puntos