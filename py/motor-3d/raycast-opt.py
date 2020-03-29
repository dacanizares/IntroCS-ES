def raycast(x, y, rot):
  distancia = 0
  # Precalculamos los valores...
  direccion_x = math.sin(rot)
  direccion_y = math.cos(rot)
  while distancia < DISTANCIA_MAX_RAYO: 
    distancia += 0.1
    # ...y los reutilizamos aqui
    rayo_x = math.floor(x + direccion_x * distancia)
    rayo_y = math.floor(y + direccion_y * distancia)

    if toca_muro(rayo_x, rayo_y):
      return distancia
  return DISTANCIA_MAX_RAYO