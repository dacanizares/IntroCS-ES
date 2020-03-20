# Punto 1
def multiplicar(a, b):
    m = 0
    for i in range(0, b):
        m = m + a
    return m

# Punto 2
def potencia(a, b):
    p = 1
    for i in range(0, b):
        p = multiplicar(p, a)
    return p

# Punto 3
a = input()
b = input()
print potencia(a, b)
