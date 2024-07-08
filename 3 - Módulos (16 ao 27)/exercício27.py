nome = str(input('Digite seu nome completo: '))

nome = nome.split()
ultimonome = len(nome)

print('É um prazer te conhecer!')
print('Seu primeiro nome é {}'.format(nome [0]))
print('Seu ultimo nome é {}'.format(nome [ultimonome-1]))

#Resposta do professor
#print('Seu primeiro nome é {}'.format(nome [0]))
#print('Seu ultimo nome é {}'.format(nome[len(nome)-1]))
