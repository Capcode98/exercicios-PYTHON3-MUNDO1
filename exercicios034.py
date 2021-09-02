s = float(input('qual o seu salário ? (em reais)'))
if s >= 1250:
    a = float((s*10/100) + (s))
    print('seu salario é {} e seu almento foi de {}'.format(s, a))
else:
    a = float((s*15/100) + (s))
    print('seu salario é {} e seu almento foi de {}'.format(s, a))
