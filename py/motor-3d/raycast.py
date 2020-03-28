distancia = 0
golpe_muro = False
while not golpe_muro and distancia <= DISTANCIA_MAX_RAYO: 
    distanceToWall += 0.1
    rayo_x = math.floor(jugador_x + math.sin(jugador_rot) * distancia)
    rayo_y = math.floor(jugador_y + math.cos(jugador_rot) * distancia)

    if toca_muro(rayo_x, rayo_y):
        golpe_muro = True