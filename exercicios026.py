f = str(input('digite uma frase:')).strip().lower()
print('tem {} letras "a"'.format(f.count('a')))
print('a primeira letra "a" apareceu na posição {}'.format(f.count('a')+1))
print('a ultima letra "a" apareceu na posição {}'.format(f.rfind('a')+1))
