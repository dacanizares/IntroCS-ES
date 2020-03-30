if adelante:
    jugador_x +=  velocidad * math.sin(jugador_rot)
    jugador_y +=  velocidad * math.cos(jugador_rot)
if atras:
    jugador_x -=  velocidad * math.sin(jugador_rot)
    jugador_y -=  velocidad * math.cos(jugador_rot)
if derecha:
    jugador_rot += velocidad_rot
if izquierda:
    jugador_rot -= velocidad_rot
