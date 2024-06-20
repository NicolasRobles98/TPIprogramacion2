from abc import ABC, abstractmethod

class Usuario():
    def __init__(self,nombre):
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre
    
    @nombre.setter
    def nombre(self,nombre_nuevo):
        self._nombre = nombre_nuevo