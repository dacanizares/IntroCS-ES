# Lectura de datos
def pedir_jugada(rocas, jugador):
    # Si esta jugando el 1 (True)
    # aplicamos la formula
    if jugador:
        return rocas % 4
    # Si no, pedimos una jugada al humano
    while True:
        jugada = input('Digite rocas a tomar ')
        # Solo retorna si se cuplen las condiciones
        # en otro caso se queda en el While True
        if jugada<=rocas and jugada>=1 and jugada<=3:
            return jugada

# Estado inicial del juego
jugador = True
rocas = 21
# Gameloop
while True:
    # Mostramos cuantas rocas quedan
    print 'Quedan ', rocas, ' rocas'
    
    # Llamamos el procedimiento
    # para pedir los datos
    # NO OLVIDAR ENVIAR AL JUGADOR ACTUAL
    jugada = pedir_jugada(rocas, jugador)

    # Restamos las rocas
    rocas = rocas - jugada

    # Miramos si termina
    if rocas == 0:
        print 'Ganador!'
        break
    # Si no cambiamos de jugador
    else:
        jugador = not jugador         
