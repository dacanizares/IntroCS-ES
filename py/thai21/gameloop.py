# Gameloop
while True:        
    # Llamamos el procedimiento
    # para pedir los datos
    jugada = pedir_jugada(rocas)

    # Restamos las rocas
    rocas = rocas - jugada

    # Miramos si termina
    if rocas == 0:
        print 'Ganador!'
        break
    # Si no cambiamos de jugador
    else:
        jugador = not jugador         
