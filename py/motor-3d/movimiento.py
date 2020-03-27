if tecla_adelante:
    jugador_x +=  velocidad * math.sin(jugador_rot)
    jugador_y +=  velocidad * math.cos(jugador_rot)
if tecla_atras:
    jugador_x -=  velocidad * math.sin(jugador_rot)
    jugador_y -=  velocidad * math.cos(jugador_rot)
if tecla_derecha:
    jugador_rot += velocidad_rot
if tecla_izquierda:
    jugador_rot -= velocidad_rot
