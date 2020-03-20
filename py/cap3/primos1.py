n = input()
if n <= 1:
    print False
elif n == 2:
    print True
elif n % 2 == 0:
    print False
else:
    primo = True
    for i in range(3, sqrt(n)):
        if n % i == 0:
            primo = False
    print primo
