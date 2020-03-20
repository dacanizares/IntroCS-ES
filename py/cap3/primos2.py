def es_primo(n):
    # Casos triviales
    if n <= 1:
        return False
    elif n == 2:
        return True
    elif n % 2 == 0:
        return False
    # Revisamos si tiene otro divisor
    for i in range(3, sqrt(n)):
        if n % i == 0:
            return False
    return True
