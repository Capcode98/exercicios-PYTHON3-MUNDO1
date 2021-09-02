from math import sqrt
Ca = float(input('digite o valor do primeiro cateto do triangulo retangulo aqui:'))
Co = float(input('digite o valor do segundo cateto do triangulo retangulo aqui:'))
H = sqrt(Ca**2 + Co**2)
print('o valor dos catetos são {} e {}, e a hipotenusa é {}'.format(Ca, Co, H))
