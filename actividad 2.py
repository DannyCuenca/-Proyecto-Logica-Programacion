import random

victorias = 0
derrotas = 0
empates = 0

while True:

    print("\n=== PIEDRA PAPEL O TIJERA ===")
    print("1. Piedra")
    print("2. Papel")
    print("3. Tijera")

    jugador = input("Seleccione una opción: ")

    opciones = ["Piedra", "Papel", "Tijera"]
    computadora = random.choice(opciones)

    if jugador == "1":
        jugador_eleccion = "Piedra"
    elif jugador == "2":
        jugador_eleccion = "Papel"
    elif jugador == "3":
        jugador_eleccion = "Tijera"
    else:
        print("Opción inválida")
        continue

    print("Jugador:", jugador_eleccion)
    print("Computadora:", computadora)

    if jugador_eleccion == computadora:
        print("Empate")
        empates += 1

    elif (
        (jugador_eleccion == "Piedra" and computadora == "Tijera") or
        (jugador_eleccion == "Papel" and computadora == "Piedra") or
        (jugador_eleccion == "Tijera" and computadora == "Papel")
    ):
        print("Ganaste")
        victorias += 1

    else:
        print("Perdiste")
        derrotas += 1

    print(f"Victorias: {victorias}")
    print(f"Derrotas: {derrotas}")
    print(f"Empates: {empates}")

    repetir = input("¿Desea jugar otra vez? (s/n): ")

    if repetir.lower() != "s":
        break

print("Fin del juego")