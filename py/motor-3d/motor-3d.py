import pygame
import math

# Posicion del jugador
jugador_x = 6
jugador_y = 6

# Direccion
jugador_rot = 0

# Velocidad
velocidad = 0
velocidad_rot = 0

# Para un FOV de 90 grados aprox.
FOV = 3.14159 / 4.0

# Otras constantes
PANTALLA_ANCHO = 320
PANTALLA_ALTO = 240
DISTANCIA_MAX_RAYO = 7

# Mapa
MAPA_ANCHO = 10
MAPA_ALTO = 10
mapa = []

# Teclas presionadas
arriba = False
derecha = False
abajo = False
izquierda = False

# Pygame
pygame.init()
fuente = pygame.font.Font(None, 30)
pantalla = pygame.display.set_mode((PANTALLA_ANCHO, PANTALLA_ALTO))


def cargar_mapa():
  global map
  mapa.append("##########")
  mapa.append("#...#....#")
  mapa.append("#........#")
  mapa.append("###.####.#")
  mapa.append("#...#....#")
  mapa.append("#...#....#")
  mapa.append("#........#")
  mapa.append("#...#..###")
  mapa.append("#..##....#")
  mapa.append("##########")

def toca_muro(x, y):
  if x < 0 or x >= MAPA_ANCHO:
    return False
  if y < 0 or y >= MAPA_ALTO:
    return False
  return mapa[y][x] == '#'

def dibujar_rectangulo(x, y, ancho, alto, color):
  global pantalla
  pygame.draw.rect(pantalla, color, pygame.Rect(x, y, ancho, alto))


def raycast(x, y, rot):
  distancia = 0
  direccion_x = math.sin(rot)
  direccion_y = math.cos(rot)
  while distancia < DISTANCIA_MAX_RAYO:
    distancia += 0.1
    rayo_x = math.floor(x + direccion_x * distancia)
    rayo_y = math.floor(y + direccion_y * distancia)

    if toca_muro(rayo_x, rayo_y):
      return distancia
  return DISTANCIA_MAX_RAYO


def actualizar_eventos():
  global arriba, derecha, abajo, izquierda

  for evento in pygame.event.get():
    # Salir del juego (?)
    if evento.type == pygame.QUIT:
      return -1
    # Solo nos interesan los eventos del teclado
    if evento.type != pygame.KEYDOWN and evento.type != pygame.KEYUP:
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

  # Nunca se encontró el evento salir
  return 0


reloj = pygame.time.Clock()
cargar_mapa()

# Gameloop
while True:
  if actualizar_eventos() == -1:
    break

  if arriba:
    jugador_x +=  0.1 * math.sin(jugador_rot)
    jugador_y +=  0.1 * math.cos(jugador_rot)
  if abajo:
    jugador_x -=  0.1 * math.sin(jugador_rot)
    jugador_y -=  0.1 * math.cos(jugador_rot)
  if izquierda: 
    jugador_rot -= 0.05
  if derecha: 
    jugador_rot += 0.05

  # Dibujamos el techo
  dibujar_rectangulo(0, 0, PANTALLA_ANCHO, PANTALLA_ALTO / 2, (0, 0, 0))
  # Dibujamos el piso
  dibujar_rectangulo(0, PANTALLA_ALTO / 2, PANTALLA_ANCHO, PANTALLA_ALTO / 2, (170, 85, 0))
  
  # Calculamos los valores necesarios...
  fov_inicio = jugador_rot - FOV / 2
  rayo_espaciado = FOV / PANTALLA_ANCHO
  # Calculamos las distancias en el FOV
  for pixel in range(0, PANTALLA_ANCHO):
    # ... para encontrar el angulo del rayo
    rayo_angulo = fov_inicio + pixel * rayo_espaciado
    distancia = raycast(jugador_x, jugador_y, rayo_angulo)     
      
    # Pintamos el fragmento de muro
    muro = PANTALLA_ALTO - (PANTALLA_ALTO / distancia)
    shading = max(0, 1 - distancia / DISTANCIA_MAX_RAYO)
    dibujar_rectangulo(pixel, muro / 2, 1, PANTALLA_ALTO - muro, (0, 255 * shading, 0))   

  fps = fuente.render(str(int(reloj.get_fps())), True, (255, 0, 0))
  pantalla.blit(fps, (50, 50))
  pygame.display.flip()
  reloj.tick(60)