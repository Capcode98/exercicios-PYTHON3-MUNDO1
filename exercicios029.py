v = int(input('qual a velocidade do carro em KM/h?'))
if v <= 80:
    print('o seu veiculo está dentro do limite de velocidade!')
else:
    multa = (v - 80)*7
    print('você execeu o limite de velocidade portanto tera de pagar uma multa de valor {}'.format(multa))
