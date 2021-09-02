n = str(input('digite seu nome completo:')).strip().capitalize()
p = n.split()
a = p[0]
print('seu primeiro nome é {}'.format(a))
print('o seu ultimo nome é {}'.format(p[len(p)-1]))
