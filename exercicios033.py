a = float(input('qual o primeiro numero? '))
b = float(input('qual o segundo numero? '))
c = float(input('qual o terceiro numero? '))
if a > b and a > c:
    print('o numero {} é o maior de todos '.format(a))
if b > a and b > c:
    print('o numero {} é o maior de todos '.format(b))
if c > b and c > a:
    print('o numero {} é o maior de todos '.format(c))
if a < b and a < c:
    print('o numero {} é o menor de todos '.format(a))
if b < a and b < c:
    print('o numero {} é o menor de todos '.format(b))
if c < b and c < a:
    print('o numero {} é o menor de todos '.format(c))
if a < b and a > c or a > b and a < c:
    print('o numero {} é o do meio  '.format(a))
if b < a and b > c or b > a and b < c:
    print('o numero {} é o do meio  '.format(b))
if c < b and c > a or c > b and c < a:
    print('o numero {} é o do meio '.format(c))