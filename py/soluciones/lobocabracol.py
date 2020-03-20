# Pinta el juego
def pintar(granjero, lobo, cabra, col):
    if granjero:
        print "     |        | G "
    else:
        print " G   |        |   "
    if lobo:
        print "     |        | L "
    else:
        print " L   |        |   "
    if cabra:
        print "     |        | C "
    else:
        print " C   |        |   "
    if col:
        print "     |        | COL "
    else:
        print " COL |        |   "
    print ""

def pierde(granjero, lobo, cabra, col):
    if lobo == cabra and cabra != granjero:
        return True
    if cabra == col and col != granjero:
        return True
    return False

def gana(granjero, lobo, cabra, col):
    # Si todos estan en true, retorna true,
    # en cualquier otro caso retorna false
    return granjero and lobo and cabra and col

def pedir_movimiento():
    while True:
        m = input('1-Lobo 2-Cabra 3-Col 0-Ninguno')
        if m >= 0 and m <= 3:
            return m

#Estado inicial
granjero = False
cabra = False
lobo = False
col = False
# Se pinta el estado inicial
pintar(granjero,lobo,cabra,col)
# Gameloop
while True:
    m = pedir_movimiento()
    # Se modifica el estado
    if m == 1:
        lobo = not lobo
    elif m == 2:
        cabra = not cabra
    elif m == 3:
        col = not col
    # El granjero siempre se mueve
    granjero = not granjero
    # Pintamos el resultado
    pintar(granjero,lobo,cabra,col)    

    # Miramos si hay gameover
    if pierde(granjero, lobo, cabra, col):
        print 'Pierde'
        break
    if gana(granjero, lobo, cabra, col):
        print 'Gana'
        break
