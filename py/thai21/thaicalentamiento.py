import random

def pedir_jugada(rocas, jugador):
    if jugador:
        r = rocas % 4
        # Si se puede aplicar la estrategia
        if r != 0:
            # Se retorna
            return r
        # Sino
        else:
            # Se retorna un valor al azar
            return random.randint(1, min(3, rocas))
        
    while True:
        jugada = input('Digite rocas a tomar ')
        if jugada<=rocas and jugada>=1 and jugada<=3:
            return jugada

# Elegimos un jugador al azar
r = random.randint(0, 1)
if r == 0:
    jugador = True
else:
    jugador = False
    
rocas = 21
while True:
    print 'Quedan ', rocas, ' rocas'
    jugada = pedir_jugada(rocas, jugador)    
    rocas = rocas - jugada    
    if rocas == 0:
        if jugador:
            print 'Gana el computador!'
        else:
            print 'Gana el humano!'
        break
    else:
        jugador = not jugador         
