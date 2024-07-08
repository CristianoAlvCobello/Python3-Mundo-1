velocidade = int(input('Qual a sua velocidade? '))

if velocidade<=80:
    print('Você não recebera multa')
else:
    velocidadeacima = velocidade-80
    multa = velocidadeacima*7
    print('MULTADO! Você recebera uma multa de R${}'.format(multa))
