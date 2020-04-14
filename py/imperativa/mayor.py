n = int(input('Digite n: '))
mayor = 0
for i in range(0, n):
  numero = int(input('Digite numero positivo: '))
  if numero > mayor:
    mayor = numero

print('El mayor es ', mayor)