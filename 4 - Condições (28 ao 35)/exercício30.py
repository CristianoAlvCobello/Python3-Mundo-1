numero = int(input('Digite um número: '))

parouimpar = numero % 2

if parouimpar == 0:
    print('{} é par'.format(numero))
else:
    print('{} é impar'.format(numero))
    