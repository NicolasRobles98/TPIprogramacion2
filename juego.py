from mazo import Mazo
from jugador import Player
from usuario import Usuario

class Juego():
    def __init__(self):
        self._jugadores = []
        self._mazo = Mazo()
        self._ganador = ""
        
    def agregar_jugador(self, nombre):
        jugador = Player(nombre)
        self._jugadores.append(jugador)
        
    def retirar_jugador(self, jugador: Player):
        self._jugadores.remove(jugador)
        
    def iniciar_juego(self):
         while len(self._mazo.cartas) > 0 and len(self._jugadores) > 0:
            for jugador in self._jugadores:
                print(f"\nTurno de {jugador.nombre}")
                accion = input("Escribe '1' para sacar una carta o '2' para retirarte del juego: ").strip().lower()

                if accion == "2":
                    print(f"{jugador.nombre} ha decidido retirarse del juego.")
                    self.retirar_jugador(jugador)
                    continue

                if accion == "1":
                    carta = self._mazo.sacar_carta()
                    if carta:
                        print(f"{jugador.nombre} ha sacado una carta con valor {carta.valor}.")
                        jugador.agregar_puntos(carta.valor)
                    else:
                        print("No hay más cartas en el mazo.")
                        break
         self.terminar_juego()
        
            


    def terminar_juego(self):
        print("\nResultados finales:")

        # Ordenar jugadores por puntos (opcional)
        self._jugadores.sort(key=lambda jugador: jugador.puntos, reverse=True)

        max_puntos = self._jugadores[0].puntos  # Puntos del primer jugador

        ganadores = []
        for jugador in self._jugadores:
            if jugador.puntos == max_puntos:
                ganadores.append(jugador.nombre)
            else:
                break  # Como están ordenados, si no hay empate con el primer jugador, no hay más empates
            
        if len(ganadores) == 1:
            print(f"{ganadores[0]} ha ganado con {max_puntos} puntos!")
        else:
            print("Empate entre los siguientes jugadores:")
            for nombre in ganadores:
                print(f"{nombre} con {max_puntos} puntos.")

        self._ganador = ganadores[0]  # Guardar el nombre del primer ganador (por ejemplo)


        