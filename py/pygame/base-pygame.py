import pygame

# Pantalla
PANTALLA_ANCHO = 320
PANTALLA_ALTO = 240

# Teclas presionadas
arriba = False
derecha = False
abajo = False
izquierda = False

# Pygame
pygame.init()
pantalla = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTO))
fuente = pygame.font.Font(None, 30)


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

  # Dibujamos un rectangulo rojo
  # Notese el RGB: (255, 0, 0) 
  dibujar_rectangulo(0, 0, PANTALLA_ANCHO, PANTALLA_ALTO / 2, (255, 0, 0))
  
  # Pintamos los FPS actuales
  fps = fuente.render(str(int(reloj.get_fps())), True, (255, 0, 0))
  pantalla.blit(fps, (50, 50))
  
  # Actualizamos 
  pygame.display.flip()
  reloj.tick(60)