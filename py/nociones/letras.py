# n es el nro palabras
n = int(input('Digite n: '))

anterior = -1
repetidas = 0 
for i in range(0, n):
  # leemos el actual
  palabra = int(input('Digite palabra: '))
  # miramos si se forma un nuevo grupo
  if palabra != anterior:
    repetidas = repetidas + 1
  # actualizamos para la siguiente iteracion
  anterior = palabra
