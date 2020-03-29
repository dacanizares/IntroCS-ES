
# Dibujamos el techo
dibujar_rectangulo(0, 0, PANTALLA_ANCHO, PANTALLA_ALTO / 2, (0, 0, 0))
# Dibujamos el piso
dibujar_rectangulo(0, PANTALLA_ALTO / 2, PANTALLA_ANCHO, PANTALLA_ALTO / 2, (170, 85, 0))

# ...

for pixel in range(0, PANTALLA_ANCHO):
  # ...

  # Pintamos el fragmento de muro
  techo = PANTALLA_ALTO / 2.0 - (PANTALLA_ALTO / distancia)
  piso = techo
  shading = max(0, 1 - distancia / DISTANCIA_MAX_RAYO)
  dibujar_rectangulo(pixel, techo, 1, PANTALLA_ALTO - techo - piso, (0, 255 * shading, 0))