from random import randint

print('-=-' * 10)
usuario = int(input('Digite um numero de 0 a 5: '))

maquina = randint(0,5)

print('-=-' * 10)
if maquina == usuario:
    print('Você acertou')
else: 
    print('Você errou')
print('Maquina {}'.format(maquina))
print('Usuario {}'.format(usuario))
print('-=-' * 10)
