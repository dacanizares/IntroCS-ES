# USANDO UN WHILE
# Tenemos que realizar una asignacion previa
# que permita entrar al ciclo
n = -1
while n < 0:
    n = input('Digite nro positivo ')
print 'El dato es valido'


# USANDO UN WHILE TRUE
# Hay que poner la condicion de salida 
while True:
    n = input('Digite nro positivo ')
    if n >= 0:
        break
print 'El dato es valido'
