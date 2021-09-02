import random
a1 = input("digite o nome do primeiro aluno ")
a2 = input("digite o nome do segundo aluno ")
a3 = input("digite o nome do terceiro aluno ")
a4 = input("digite o nome do quarto aluno ")
lista = [a1 , a2 , a3 , a4]
random.shuffle(lista)
print("a ordem soreada foi:{}".format(lista))