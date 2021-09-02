numero = int(input('digite um numero: '))
k = float((numero/2) - (numero//2))
if k != 0.0:
    print('{} é um numero impar'.format(numero))
else:
    print('{} é um numero par'.format(numero))
