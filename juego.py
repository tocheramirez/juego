import random

puntmaquina = 0
puntjugador = 0

 opciones=["piedra", "papel", "tijera"] 

while puntmaquina < 3 and puntjugador < 3:
        print(f"\nMarcador es: Jugador {puntjugador} - Maquina {puntmaquina}")

        maquina = random.choice(opciones)
        jugador = input("Elige piedra, papel o tijera: ").lower()

        if jugador not in ["piedra", "papel", "tijera"]:
            print("Opción no válida, por favor elige piedra, papel o tijera.")
            continue


        if jugador == maquina:
            print("Empate!")
        elif (jugador == "piedra" and maquina == "tijera") or \
            (jugador == "papel" and maquina == "piedra")or\
                (jugador == "tijera" and maquina == "papel"):
            print("¡Ganaste!")
            puntjugador += 1
        else:
            print("perdiste!")  
            puntmaquina += 1

if puntjugador == 3:
    print("¡Felicidades, ganaste el juego!")
else:    print("¡La máquina ganó el juego, mejor suerte la próxima vez!")   
