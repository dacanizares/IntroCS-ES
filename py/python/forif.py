a = int(input('Digite nro. '))
b = int(input('Digite nro. '))

for i in range(a, b):
  print(i)
  if i < 0:
    print('Es negativo')
  else:
    print('No es negativo')
