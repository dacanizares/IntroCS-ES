n = input()
divisores = 2
for divisor in range(2,n):
	if n % divisor == 0:
		divisores = divisores + 1
print('Tiene ', divisores, ' divisores')
		
if divisores == 2 and n != 1:
	print('Es primo')