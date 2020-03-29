for pixel in range(0, PANTALLA_ANCHO):
  # Calculamos los valores necesarios...
  fov_inicio = jugador_rot - FOV / 2
  rayo_espaciado = pixel * (FOV / PANTALLA_ANCHO)

  # ... para encontrar el angulo del rayo
  rayo_angulo = fov_inicio + pixel * rayo_espaciado

  distancia = raycast(jugador_x, jugador_y, rayo_angulo)