x = float(input('Qual o preço do produto?'))
D = float(input('Qual a porcentagem do desconto?'))
XD = x - x*(D/100)
print('O valor do produto sem desconto é {} reais, o valor do produto com o desconto é {} reais, você economizou {} reais '.format( x, XD, x*(D/100)))
