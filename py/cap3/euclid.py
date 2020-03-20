def euclides(a, b):
    while b != 0:
        # Se calcula el residuo
        r = a % b
        
        # Se realizan los intercambios
        a = b
        b = r
        
    return a
