# La pantalla inicializada globalmente
pantalla = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTO))

# La funcion
def dibujar_rectangulo(x, y, ancho, alto, color):
  global pantalla
  pygame.draw.rect(pantalla, color, pygame.Rect(x, y, ancho, alto))


# Por ejemplo para pintar un rectangulo rojo de 200 x 100 px
dibujar_rectangulo(0, 0, 200, 100, (255, 0, 0))