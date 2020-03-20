# Procedimiento utilizando descartes
def atender(disponible, agentes, motorizada, armas, agentes_necesarios, requiere_vehiculos, sospechosos_armados):
    # not disponible es igual que
    # disponible == False

    # requiere_vehiculos es igual que
    # requiere_vehiculos == True    
    if not disponible:
        return False
    if agentes < agentes_necesarios:
        return False
    if not motorizada and requiere_vehiculos:
        return False
    if armas == False and sospechosos_armados:
        return False
    return True

# Pedimos datos de la emergencia
agentes_necesarios = input('Agentes necesarios: ')
requiere_vehiculos = input('Vehiculos: (True | False) ')
sospechosos_armados = input('Sospechosos armados: (True | False) ')
# Pedimos datos de las patrullas
for patrulla in range(0,10):
    print 'Patrulla ', patrulla
    disponible = input('Disponible: (True | False) ')
    agentes = input('Agentes asignados: ')
    motorizada = input('Motorizada: (True | False) ')
    armas = input('Armas: (True | False) ')

    if atender(disponible, agentes, motorizada, armas, agentes_necesarios, requiere_vehiculos, sospechosos_armados):
        print 'Puede atender la emergencia'        
    else:
        print 'No puede'
