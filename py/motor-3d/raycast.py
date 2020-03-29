def toca_muro(x, y):
  if x < 0 or x >= MAPA_ANCHO:
    return False
  if y < 0 or y >= MAPA_ALTO:
    return False
  return mapa[y][x] == '#'

def raycast(x, y, rot):
  distancia = 0
  while distancia < DISTANCIA_MAX_RAYO: 
    distancia += 0.1 
    rayo_x = math.floor(x + math.sin(rot) * distancia)
    rayo_y = math.floor(y + math.cos(rot) * distancia)

    if toca_muro(rayo_x, rayo_y):
      return distancia  
  return distancia