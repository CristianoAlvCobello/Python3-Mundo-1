from random import choice

aluno1 = input('Nome do aluno 1: ')
aluno2 = input('Nome do aluno 2: ')
aluno3 = input('Nome do aluno 3: ')
aluno4 = input('Nome do aluno 4: ')
aluno5 = input('Nome do aluno 5: ')

lista = [aluno1, aluno2, aluno3, aluno4, aluno5]
sorteado = choice(lista)

print('O aluno sortudo foi {}'.format(sorteado))
