ano = int(input('digite o ano que você queira saber se é bissexto '))
if ano % 4 == 0 and ano % 400 == 0 or ano % 100 != 0:
    print('{} é um ano bissexto'.format(ano))
else:
    print('{} não é um ano bissexto '.format(ano))
