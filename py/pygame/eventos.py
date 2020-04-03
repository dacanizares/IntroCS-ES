# Variables globales para las teclas presionadas
arriba = False
derecha = False
abajo = False
izquierda = False

# La funcion
def actualizar_eventos():
  global arriba, derecha, abajo, izquierda

  for evento in pygame.event.get():
    # Salir del juego (?)
    if evento.type == pygame.QUIT:
      return -1
    # Solo nos interesan los eventos del teclado
    if evento.type not in [pygame.KEYDOWN, pygame.KEYUP]:
      continue
    # Mapeos de las teclas
    if evento.key == pygame.K_UP:
      arriba = evento.type == pygame.KEYDOWN
    if evento.key == pygame.K_RIGHT:
      derecha = evento.type == pygame.KEYDOWN
    if evento.key == pygame.K_DOWN:
      abajo = evento.type == pygame.KEYDOWN
    if evento.key == pygame.K_LEFT:
      izquierda = evento.type == pygame.KEYDOWN 

# Ejemplo de uso
while True:
  if actualizar_eventos() == -1:
    break

  if arriba:
    # Hacer algo

  # Y pintar la pantalla