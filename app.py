from juego import Juego

print("\n-------------BIENVENIDO AL JUEGO DE CARTAS---------------- \n")

juego = Juego()
num_jugadores = int(input("Ingresa el número de jugadores: "))
for i in range(num_jugadores):
    nombre = input(f"Ingresa el nombre del jugador {i + 1}: ")
    juego.agregar_jugador(nombre)


juego.iniciar_juego()
