import random
print('digite os nomes dos alunos para serem sorteados a seguir!')
A = input('primeiro aluno:')
B = input('segundo aluno:')
C = input('terceiro aluno:')
D = input('quarto aluno:')
k = random.choice([A, B, C, D])
print('o aluno sorteado foi {}!'.format(k))
