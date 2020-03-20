# n es el nro palabras
n = input()

anterior = -1
repetidas = 0 
for i in range(0, n):
    # leemos el actual
    palabra = input()
    # miramos si se forma un nuevo grupo
    if palabra != anterior:
        repetidas = repetidas + 1
    # actualizamos para la siguiente iteracion
    anterior = palabra
