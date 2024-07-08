nome = str(input('Qual seu nome? ')).strip()

print('Letras em maiúsculo: {}'.format(nome.upper()))
print('Letras em minusculo: {}'.format(nome.lower()))
print('Quantidade de letras: {}'.format(len(''.join(nome.split()))))
print('Seu primeiro nome é {} e tem {} letras'.format(nome, len(nome.split() [0] [0:])))

#resposta do professor 
#print('Quantidade de letras: {}'.format(len(nome)-nome.count(' ')))
#print('Quantidade de letras do primeiro nome {}'.format(nome.find' '))
