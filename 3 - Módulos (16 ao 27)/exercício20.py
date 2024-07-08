from random import shuffle

aluno1 = input('Nome do aluno 1: ')
aluno2 = input('Nome do aluno 2: ')
aluno3 = input('Nome do aluno 3: ')
aluno4 = input('Nome do aluno 4: ')
aluno5 = input('Nome do aluno 5: ')

lista = [aluno1, aluno2, aluno3, aluno4, aluno5]
sorteado = shuffle(lista)

print('A ordem de apresentação será:')
print(lista)
