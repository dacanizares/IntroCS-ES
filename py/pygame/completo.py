import pygame

# Pantalla
PANTALLA_ANCHO = 320
PANTALLA_ALTO = 240

# Coordenadas cuadrado
x = 0
y = 0

# Teclas presionadas
arriba = False
derecha = False
abajo = False
izquierda = False

# Pygame
pygame.init()
pantalla = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTO))


## Dibuja un rectangulo en la pantalla
## -----------------------------------
## Recibe las coordenadas y dimensions
## El parametro color debe ser una tupla (R,G,B)
def dibujar_rectangulo(x, y, ancho, alto, color):
  global pantalla
  pygame.draw.rect(pantalla, color, pygame.Rect(x, y, ancho, alto))


## Actualiza los eventos recibidos 
## ------------------------------------
## Actualiza las teclas presionadas
## Retorna -1 si se recibe un evento
## para cerrar el juego. En otro caso
## retorna 0.
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

  # Nunca se encontro el evento salir
  return 0

# Reloj para controlar el maximo de FPS
reloj = pygame.time.Clock()
# Gameloop
while True:
  if actualizar_eventos() == -1:
    break

  # Movimiento del rectangulo
  if arriba:
    y -= 1
  if abajo:
    y += 1
  if derecha:
    x += 1
  if izquierda:
    x -= 1

  # Borramos la pantalla que estaba pintada
  dibujar_rectangulo(0, 0, PANTALLA_ANCHO, PANTALLA_ALTO, (0, 0, 0))

  # Dibujamos un rectangulo rojo
  # Notese el RGB: (255, 0, 0) 
  dibujar_rectangulo(x, y, 20, 30, (255, 0, 0))
  
  # Actualizamos 
  pygame.display.flip()
  reloj.tick(60)