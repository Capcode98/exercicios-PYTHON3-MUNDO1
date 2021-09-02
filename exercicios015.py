D = float(input('quantos dias o carro foi alugado?'))
d = float(input('qual a distancia percorrida (em KM)?'))
T = D*60 + d*0.15
print('o total a pagar, por ter alugado {} dias e ter percorrido {} km, é {} reais'.format( D, d, T))
