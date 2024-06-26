from juego import Juego

print("\n-------------BIENVENIDO AL JUEGO DE CARTAS---------------- \n")

juego = Juego()
incorrecto = True
while incorrecto:
    num_jugadores = int(input("Ingresa el número de jugadores: "))
    if num_jugadores > 0 :
        incorrecto = False
        for i in range(num_jugadores):
            nombre = input(f"Ingresa el nombre del jugador {i + 1}: ")
            juego.agregar_jugador(nombre)

    else:
        print("La cantidad de jugadores es incorrecta")


juego.iniciar_juego()
