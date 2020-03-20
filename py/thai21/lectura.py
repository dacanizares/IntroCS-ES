# Lectura de datos
def pedir_jugada(rocas):
    while True:
        jugada = input('Digite rocas a tomar ')
        # Solo retorna si se cuplen las condiciones
        # en otro caso se queda en el While True
        if jugada<=rocas and jugada>=1 and jugada<=3:
            return jugada
