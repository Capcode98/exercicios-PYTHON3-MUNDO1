import random
numero = int(random.randint(1, 5))
resposta = int(input('qual o numero que vc acha q o computador pensou?'))
if resposta == numero:
    print('parabens vc acertou!')
else:
    print('tente novamente!')
print(numero)
