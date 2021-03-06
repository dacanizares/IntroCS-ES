MITAD = PANTALLA_ALTO / 2
# Dibujamos el techo
dibujar_rectangulo(0, 0, PANTALLA_ANCHO, MITAD, (0, 0, 0))
# Dibujamos el piso
dibujar_rectangulo(0, MITAD, PANTALLA_ANCHO, MITAD, (170, 85, 0))
# ...

for pixel in range(0, PANTALLA_ANCHO):
  # Calculos de las distancias con raycasts
  # ...

  # Pintamos el fragmento de muro
  techo = max(0, PANTALLA_ALTO / 2.0 - PANTALLA_ALTO / distancia)
  piso = techo
  muro = PANTALLA_ALTO - techo - piso
  shading = max(0, 1 - distancia / DISTANCIA_MAX_RAYO)
  dibujar_rectangulo(pixel, techo, 1, muro, (0, 255 * shading, 0))