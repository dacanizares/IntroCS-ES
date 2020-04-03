# Variables generales
jugador_x = 0

# Gameloop
while True:
  if termina_juego():
    break
  
  # Revisamos teclas
  if tecla_derecha:
    # Actualizamos datos
    jugador_x += 1

  # Pintamos de acuerdo los nuevos datos
  pintar_jugador(jugador_x)
