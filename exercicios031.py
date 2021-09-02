d = float(input('qual a distancia toatl que será percorrida pela viagem (em km)'))
if d <= 200:
    custo = d*(1/2)
    print('ocusto da viagem sera {}'.format(custo))
else:
    cust = d*(0.45)
    print('o custo sera {}'.format(cust))
