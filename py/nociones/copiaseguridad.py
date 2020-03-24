x = int(input())
q = int(input())

# Calculamos el nro de discos
respuesta = x // q
# Si falto un poco de espacio
if x % q != 0:
    # Se debe comprar otro
    respuesta = respuesta + 1

print(respuesta)
