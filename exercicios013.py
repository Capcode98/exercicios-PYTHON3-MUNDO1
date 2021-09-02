x = float(input('qual o salario do funcionario sem o aumento?'))
A = float(input('Qual a porcentagem do aumento?'))
XA = x + x*(A/100)
print('o salario do funcionario sem o aumento de {}% era {} reais, com o aumento foi para {} reais, com o acrecimo de {} reais'.format( A, x, XA, x*(A/100)))
