# Dolares
x = input()
# Nro de juegos
n = input()

comprados = 0
# Para cada juego
for i in range(0, n):
    precio = input()
    # Verificamos si se puede comprar
    if x >= precio:
        # Si lo compramos nos queda
        # menos dinero
        x = x - precio
        comprados = comprados + 1 

print comprados
