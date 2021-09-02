import math
x = float(input('digite o angulo aqui: (em graus)'))
s = float(math.sin(math.radians(x)))
c = float(math.cos(math.radians(x)))
t = float(math.tan(math.radians(x)))
print('o agulo que você digitou foi {}'.format(x))
print('o seno do angulo é {:.2f}'.format(s))
print('o cosseno do angulo é {:.2f}'.format(c))
print('a tangente do angulo é {:.2f}'.format(t))
